import streamlit as st
import plotly.graph_objects as go
import trimesh
import os
from validator import analyze_cross_domain_clash
from test_data import TEST_CASES

# --- PAGE CONFIG ---
st.set_page_config(page_title="NexusValidate 🚀", layout="wide", initial_sidebar_state="expanded")

# --- CAD VISUALIZER WITH HARDCODED PATHS ---
def render_cad_model(status, selected_case):
    # Retrieve the hardcoded path from test_data.py
    file_path = TEST_CASES[selected_case].get("file_path")
    
    mesh_color = 'rgba(255, 50, 50, 0.9)' if status == "FAIL" else ('rgba(50, 255, 50, 0.9)' if status == "PASS" else 'rgba(150, 150, 150, 0.5)')
        
    fig = go.Figure()
    
    # Check if the file exists and attempt to load it
    if file_path and os.path.exists(file_path):
        try:
            mesh = trimesh.load(file_path, file_type='step')
            if isinstance(mesh, trimesh.Scene):
                mesh = trimesh.util.concatenate([geom for geom in mesh.geometry.values()])
            
            fig.add_trace(go.Mesh3d(
                x=mesh.vertices[:, 0], y=mesh.vertices[:, 1], z=mesh.vertices[:, 2], 
                i=mesh.faces[:, 0], j=mesh.faces[:, 1], k=mesh.faces[:, 2], 
                color=mesh_color, opacity=0.8, flatshading=True, name=selected_case
            ))
        except Exception as e:
            st.sidebar.error(f"Error loading CAD: {e}")
            fig = render_fallback_box(mesh_color)
    else:
        fig = render_fallback_box(mesh_color)

    fig.update_layout(
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='data'),
        margin=dict(l=0, r=0, b=0, t=0), 
        height=500
    )
    return fig

def render_fallback_box(color):
    """Fallback if STEP file is missing or fails to render."""
    return go.Figure(data=[go.Mesh3d(
        x=[0,10,10,0,0,10,10,0], y=[0,0,10,10,0,0,10,10], z=[0,0,0,0,10,10,10,10], 
        color=color, opacity=0.5
    )])

# --- CALLBACK TO SYNC TEST DATA ---
def update_inputs():
    case = st.session_state.selected_case
    st.session_state.reqs = TEST_CASES[case]["requirements"]
    st.session_state.json_a = TEST_CASES[case]["data_a"]
    st.session_state.json_b = TEST_CASES[case]["data_b"]

# --- APP LAYOUT ---
st.title("NexusValidate 🚀")
st.subheader("Universal Systems Interface & Verification Engine")

with st.sidebar:
    st.header("1. Scenario Selection")
    # Initialize session state if first run
    if 'selected_case' not in st.session_state:
        st.session_state.selected_case = list(TEST_CASES.keys())[0]
        update_inputs()

    st.selectbox(
        "Load Pre-configured Test Case", 
        options=list(TEST_CASES.keys()), 
        key="selected_case", 
        on_change=update_inputs
    )
    
    st.markdown("---")
    st.header("2. Integration Data")
    requirements = st.text_area("System Requirements (ICD)", key="reqs", height=80)
    json_a = st.text_area("System A State (JSON)", key="json_a", height=100)
    json_b = st.text_area("System B State (JSON)", key="json_b", height=100)

col1, col2 = st.columns([1, 1.2], gap="large")

# --- REPLACE YOUR COL1 LOGIC WITH THIS ---

with col1:
    st.header("Interface Verification")
    if st.button("Run System Sanity Check", type="primary", use_container_width=True):
        with st.spinner("AI is analyzing the interface..."):
            # This call is LIVE. The LLM is thinking right now.
            result = analyze_cross_domain_clash(st.session_state.selected_case, json_a, json_b, requirements)
            st.session_state['result'] = result

    if 'result' in st.session_state:
        res = st.session_state['result']
        
        # 1. Use a clear Status indicator
        if res.get('status') == "FAIL":
            st.error("### ❌ Verification Status: FAIL")
        else:
            st.success("### ✅ Verification Status: PASS")
            
        # 2. PROOF OF LIVE AI: Display the Reasoning
        st.markdown("---")
        st.write("#### 🧠 AI Engine Reasoning:")
        st.info(res.get('reason', 'No reasoning provided.'))
        
        # 3. Optional: Show the specific clash type
        if res.get('status') == "FAIL":
            st.warning(f"**Clash Category:** {res.get('clash_type', 'System Interface')}")

with col2:
    st.header("Context Visualizer")
    status = st.session_state.get('result', {}).get('status', 'NEUTRAL')
    st.plotly_chart(render_cad_model(status, st.session_state.selected_case), use_container_width=True)
