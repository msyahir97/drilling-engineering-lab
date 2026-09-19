
import math

# DRILLING ENGINEERING LAB
# Project 01: Well Depth and ECD Calculator
# Synthetic training data only

well_name = "DE-001"

# ---------------------------------
# 1. WELL GEOMETRY
# ---------------------------------

vertical_md = 1000       # m
inclined_length = 600    # m
inclination = 60         # degrees

# ---------------------------------
# 2. DRILLING FLUID
# ---------------------------------

mud_density = 1200       # kg/m3
gravity = 9.81           # m/s2

# ---------------------------------
# 3. CIRCULATING PRESSURE
# ---------------------------------

annular_friction_mpa = 0.75 # MPa

# Convert MPa to Pa
annular_friction_pa = annular_friction_mpa * 1_000_000

# ---------------------------------
# 4. WELL DEPTH CALCULATIONS
# ---------------------------------

total_md = vertical_md + inclined_length

total_tvd = vertical_md + (
    inclined_length * math.cos(
        math.radians(inclination)
    )
)

# ---------------------------------
# 5. STATIC HYDROSTATIC PRESSURE
# ---------------------------------

hydrostatic_pa = mud_density * gravity * total_tvd

hydrostatic_mpa = hydrostatic_pa / 1_000_000

# ---------------------------------
# 6. CIRCULATING BOTTOMHOLE PRESSURE
# ---------------------------------

circulating_bhp_pa = (
    hydrostatic_pa + annular_friction_pa
)

circulating_bhp_mpa = circulating_bhp_pa / 1_000_000

# ---------------------------------
# 7. EQUIVALENT CIRCULATING DENSITY
# ---------------------------------

ecd = mud_density + (
    annular_friction_pa / (gravity * total_tvd)
)

# ---------------------------------
# 8. ENGINEERING REPORT
# ---------------------------------

print("================================")
print("DRILLING ENGINEERING LAB")
print("================================")

print(f"Well: {well_name}")

print("\nWELL GEOMETRY")
print(f"MD: {total_md:.2f} m")
print(f"TVD: {total_tvd:.2f} m")
print(f"Inclination: {inclination} degrees")

print("\nDRILLING FLUID")
print(f"Mud Density: {mud_density} kg/m3")

print("\nPRESSURE")
print(f"Static BHP: {hydrostatic_mpa:.2f} MPa")
print(f"Annular Friction: {annular_friction_mpa:.2f} MPa")
print(f"Circulating BHP: {circulating_bhp_mpa:.2f} MPa")

print("\nECD")
print(f"Equivalent Circulating Density: {ecd:.2f} kg/m3")

print("================================")
