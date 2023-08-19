"# MEDIMAGE" 
# MediImage - Medical Image Processing Package

## Goals
The "MediImage" package aims to provide intermediate-level medical image processing functionalities for Python users. It includes a variety of image processing techniques, such as filtering, edge detection, and image segmentation, commonly used in the medical field.

## Organization
The package is organized into the following modules:

1. `image_operations.py`: Contains functions for basic image processing operations on medical images, such as contrast adjustment and binary thresholding.

2. `image_utils.py`: Contains utility functions for loading and displaying medical images.

3. `image_filtering.py`: Contains functions for advanced image filtering techniques like Gaussian filtering and median filtering.

4. `image_segmentation.py`: Contains functions for image segmentation techniques like Canny edge detection and watershed segmentation.

## Examples of Intermediate-Level Use in the Medical Field

```python
# Import the MediImage package and its modules
import MediImage.image_operations as img_ops
import MediImage.image_utils as img_utils
import MediImage.image_filtering as img_filter
import MediImage.image_segmentation as img_segment

# Load and display a medical image
image = img_utils.load_image('path_to_medical_image.jpg')
img_utils.display_image(image)

# Apply Gaussian filtering to the image
filtered_image_gaussian = img_filter.apply_gaussian_filter(image, sigma=1.5)
img_utils.display_image(filtered_image_gaussian)

# Apply median filtering to the image
filtered_image_median = img_filter.apply_median_filter(image, kernel_size=3)
img_utils.display_image(filtered_image_median)

# Apply Canny edge detection to the image
edges_canny = img_segment.apply_canny_edge_detection(image, threshold1=100, threshold2=200)
img_utils.display_image(edges_canny)

# Apply watershed segmentation to the image
segmented_image = img_segment.apply_watershed_segmentation(image)
img_utils.display_image(segmented_image)
