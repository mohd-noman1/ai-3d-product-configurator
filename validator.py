import os
import json
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# --- 1. LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# .strip().upper() ensures no accidental spaces in your .env break the logic
ACTIVE_LLM = os.getenv("ACTIVE_LLM", "GEMINI").strip().upper() 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
SUBSCRIPTION_KEY = os.getenv("APIM_SUBSCRIPTION_KEY", "").strip()

# --- 2. CONFIGURE CLIENTS ---
AZURE_ENDPOINT_URL = "https://apim-foundry-prod-ltts.azure-api.net/gpt5-mini/deployments/gpt-5-mini/chat/completions?api-version=2024-12-01-preview"

# Safely initialize Gemini only if the key exists
gemini_model = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config={"response_mime_type": "application/json", "temperature": 0.1}
    )

# --- 3. THE CORE VALIDATION ENGINE ---
def analyze_cross_domain_clash(test_case, mech_json_str, elec_json_str, requirements_text):
    """
    Routes the validation request to either Gemini or Azure.
    Includes bulletproof JSON parsing to prevent UI crashes.
    """
    
    system_instruction = """
    You are an expert Electromechanical Systems Engineer validating a design for NexusValidate.
    Your job is to read the Systems Requirements, Mechanical Data, and Electrical Data, and determine if there is an interface failure.
    
    Instructions:
    1. Cross-reference the mechanical parameters against the electrical parameters.
    2. Check if the combined reality violates the Systems Requirements.
    3. You must respond ONLY with a raw, valid JSON object. Do not include markdown formatting.
    
    Required JSON Output Format:
    {
        "status": "PASS" or "FAIL",
        "clash_type": "Spatial", "Thermal", "Routing", "Kinematic", or "None",
        "reason": "A 1-2 sentence technical explanation of exactly what failed and why."
    }
    """

    user_context = f"""
    Context - Test Case: {test_case}
    
    [SYSTEMS REQUIREMENTS]
    {requirements_text}
    
    [MECHANICAL PARAMETERS]
    {mech_json_str}
    
    [ELECTRICAL PARAMETERS]
    {elec_json_str}
    """

    # -----------------------------------------
    # ROUTE A: GEMINI EXECUTION
    # -----------------------------------------
    if ACTIVE_LLM == "GEMINI":
        if not gemini_model:
            return {"status": "FAIL", "clash_type": "Config Error", "reason": "GEMINI_API_KEY is missing from .env file."}
        
        try:
            full_prompt = system_instruction + "\n\n" + user_context
            response = gemini_model.generate_content(full_prompt)
            # Gemini's response_mime_type guarantees clean JSON, so we just load it
            return json.loads(response.text.strip())
            
        except Exception as e:
            print(f"Gemini API Error: {e}")
            return {"status": "FAIL", "clash_type": "API Error", "reason": f"Gemini connection failed: {str(e)}"}

    # -----------------------------------------
    # ROUTE B: AZURE APIM EXECUTION
    # -----------------------------------------
    elif ACTIVE_LLM == "AZURE":
        if not SUBSCRIPTION_KEY:
            return {"status": "FAIL", "clash_type": "Config Error", "reason": "APIM_SUBSCRIPTION_KEY is missing from .env file."}
            
        try:
            headers = {
                "Content-Type": "application/json",
                "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
                "api-key": SUBSCRIPTION_KEY
            }
            payload = {
                "messages": [
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_context}
                ],
                "temperature": 0.1
            }
            
            response = requests.post(AZURE_ENDPOINT_URL, headers=headers, json=payload)
            response.raise_for_status() 
            
            # Parse Azure Response
            response_data = response.json()
            raw_text = response_data["choices"][0]["message"]["content"].strip()
            
            # 🛡️ Bulletproof Markdown Stripper
            if raw_text.startswith("```"):
                lines = raw_text.split('\n')
                # Check if lines exist before attempting to strip them to avoid index errors
                if lines and lines[0].startswith("```"): 
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"): 
                    lines = lines[:-1]
                raw_text = '\n'.join(lines).strip()
                
            return json.loads(raw_text)
            
        except requests.exceptions.RequestException as e:
            print(f"Azure API Error: {e}")
            return {"status": "FAIL", "clash_type": "API Network Error", "reason": "Azure APIM connection failed. Check console for details."}
        except json.JSONDecodeError as e:
            print(f"JSON Parsing Error: {e}")
            print(f"Raw Output was: {raw_text}")
            return {"status": "FAIL", "clash_type": "Data Parsing Error", "reason": "Azure returned invalid JSON format."}

    # -----------------------------------------
    # ROUTE C: FAILSAFE
    # -----------------------------------------
    else:
        return {"status": "FAIL", "clash_type": "Configuration Error", "reason": f"Unknown ACTIVE_LLM: {ACTIVE_LLM}. Must be GEMINI or AZURE."}

# --- Quick Local Test ---
if __name__ == "__main__":
    print(f"🚀 NexusValidate Engine Starting...")
    print(f"⚙️ Active Model: {ACTIVE_LLM}")
    
    dummy_mech = '{"enclosure_type": "sealed_IP67", "ambient_temp_max_c": 45}'
    dummy_elec = '{"component": "motor_driver", "heat_dissipation_w": 28, "max_operating_temp_c": 60}'
    reqs = "The motor driver must be fully sealed for outdoor use and operate below 65°C."
    
    result = analyze_cross_domain_clash("Thermal Trap", dummy_mech, dummy_elec, reqs)
    
    print("\n✅ AI Response:")
    print(json.dumps(result, indent=2))
