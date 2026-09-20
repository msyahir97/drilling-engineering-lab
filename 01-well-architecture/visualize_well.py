import math
import os
import matplotlib.pyplot as plt


# ============================================================
# DRILLING ENGINEERING LAB
# 2D Well Trajectory Visualisation
# Synthetic training data only
# ============================================================


# ------------------------------------------------------------
# WELL INPUTS
# ------------------------------------------------------------

vertical_md = 1000          # m
inclined_length = 600       # m
inclination = 60            # degrees from vertical


# ------------------------------------------------------------
# TRAJECTORY CALCULATIONS
# ------------------------------------------------------------

angle_rad = math.radians(inclination)

# Vertical component of inclined section
vertical_component = (
    inclined_length
    * math.cos(angle_rad)
)

# Horizontal displacement
horizontal_displacement = (
    inclined_length
    * math.sin(angle_rad)
)

# Final TVD
final_tvd = (
    vertical_md
    + vertical_component
)

# Final MD
final_md = (
    vertical_md
    + inclined_length
)


# ------------------------------------------------------------
# DEFINE WELL TRAJECTORY POINTS
# ------------------------------------------------------------

# Starting point
x_start = 0
tvd_start = 0

# Kick-off point
x_kop = 0
tvd_kop = vertical_md

# Total depth
x_td = horizontal_displacement
tvd_td = final_tvd


x = [
    x_start,
    x_kop,
    x_td
]

tvd = [
    tvd_start,
    tvd_kop,
    tvd_td
]


# ------------------------------------------------------------
# CREATE PLOT
# ------------------------------------------------------------

plt.figure(figsize=(7, 8))

plt.plot(
    x,
    tvd,
    marker="o",
    linewidth=3
)

# Depth increases downward
plt.gca().invert_yaxis()

plt.xlabel("Horizontal Displacement (m)")
plt.ylabel("True Vertical Depth (m)")

plt.title(
    "DE-001 Simplified Well Trajectory"
)

plt.grid(True)

plt.gca().set_aspect("equal", adjustable="box")

# ------------------------------------------------------------
# LABEL IMPORTANT POINTS
# ------------------------------------------------------------

plt.annotate(
    "Surface",
    (x_start, tvd_start),
    xytext=(10, 10),
    textcoords="offset points"
)

plt.annotate(
    "Kick-Off Point\nMD = 1000 m",
    (x_kop, tvd_kop),
    xytext=(-15, 15),
    textcoords="offset points",
    ha="right"
)

plt.annotate(
    f"TD\n"
    f"MD = {final_md:.0f} m\n"
    f"TVD = {final_tvd:.0f} m",
    (x_td, tvd_td),
    xytext=(-15, -5),
    textcoords="offset points",
    ha="right"
)


# ------------------------------------------------------------
# SAVE IMAGE
# ------------------------------------------------------------

output_folder = (
    "01-well-architecture/plots"
)

os.makedirs(
    output_folder,
    exist_ok=True
)

output_file = (
    f"{output_folder}/"
    "well_trajectory_2d.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print(
    f"Plot saved to: {output_file}"
)


# ------------------------------------------------------------
# DISPLAY PLOT
# ------------------------------------------------------------

plt.show()