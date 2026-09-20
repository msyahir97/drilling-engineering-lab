
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# DRILLING ENGINEERING LAB
# PROJECT 01 - VISUALISATION 02
# Pore Pressure, Fracture Pressure, Mud Weight and ECD
#
# Synthetic training data only
# Not for operational well design
# ============================================================


# ------------------------------------------------------------
# 1. WELL INPUTS
# ------------------------------------------------------------

well_name = "DE-001"

total_tvd = 1300          # m
mud_density = 1200        # kg/m3

gravity = 9.81            # m/s2

# Friction pressure at total depth
annular_friction_td = 0.75    # MPa


# ------------------------------------------------------------
# 2. CREATE DEPTH POINTS
# ------------------------------------------------------------

# Begin at 100 m because equivalent density
# calculated from P/(g*TVD) is undefined at TVD = 0.

depths = list(range(100, 1301, 25))


# ------------------------------------------------------------
# 3. CREATE SYNTHETIC FORMATION PROFILES
# ------------------------------------------------------------

pore_pressure = []
fracture_pressure = []

mud_weight = []
ecd_profile = []


for tvd in depths:

    # Pore-pressure equivalent:
    # 1000 kg/m3 near datum, increasing
    # to 1100 kg/m3 at 1300 m.

    pp = 1000 + (
        100 / total_tvd
    ) * tvd


    # Fracture-pressure equivalent:
    # 1400 kg/m3 near datum, decreasing
    # to 1230 kg/m3 at 1300 m.

    fg = 1400 - (
        170 / total_tvd
    ) * tvd


    # Simplified annular friction profile
    # Reaches 0.75 MPa at total depth.

    friction_mpa = (
        annular_friction_td
        * (tvd / total_tvd) ** 1.5
    )


    # Convert friction into Pa

    friction_pa = (
        friction_mpa * 1_000_000
    )


    # Hydrostatic pressure

    hydrostatic_pa = (
        mud_density
        * gravity
        * tvd
    )


    # Circulating bottomhole pressure

    bhp_pa = (
        hydrostatic_pa
        + friction_pa
    )


    # Equivalent circulating density

    ecd = (
        bhp_pa
        / (gravity * tvd)
    )


    # Store results

    pore_pressure.append(pp)

    fracture_pressure.append(fg)

    mud_weight.append(mud_density)

    ecd_profile.append(ecd)


# ------------------------------------------------------------
# 4. CREATE THE GRAPH
# ------------------------------------------------------------

fig, ax = plt.subplots(
    figsize=(9, 10)
)


# Pore pressure

ax.plot(
    pore_pressure,
    depths,
    label="Pore Pressure Equivalent",
    linewidth=2
)


# Fracture pressure

ax.plot(
    fracture_pressure,
    depths,
    label="Fracture Pressure Equivalent",
    linewidth=2
)


# Static mud density

ax.plot(
    mud_weight,
    depths,
    label="Mud Density",
    linewidth=2,
    linestyle="--"
)


# Equivalent circulating density

ax.plot(
    ecd_profile,
    depths,
    label="ECD",
    linewidth=2.5
)


# ------------------------------------------------------------
# 5. HIGHLIGHT PRESSURE WINDOW
# ------------------------------------------------------------

ax.fill_betweenx(
    depths,
    pore_pressure,
    fracture_pressure,
    where=[
        pp < fg
        for pp, fg in zip(
            pore_pressure,
            fracture_pressure
        )
    ],
    alpha=0.12,
    label="Model Pressure Window"
)


# ------------------------------------------------------------
# 6. HIGHLIGHT POTENTIAL LOSSES
# ------------------------------------------------------------

losses_zone = [
    ecd >= fg
    for ecd, fg in zip(
        ecd_profile,
        fracture_pressure
    )
]


ax.scatter(
    [
        ecd_profile[i]
        for i in range(len(depths))
        if losses_zone[i]
    ],
    [
        depths[i]
        for i in range(len(depths))
        if losses_zone[i]
    ],
    marker="x",
    label="At/Above Fracture Limit"
)


# ------------------------------------------------------------
# 7. GRAPH FORMATTING
# ------------------------------------------------------------

ax.invert_yaxis()

ax.set_xlabel(
    "Equivalent Density (kg/m3)"
)

ax.set_ylabel(
    "True Vertical Depth (m)"
)

ax.set_title(
    f"{well_name} - Drilling Pressure Window"
)

ax.grid(
    True,
    alpha=0.3
)

ax.legend(
    loc="upper right"
)


# ------------------------------------------------------------
# 8. SAVE FIGURE
# ------------------------------------------------------------

output_folder = (
    Path(__file__).resolve().parent
    / "plots"
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder
    / "pressure_window.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 9. ENGINEERING REPORT
# ------------------------------------------------------------

print("================================")
print("DRILLING ENGINEERING LAB")
print("================================")

print(f"Well: {well_name}")

print(
    f"Total TVD: {total_tvd} m"
)

print(
    f"Mud Density: {mud_density} kg/m3"
)

print(
    f"ECD at TD: {ecd_profile[-1]:.2f} kg/m3"
)

print(
    f"Pore Pressure Eq. at TD: "
    f"{pore_pressure[-1]:.2f} kg/m3"
)

print(
    f"Fracture Pressure Eq. at TD: "
    f"{fracture_pressure[-1]:.2f} kg/m3"
)


fracture_margin = (
    fracture_pressure[-1]
    - ecd_profile[-1]
)

print(
    f"Fracture Margin at TD: "
    f"{fracture_margin:.2f} kg/m3"
)


# ------------------------------------------------------------
# 10. BASIC VALIDATION
# ------------------------------------------------------------

assert abs(
    ecd_profile[-1] - 1258.81
) < 0.02

assert pore_pressure[-1] == 1100

assert fracture_pressure[-1] == 1230

print("VALIDATION: PASSED")

print(
    f"Plot saved to: {output_file}"
)

print("================================")


# ------------------------------------------------------------
# 11. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()
