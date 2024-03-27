import cv2
import os

input_folder = "/home/monotera/Downloads/bg/"
output_folder = "/home/monotera/Downloads/bgb/"
blur_level = 25

# Check if output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get all files in the input folder
image_files = [
    f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))
]

# Filter jpg files
jpg_files = [f for f in image_files if f.lower().endswith(".jpg")]

# Apply blur to each jpg image
for jpg_file in jpg_files:
    input_path = os.path.join(input_folder, jpg_file)
    output_path = os.path.join(output_folder, jpg_file)

    # Apply Gaussian Blur
    try:
        image = cv2.imread(input_path)
        if image is None:
            print(f"Error: Unable to load image '{input_path}'. Skipping...")
            continue
        gaussian_blur = cv2.GaussianBlur(image, (blur_level, blur_level), 0)
    except Exception as e:
        print(f"Error: {e}. Skipping...")
        continue

    # Save the result
    try:
        cv2.imwrite(output_path, gaussian_blur)
        print(
            f"Image '{input_path}' processed and saved successfully at '{output_path}'"
        )
    except Exception as e:
        print(f"Error: {e}. Skipping...")
        continue
