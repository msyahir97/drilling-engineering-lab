import math

# ============================================================
# DRILLING ENGINEERING LAB
# Project 01: Well Depth, Hydrostatic Pressure,
# ECD and Pressure Window Calculator
#
# Synthetic training data only.
# Not for operational well design.
# ============================================================


# ------------------------------------------------------------
# 1. WELL INFORMATION
# ------------------------------------------------------------

well_name = "DE-001"


# ------------------------------------------------------------
# 2. WELL GEOMETRY INPUTS
# ------------------------------------------------------------

vertical_md = 1000          # m
inclined_length = 600       # m
inclination = 60            # degrees from vertical


# ------------------------------------------------------------
# 3. DRILLING FLUID INPUTS
# ------------------------------------------------------------

mud_density = 1200          # kg/m3
gravity = 9.81              # m/s2


# ------------------------------------------------------------
# 4. CIRCULATING PRESSURE INPUT
# ------------------------------------------------------------

annular_friction_mpa = 0.75     # MPa

# Convert MPa to Pa
annular_friction_pa = (
    annular_friction_mpa * 1_000_000
)


# ------------------------------------------------------------
# 5. FORMATION PRESSURE LIMITS
# ------------------------------------------------------------

# Synthetic equivalent-density limits

pore_pressure_eq = 1100         # kg/m3
fracture_pressure_eq = 1230     # kg/m3


# ------------------------------------------------------------
# 6. WELL DEPTH CALCULATIONS
# ------------------------------------------------------------

# Total measured depth
total_md = (
    vertical_md
    + inclined_length
)

# Vertical component of the inclined section
inclined_vertical_component = (
    inclined_length
    * math.cos(
        math.radians(inclination)
    )
)

# Total true vertical depth
total_tvd = (
    vertical_md
    + inclined_vertical_component
)


# ------------------------------------------------------------
# 7. STATIC HYDROSTATIC PRESSURE
# ------------------------------------------------------------

hydrostatic_pa = (
    mud_density
    * gravity
    * total_tvd
)

hydrostatic_mpa = (
    hydrostatic_pa
    / 1_000_000
)


# ------------------------------------------------------------
# 8. CIRCULATING BOTTOMHOLE PRESSURE
# ------------------------------------------------------------

circulating_bhp_pa = (
    hydrostatic_pa
    + annular_friction_pa
)

circulating_bhp_mpa = (
    circulating_bhp_pa
    / 1_000_000
)


# ------------------------------------------------------------
# 9. EQUIVALENT CIRCULATING DENSITY
# ------------------------------------------------------------

ecd = (
    circulating_bhp_pa
    / (gravity * total_tvd)
)


# ------------------------------------------------------------
# 10. BASE CASE ENGINEERING REPORT
# ------------------------------------------------------------

print("\n========================================")
print("DRILLING ENGINEERING LAB")
print("========================================")

print(f"Well: {well_name}")

print("\nWELL GEOMETRY")
print("----------------------------------------")

print(
    f"Vertical Section: "
    f"{vertical_md:.2f} m"
)

print(
    f"Inclined Section Length: "
    f"{inclined_length:.2f} m"
)

print(
    f"Inclination: "
    f"{inclination:.2f} degrees"
)

print(
    f"Measured Depth (MD): "
    f"{total_md:.2f} m"
)

print(
    f"True Vertical Depth (TVD): "
    f"{total_tvd:.2f} m"
)


print("\nDRILLING FLUID")
print("----------------------------------------")

print(
    f"Mud Density: "
    f"{mud_density:.2f} kg/m3"
)


print("\nPRESSURE")
print("----------------------------------------")

print(
    f"Static BHP: "
    f"{hydrostatic_mpa:.2f} MPa"
)

print(
    f"Annular Friction Pressure: "
    f"{annular_friction_mpa:.2f} MPa"
)

print(
    f"Circulating BHP: "
    f"{circulating_bhp_mpa:.2f} MPa"
)


print("\nECD")
print("----------------------------------------")

print(
    f"Equivalent Circulating Density: "
    f"{ecd:.2f} kg/m3"
)


# ------------------------------------------------------------
# 11. BASE CASE PRESSURE WINDOW CHECK
# ------------------------------------------------------------

print("\nDRILLING PRESSURE WINDOW")
print("----------------------------------------")

print(
    f"Pore Pressure Equivalent: "
    f"{pore_pressure_eq:.2f} kg/m3"
)

print(
    f"Fracture Pressure Equivalent: "
    f"{fracture_pressure_eq:.2f} kg/m3"
)

print(
    f"Calculated ECD: "
    f"{ecd:.2f} kg/m3"
)


# Calculate pressure-window margins

pore_margin = (
    ecd
    - pore_pressure_eq
)

fracture_margin = (
    fracture_pressure_eq
    - ecd
)


print(
    f"Pore Pressure Margin: "
    f"{pore_margin:.2f} kg/m3"
)

print(
    f"Fracture Pressure Margin: "
    f"{fracture_margin:.2f} kg/m3"
)


# Pressure-window status

if ecd <= pore_pressure_eq:

    print(
        "STATUS: AT/BELOW PORE PRESSURE"
    )

    print(
        "Potential formation influx risk."
    )


elif ecd >= fracture_pressure_eq:

    print(
        "STATUS: AT/ABOVE FRACTURE PRESSURE"
    )

    print(
        "Potential mud losses."
    )


else:

    print(
        "STATUS: WITHIN MODEL PRESSURE WINDOW"
    )

    print(
        "Calculated ECD is between "
        "the specified limits."
    )


