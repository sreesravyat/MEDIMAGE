from skimage.feature import canny
from skimage.segmentation import watershed
from skimage.measure import label, regionprops

def apply_canny_edge_detection(image, sigma):
    """Apply Canny edge detection to the input image."""
    """
    Apply the Canny edge detection algorithm to the input image for edge detection.
    
    Parameters:
    image (numpy array): The input medical image in numpy array format (e.g., using OpenCV).
    threshold1 (int): The lower threshold value for edge linking.
    threshold2 (int): The higher threshold value for edge linking.
    
    Returns:
    numpy array: The edge-detected medical image.
    """
    edges = canny(image, sigma=sigma)
    return edges

def apply_watershed_segmentation(image, markers):
    """Apply watershed segmentation to the input image using markers."""
    """
    Apply the watershed segmentation algorithm to the input image for image segmentation.
    
    Parameters:
    image (numpy array): The input medical image in numpy array format (e.g., using OpenCV).
    
    Returns:
    numpy array: The segmented medical image.
    """
    labels = watershed(image, markers=markers)
    return labels

def extract_regions_of_interest(label_image):
    """Extract regions of interest from the label image."""
    regions = regionprops(label_image)
    return regions
