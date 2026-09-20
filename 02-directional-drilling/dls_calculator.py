import math

# ==========================================
# PROJECT 02: BUILD RATE & DLS CALCULATOR
# Fictional directional well: DE-002
# ==========================================

# Survey 1
md1 = 1200.0
inc1 = 40.0
azi1 = 80.0

# Survey 2
md2 = 1290.0
inc2 = 46.0
azi2 = 95.0

# STEP 1: Calculate MD interval
delta_md = md2 - md1

if delta_md <= 0:
    raise ValueError("Survey 2 MD must be greater than Survey 1 MD.")

# STEP 2: Calculate Build Rate (degrees per 30 m)
build_rate = (inc2 - inc1) / delta_md * 30

# STEP 3: Convert degrees into radians for Python
i1 = math.radians(inc1)
i2 = math.radians(inc2)
a1 = math.radians(azi1)
a2 = math.radians(azi2)

# STEP 4: Calculate the cosine of the dogleg angle
cos_beta = (
    math.cos(i1) * math.cos(i2)
    + math.sin(i1) * math.sin(i2) * math.cos(a2 - a1)
)

# Keep the number within the valid range for acos()
cos_beta = max(-1.0, min(1.0, cos_beta))

# STEP 5: Calculate dogleg angle
beta_rad = math.acos(cos_beta)
beta_deg = math.degrees(beta_rad)

# STEP 6: Calculate DLS (degrees per 30 m)
dls = beta_deg / delta_md * 30


# STEP 7: Check results against our DE-002 reference calculation
assert abs(build_rate - 2.00) < 0.01
assert abs(beta_deg - 11.83) < 0.02
assert abs(dls - 3.94) < 0.02

print("Validation: PASSED (DE-002 reference case)")


# DISPLAY RESULTS
print("=== DE-002 DIRECTIONAL SURVEY ===")
print(f"MD interval: {delta_md:.2f} m")
print(f"Inclination change: {inc2 - inc1:.2f} degrees")
print(f"Azimuth change: {azi2 - azi1:.2f} degrees")

print("\n=== RESULTS ===")
print(f"Build Rate: {build_rate:.2f} deg/30 m")
print(f"Dogleg Angle: {beta_deg:.2f} degrees")
print(f"Dogleg Severity: {dls:.2f} deg/30 m")
