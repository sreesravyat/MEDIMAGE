from scipy.ndimage import gaussian_filter, median_filter

def apply_gaussian_filter(image, sigma):
    """Apply Gaussian filtering to the input image."""
    """
    Apply a Gaussian filter to the input image for noise reduction.
    
    Parameters:
    image (numpy array): The input medical image in numpy array format (e.g., using OpenCV).
    sigma (float): The standard deviation of the Gaussian kernel.
    
    Returns:
    numpy array: The filtered medical image.
    """
    return gaussian_filter(image, sigma=sigma)

def apply_median_filter(image, size):
    """Apply median filtering to the input image."""
    """
    Apply a median filter to the input image for noise reduction.
    
    Parameters:
    image (numpy array): The input medical image in numpy array format (e.g., using OpenCV).
    kernel_size (int): The size of the median filter kernel. Must be odd.
    
    Returns:
    numpy array: The filtered medical image.
    """
    return median_filter(image, size=size)
