import numpy as np

def adjust_contrast(image, alpha):
    """Adjust the contrast of the input image."""
    """
    Apply contrast adjustment to the input image.
    
    Parameters:
    image (numpy array): The input image in numpy array format (e.g., from OpenCV).
    factor (float): The contrast adjustment factor. A value greater than 1 increases contrast, while a value less than 1 decreases contrast.
    
    Returns:
    numpy array: The contrast-adjusted image.
    """
    return alpha * image

def binary_threshold(image, threshold):
    """Apply binary thresholding to the input image."""
    """
    Apply binary thresholding to the input image.
    
    Parameters:
    image (numpy array): The input image in numpy array format (e.g., from OpenCV).
    threshold_value (int): The threshold value. Pixel intensities greater than this value will be set to 255 (white), and pixel intensities less than or equal to this value will be set to 0 (black).
    
    Returns:
    numpy array: The thresholded image.
    """
    return (image > threshold).astype(np.uint8) * 255
