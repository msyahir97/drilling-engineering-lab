
import math

# Drilling Engineering Lab
# Project 01: Well Depth Calculator

well_name = "DE-001"

vertical_md = 1000
inclined_length = 600
inclination = 30

total_md = vertical_md + inclined_length

total_tvd = vertical_md + (
    inclined_length * math.cos(math.radians(inclination))
)

print(f"Well Name: {well_name}")
print(f"Measured Depth: {total_md:.2f} m")
print(f"True Vertical Depth: {total_tvd:.2f} m")