# ------------------------------------------------------------
# 12. PRESSURE WINDOW SIMULATOR
# ------------------------------------------------------------

print("\n========================================")
print("PRESSURE WINDOW SIMULATOR")
print("========================================")


# Base operating conditions

scenarios = {
    "PUMPS OFF": 0.00,
    "PUMPS ON": annular_friction_mpa
}


for condition, friction_mpa in scenarios.items():

    friction_pa = (
        friction_mpa
        * 1_000_000
    )

    # Bottomhole pressure
    bhp_pa = (
        hydrostatic_pa
        + friction_pa
    )

    bhp_mpa = (
        bhp_pa
        / 1_000_000
    )

    # Equivalent density
    scenario_ecd = (
        bhp_pa
        / (gravity * total_tvd)
    )

    # Pressure-window margins
    scenario_pore_margin = (
        scenario_ecd
        - pore_pressure_eq
    )

    scenario_fracture_margin = (
        fracture_pressure_eq
        - scenario_ecd
    )


    print(f"\nCondition: {condition}")

    print(
        f"Annular Friction: "
        f"{friction_mpa:.2f} MPa"
    )

    print(
        f"BHP: "
        f"{bhp_mpa:.2f} MPa"
    )

    print(
        f"ECD: "
        f"{scenario_ecd:.2f} kg/m3"
    )

    print(
        f"Pore Pressure Margin: "
        f"{scenario_pore_margin:.2f} kg/m3"
    )

    print(
        f"Fracture Pressure Margin: "
        f"{scenario_fracture_margin:.2f} kg/m3"
    )


    if scenario_ecd <= pore_pressure_eq:

        print(
            "STATUS: AT/BELOW PORE PRESSURE"
        )


    elif scenario_ecd >= fracture_pressure_eq:

        print(
            "STATUS: AT/ABOVE FRACTURE LIMIT"
        )


    else:

        print(
            "STATUS: WITHIN MODEL WINDOW"
        )


# ------------------------------------------------------------
# 13. HIGH-FRICTION SENSITIVITY CASE
# ------------------------------------------------------------

print("\n========================================")
print("HIGH-FRICTION SENSITIVITY CASE")
print("========================================")


high_friction_mpa = 1.00

high_friction_pa = (
    high_friction_mpa
    * 1_000_000
)


high_friction_bhp_pa = (
    hydrostatic_pa
    + high_friction_pa
)

high_friction_bhp_mpa = (
    high_friction_bhp_pa
    / 1_000_000
)


high_friction_ecd = (
    high_friction_bhp_pa
    / (gravity * total_tvd)
)


high_friction_fracture_margin = (
    fracture_pressure_eq
    - high_friction_ecd
)


print(
    f"Annular Friction: "
    f"{high_friction_mpa:.2f} MPa"
)

print(
    f"BHP: "
    f"{high_friction_bhp_mpa:.2f} MPa"
)

print(
    f"ECD: "
    f"{high_friction_ecd:.2f} kg/m3"
)

print(
    f"Fracture Pressure Margin: "
    f"{high_friction_fracture_margin:.2f} kg/m3"
)


if high_friction_ecd >= fracture_pressure_eq:

    print(
        "STATUS: AT/ABOVE FRACTURE LIMIT"
    )

else:

    print(
        "STATUS: BELOW FRACTURE LIMIT"
    )


# ------------------------------------------------------------
# 14. ENGINEERING VALIDATION TESTS
# ------------------------------------------------------------

print("\n========================================")
print("ENGINEERING VALIDATION")
print("========================================")


tolerance = 0.01


# TEST 1
# Pumps OFF:
# ECD should equal actual mud density

ecd_pumps_off = (
    hydrostatic_pa
    / (gravity * total_tvd)
)

assert abs(
    ecd_pumps_off
    - mud_density
) < tolerance

print(
    "TEST 1 PASSED: "
    "Pumps OFF ECD = Mud Density"
)


# TEST 2
# Calculate ECD using two methods

test_friction_pa = (
    annular_friction_mpa
    * 1_000_000
)


# Method 1:
# Mud density + equivalent friction density

ecd_method_1 = (
    mud_density
    + (
        test_friction_pa
        / (gravity * total_tvd)
    )
)


# Method 2:
# Calculate circulating BHP first

test_bhp_pa = (
    hydrostatic_pa
    + test_friction_pa
)

ecd_method_2 = (
    test_bhp_pa
    / (gravity * total_tvd)
)


assert abs(
    ecd_method_1
    - ecd_method_2
) < tolerance

print(
    "TEST 2 PASSED: "
    "Both ECD calculation methods agree"
)


# TEST 3
# Higher annular friction should increase ECD

assert (
    high_friction_ecd
    > ecd_method_1
)

print(
    "TEST 3 PASSED: "
    "Higher friction increases ECD"
)


# TEST 4
# Pumps ON ECD should exceed mud density

assert (
    ecd_method_1
    > mud_density
)

print(
    "TEST 4 PASSED: "
    "Pumps ON ECD > Mud Density"
)


# TEST 5
# Higher ECD should reduce fracture margin

base_fracture_margin = (
    fracture_pressure_eq
    - ecd_method_1
)

assert (
    high_friction_fracture_margin
    < base_fracture_margin
)

print(
    "TEST 5 PASSED: "
    "Higher ECD reduces fracture margin"
)


print("----------------------------------------")
print("ALL VALIDATION TESTS PASSED")
print("========================================")