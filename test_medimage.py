import cv2
import sys
sys.path.append("C:/Users/jagad/OneDrive/Documents/Medimage/medimage_package/examplechestxray.jpg")  # Replace with the actual path to the directory containing medimage_package
from medimage_package.image_utils import load_image, display_image
from medimage_package.image_operations import adjust_contrast, binary_threshold
from medimage_package.image_filtering import apply_gaussian_filter, apply_median_filter
from medimage_package.image_segmentation import apply_canny_edge_detection

# Load an image
image_path = "C:/Users/jagad/OneDrive/Documents/Medimage/medimage_package/examplechestxray.jpg"
loaded_image = load_image(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)

# Apply contrast adjustment
adjusted_image = adjust_contrast(loaded_image, alpha=1.5)

# Apply binary thresholding
thresholded_image = binary_threshold(loaded_image, threshold=128)

# Apply Gaussian filter
gaussian_filtered_image = apply_gaussian_filter(loaded_image, sigma=1.0)

# Apply median filter
median_filtered_image = apply_median_filter(loaded_image, size=3)

# Apply Canny edge detection
canny_edges = apply_canny_edge_detection(gray_image, sigma=1.0)

# Display the images
display_image(loaded_image)
display_image(adjusted_image)
display_image(thresholded_image)
display_image(gaussian_filtered_image)
display_image(median_filtered_image)
display_image(canny_edges)
