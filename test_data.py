import json

TEST_CASES = {
    "1. Thermal Trap": {
        "requirements": "Core temp <65°C, Efficiency >92%, IP67 sealing. Max Ambient 45°C.",
        "data_a": json.dumps({
            "enclosure_type": "sealed_IP67", "ambient_temp_max_c": 45, "internal_volume_cc": 1200, "surface_area_sq_cm": 450,
            "thermal_conductivity_w_mk": 0.2, "material_emissivity": 0.85, "airflow_cfm": 0, "altitude_rating_m": 2000,
            "humidity_max_percent": 95, "vibration_tolerance_g": 5, "shock_rating_g": 20, "material_uv_resistance": "high",
            "wall_thickness_mm": 3.5, "seal_material": "silicone", "fastener_torque_nm": 4, "mounting_type": "vertical",
            "paint_finish": "powder_coat", "ingress_protection_rating": "IP67", "thermal_expansion_coefficient": 23, "cost_per_unit_usd": 125
        }),
        "data_b": json.dumps({
            "component": "high_torque_motor_driver", "heat_dissipation_w": 35, "operating_efficiency_percent": 91.5, "max_operating_temp_c": 65,
            "current_draw_a": 12.5, "startup_surge_w": 80, "switching_frequency_khz": 20, "standby_power_w": 2, "power_factor": 0.98,
            "thermal_expansion_coefficient": 15, "mtbf_hours": 45000, "voltage_input_v": 24, "output_torque_nm": 4.5, "communication_protocol": "CANOpen",
            "pcb_layer_count": 6, "component_count": 142, "rohs_compliant": True, "weight_g": 450, "dimensions_mm": "120x80x40", "expected_lifecycle_years": 10
        }),
        "file_path": "data/enclosure_model.step"
    },
    "2. Kinematic Pinch": {
        "requirements": "Harness must handle 10k cycles at 30° rotation, maintain >100M-ohm insulation, and stay within IP67 routing constraints.",
        "data_a": json.dumps({
            "joint_type": "articulating", "max_rotation_deg": 30, "routing_channel_width_mm": 20, "routing_radius_mm": 12,
            "surface_roughness_microns": 3.2, "lubrication_type": "dry_ptfe", "joint_friction_coefficient": 0.15, "protection_rating": "IP67",
            "material_hardness_hb": 150, "cycle_test_velocity_deg_s": 5, "actuator_type": "servo_electric", "max_load_capacity_kg": 50,
            "bearing_type": "ball_thrust", "clearance_tolerance_mm": 0.05, "housing_material": "AISI_304", "seal_friction_n": 2,
            "thermal_drift_mm": 0.1, "maintenance_interval_hours": 5000, "sensor_feedback_rate_hz": 100, "total_weight_kg": 12
        }),
        "data_b": json.dumps({
            "cable_type": "shielded_power_heavy_duty", "outer_diameter_mm": 14, "min_bend_radius_mm": 48, "insulation_class": "Polyurethane",
            "shielding_material": "Braided_Copper", "expected_flex_life_cycles": 15000, "insulation_resistance_mohm": 120, "conductor_awg": 10,
            "voltage_rating_v": 600, "weight_per_m_g": 250, "flame_retardant_rating": "UL94-V0", "temp_rating_c": 105, "shield_coverage_percent": 95,
            "jacket_thickness_mm": 1.2, "strand_count": 72, "max_current_a": 30, "halogen_free": True, "bend_radius_static_mm": 24,
            "oil_resistance": "high", "flex_speed_max_m_s": 2
        }),
        "file_path": "data/boom.step"
    },
    "3. Pressure Burst": {
        "requirements": "System must withstand 5000 PSI surge, 1.5x safety factor.",
        "data_a": json.dumps({
            "housing_material": "Steel_4140", "yield_strength_psi": 60000, "wall_thickness_mm": 8, "internal_diameter_mm": 25,
            "burst_safety_factor": 2.0, "sealing_method": "O-ring_nitrile", "surface_finish_ra": 0.8, "corrosion_resistance_level": "high",
            "assembly_torque_nm": 35, "weight_g": 1200, "max_pressure_rating_psi": 8000, "bolt_pattern": "M8_4x", "gasket_type": "viton",
            "fluid_type": "hydraulic_oil", "operating_pressure_psi": 3000, "test_pressure_psi": 6000, "fatigue_limit_cycles": 2e6,
            "tensile_strength_mpa": 450, "elongation_percent": 15, "hardness_brinell": 210
        }),
        "data_b": json.dumps({
            "component": "hydraulic_valve", "max_working_pressure_psi": 3000, "peak_surge_pressure_psi": 5000, "port_size_in": 0.5,
            "fluid_compatibility": "mineral_oil", "response_time_ms": 30, "leakage_rate_ml_min": 0.05, "operating_temp_range_c": "-20_to_80",
            "coil_voltage_v": 24, "iso_fluid_class": "18_16_13", "solenoid_type": "latching", "max_cycle_rate_cpm": 60, "seal_life_cycles": 1e6,
            "body_material": "stainless_steel", "actuation_force_n": 10, "power_consumption_w": 12, "ip_rating": "IP67",
            "weight_kg": 0.5, "certification": "CE", "mtbf_years": 10
        }),
        "file_path": "data/valve_assembly.step"
    },
    "4. Signal Crosstalk": {
        "requirements": "High-speed LVDS pairs must be isolated from PWM power traces by at least 5mm.",
        "data_a": json.dumps({
            "pcb_layer_stack": "4_layer_fr4", "pwm_trace_width_mm": 1.5, "pwm_frequency_khz": 100, "signal_trace_spacing_mm": 1,
            "ground_plane_integrity": "solid", "via_spacing_mm": 10, "trace_impedance_ohm": 50, "shielding_type": "none",
            "crosstalk_db_limit": -60, "crosstalk_actual_db": -30, "layer_separation_mm": 0.2, "dielectric_constant": 4.5,
            "surface_finish": "ENIG", "trace_copper_weight_oz": 1, "soldermask_thickness_um": 20, "emi_filter_type": "ferrite",
            "connector_type": "usb_c", "cable_length_m": 1.5, "baud_rate_mbps": 480, "voltage_swing_v": 0.8
        }),
        "data_b": json.dumps({
            "lvds_pair_width_mm": 0.15, "differential_impedance_ohm": 100, "skew_limit_ps": 10, "max_data_rate_gbps": 5,
            "transmitter_type": "high_speed_serdes", "receiver_sensitivity_mv": 150, "common_mode_range_v": 1.2,
            "esd_protection_rating_kv": 8, "operating_voltage_v": 3.3, "jitter_tolerance_ps": 50, "power_per_lane_mw": 50,
            "trace_length_matching_mm": 0.05, "via_count": 2, "crosstalk_immunity_level": "high", "thermal_rating_c": 125,
            "connector_pins": 24, "shielding_effectiveness_db": 30, "rohs_status": "compliant", "weight_g": 5, "manufacturing_process": "smt"
        }),
        "file_path": "data/control_board.step"
    },
    "5. Vibration Resonance": {
        "requirements": "System natural frequency must be outside the 100-150Hz operating range.",
        "data_a": json.dumps({
            "structure_material": "Aluminum_6061", "stiffness_n_m": 8e5, "damping_ratio": 0.05, "mass_kg": 8,
            "natural_freq_hz": 175, "operating_range_min_hz": 100, "operating_range_max_hz": 150, "mounting_points": 4,
            "bolt_torque_nm": 25, "acceleration_g": 5, "fatigue_life_cycles": 1e7, "weld_type": "tig", "wall_thickness_mm": 8,
            "surface_treatment": "anodized", "safety_factor": 2.5, "thermal_expansion_hz_offset": 5, "geometry_factor": 1.1,
            "base_plate_thickness_mm": 12, "bolt_grade": "10.9", "total_height_mm": 250
        }),
        "data_b": json.dumps({
            "motor_rpm": 7200, "unbalance_g_mm": 2, "blade_count": 3, "frequency_source_hz": 120, "dynamic_load_n": 300,
            "bearing_rating_life": 10000, "motor_power_w": 500, "voltage_v": 230, "current_a": 2.5, "efficiency_percent": 90,
            "insulation_class": "F", "enclosure_type": "IP55", "weight_kg": 4, "shaft_diameter_mm": 20, "bearing_type": "deep_groove",
            "lubrication": "grease", "max_temp_rise_c": 30, "coolant": "air", "shaft_material": "carbon_steel", "noise_level_db": 60
        }),
        "file_path": "data/mounting_bracket.step"
    },
    "6. Material Fatigue": {
        "requirements": "Component must survive 1 million cycles at peak load without cracking.",
        "data_a": json.dumps({
            "material": "ABS_plastic", "yield_strength_mpa": 40, "fatigue_strength_mpa": 5, "load_type": "tension",
            "cycle_count_requested": 1000000, "service_environment": "humid", "stress_concentration_factor": 3.0,
            "peak_load_n": 800, "cross_section_area_mm2": 50, "surface_finish": "molded", "uv_exposure": "none",
            "temp_range_c": "0_to_40", "moisture_absorption_percent": 0.5, "creep_resistance": "low", "thermal_conductivity": 0.2,
            "density_g_cc": 1.05, "recyclability": "high", "weld_line_strength": 0.5, "impact_strength_kj_m2": 10, "cost": 0.2
        }),
        "data_b": json.dumps({
            "load_frequency_hz": 10, "duty_cycle_percent": 50, "peak_strain_percent": 5, "max_load_n": 900,
            "loading_condition": "cyclic", "operating_hours_per_day": 12, "total_days_required": 365, "safety_factor": 1.1,
            "test_standard": "ASTM_D638", "clamping_force_n": 100, "vibration_amp_mm": 0.5, "shock_load_n": 1000,
            "holding_time_s": 0.5, "reset_time_s": 0.1, "max_stroke_mm": 50, "stroke_rate_min": 60, "dwell_time_s": 2,
            "accel_max_g": 8, "stop_pos_tolerance_mm": 0.5, "operational_mode": "continuous"
        }),
        "file_path": "data/plastic_link.step"
    },
    "7. High-Speed Data Sync": {
        "requirements": "Parallel bus must maintain timing skew < 100ps.",
        "data_a": json.dumps({
            "bus_type": "parallel_cmos", "trace_length_mm": 200, "propagation_delay_ps_mm": 10, "clock_freq_mhz": 200,
            "setup_time_req_ps": 500, "hold_time_req_ps": 500, "driver_type": "push_pull", "load_capacitance_pf": 20,
            "terminating_resistor_ohm": 33, "supply_voltage_v": 3.3, "rise_time_ps": 1200, "fall_time_ps": 1200,
            "jitter_max_ps": 200, "crosstalk_coupling_pf": 5, "ground_bounce_mv": 200, "trace_impedance_ohm": 50,
            "via_count": 8, "board_material": "fr4", "layer_count": 4, "emi_shielding": "none"
        }),
        "data_b": json.dumps({
            "processor_type": "fpga", "clk_to_out_max_ps": 800, "clk_to_out_min_ps": 100, "skew_allowance_ps": 300,
            "setup_time_provided_ps": 400, "hold_time_provided_ps": 400, "v_ih_min": 2.0, "v_il_max": 0.8,
            "i_source_ma": 8, "i_sink_ma": 8, "package_type": "bga", "thermal_pad_present": True, "junction_temp_c": 85,
            "power_draw_w": 2.5, "pin_count": 256, "interface_standard": "lvcmos33", "output_drive_strength": "12ma",
            "tristate_mode": True, "enable_time_ns": 5, "disable_time_ns": 5
        }),
        "file_path": "data/fpga_module.step"
    },
    "8. Battery Discharge": {
        "requirements": "Battery must support 20A peak load for 30 seconds without thermal runaway.",
        "data_a": json.dumps({
            "cell_chemistry": "li_ion", "capacity_ah": 5, "c_rate_max_continuous": 1, "c_rate_max_burst": 2,
            "internal_resistance_mohm": 100, "max_temp_runaway_c": 100, "nominal_voltage_v": 3.7, "max_voltage_v": 4.2,
            "cycle_life_80": 300, "operating_temp_c": "0_to_45", "weight_g": 100, "dimensions_mm": "18x65",
            "max_discharge_current_a": 5, "peak_discharge_current_a": 10, "overcurrent_protection_a": 12,
            "thermal_cutoff_c": 60, "ventilation_req": "forced", "casing_material": "steel", "charge_time_hours": 3, "rohs": True
        }),
        "data_b": json.dumps({
            "load_profile": "peak_discharge", "load_current_a": 20, "load_duration_s": 45, "duty_cycle_percent": 10,
            "cutoff_voltage_v": 3.0, "power_bus_impedance_mohm": 20, "thermal_management_type": "passive_heatsink",
            "heat_dissipation_coeff": 0.01, "ambient_temp_c": 40, "safety_margin_percent": 5, "wire_gauge_awg": 18,
            "connection_resistance_mohm": 10, "mosfet_on_resistance_mohm": 20, "protection_ic_latency_ms": 50,
            "monitoring_freq_hz": 10, "surge_suppression": "none", "connector_type": "xt60", "max_temp_rise_c": 60,
            "expected_mtbf_hours": 10000, "storage_mode": "balance"
        }),
        "file_path": "data/battery_pack.step"
    },
    "9. Cable Tension": {
        "requirements": "Suspension cable must support 2000N static load with a factor of safety of 3.",
        "data_a": json.dumps({
            "material": "nylon_rope", "yield_strength_mpa": 50, "diameter_mm": 5, "min_breaking_load_n": 1000,
            "elongation_at_break_percent": 30, "elastic_modulus_gpa": 3, "surface_treatment": "none",
            "weight_per_m_g": 50, "bend_radius_min_mm": 10, "temp_coefficient": 100e-6, "service_life_years": 2,
            "uv_resistance": "low", "corrosion_resistance": "n/a", "max_static_load_n": 500, "safety_factor": 1.2,
            "clamp_type": "knot", "termination_efficiency_percent": 40, "friction_coeff": 0.5, "dampening_freq_hz": 5,
            "vibration_tolerance": "low"
        }),
        "data_b": json.dumps({
            "load_type": "static", "applied_load_n": 2200, "dynamic_load_factor": 1.5, "temp_c": 25,
            "vibration_amp_mm": 2.0, "wind_load_n": 500, "snow_load_n": 500, "acceleration_g": 0.5,
            "mounting_angle_deg": 45, "anchor_depth_mm": 50, "anchor_type": "plastic_plug", "installation_torque_nm": 5,
            "environment": "outdoor_coastal", "salinity_level": "high", "inspect_interval_months": 1, "max_deflection_mm": 50,
            "safety_margin_target_n": 6000, "base_material": "drywall", "concrete_strength_mpa": 10, "installation_certified": False
        }),
        "file_path": "data/cable_suspension.step"
    },
    "10. High-Speed Fluid Flow ": {
        "requirements": "Pipe must prevent cavitation at flow rates up to 50 L/min.",
        "data_a": json.dumps({
            "pipe_material": "steel_schedule_80", "inner_diameter_mm": 35, "wall_thickness_mm": 4.5, "max_pressure_psi": 1000,
            "roughness_mm": 0.045, "thermal_expansion": 0.012, "uv_stability": "high", "impact_resistance": "high",
            "cost": 15.0, "length_m": 5, "connection_type": "welded", "solvent_type": "n/a", "max_flow_rate_lmin": 100,
            "cavitation_limit_m_s": 5.0, "bend_radius_min_mm": 150, "weight_g_m": 2000, "fire_rating": "non_flammable",
            "density_g_cc": 7.85, "temp_max_c": 300, "transparency": "opaque"
        }),
        "data_b": json.dumps({
            "fluid_type": "water", "flow_rate_lmin": 50, "viscosity_cp": 1.0, "density_kg_m3": 1000, "inlet_pressure_bar": 5,
            "outlet_pressure_bar": 4.5, "temp_c": 20, "turbulence_level": "low", "pipe_velocity_m_s": 0.8,
            "system_type": "pump_discharge", "valve_count": 1, "elbow_count": 1, "fittings_type": "welded",
            "seal_integrity_psi": 500, "operating_hours_per_day": 8, "maintenance_required": False, "pressure_drop_bar": 0.5,
            "cavitation_expected": False, "flow_stability": "high", "noise_level_db": 40, "sensor_read_hz": 100
        }),
        "file_path": "data/piping_assembly.step"
    }
}
