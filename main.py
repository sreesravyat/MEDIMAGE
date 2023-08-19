from medimage.image_utils import load_image, display_image
from medimage.image_operations import adjust_contrast, binary_threshold
from medimage.image_filtering import apply_gaussian_filter, apply_median_filter
from medimage.image_segmentation import apply_canny_edge_detection

# Load an image
image_path = 'path_to_your_image.jpg'
loaded_image = load_image(image_path)

# Apply contrast adjustment
adjusted_image = adjust_contrast(loaded_image, alpha=1.5)

# Apply binary thresholding
thresholded_image = binary_threshold(loaded_image, threshold=128)

# Apply Gaussian filter
gaussian_filtered_image = apply_gaussian_filter(loaded_image, sigma=1.0)

# Apply median filter
median_filtered_image = apply_median_filter(loaded_image, size=3)

# Apply Canny edge detection
canny_edges = apply_canny_edge_detection(loaded_image, sigma=1.0)

# Display the images
display_image(loaded_image)
display_image(adjusted_image)
display_image(thresholded_image)
display_image(gaussian_filtered_image)
display_image(median_filtered_image)
display_image(canny_edges)
