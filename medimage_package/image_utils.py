import matplotlib.pyplot as plt

def load_image(file_path):
    """Load a medical image from the given file path."""
    """
    Load a medical image from the specified file path.
    
    Parameters:
    file_path (str): The path to the medical image file.
    
    Returns:
    numpy array: The loaded medical image in numpy array format (e.g., using OpenCV).
    """
    image = plt.imread(file_path)
    return image

def display_image(image):
    """Display the given image using matplotlib."""
    """
    Display a medical image using a GUI window or notebook interface.
    
    Parameters:
    image (numpy array): The medical image in numpy array format (e.g., using OpenCV).
    """
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def save_image(image, file_path):
    """Save the image to the specified file path."""
    plt.imsave(file_path, image, cmap='gray')
