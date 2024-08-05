import numpy as np

x_res_px = 1280
baseline_mm = 50
hfov = 90

focal_length_px = 0.5 * (x_res_px / np.tan(np.radians(hfov / 2)))

for disparity_shift in range(0, 126):
	min_z_mm = (focal_length_px * baseline_mm) / (disparity_shift + 126)
	max_z_mm = (focal_length_px * baseline_mm) / disparity_shift
	print(f"disparity_shift {disparity_shift}, min_z-max_z (mm) {min_z_mm} - {max_z_mm}")