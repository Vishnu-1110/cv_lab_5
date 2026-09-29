import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display images
def show_comparison(original, sobel, prewitt, canny):
    plt.figure(figsize=(12, 10))

    # Original image
    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # Sobel Edge Detection
    plt.subplot(2, 2, 2)
    plt.imshow(sobel, cmap='gray')
    plt.title('Sobel Edge Detection')
    plt.axis('off')

    # Prewitt Edge Detection
    plt.subplot(2, 2, 3)
    plt.imshow(prewitt, cmap='gray')
    plt.title('Prewitt Edge Detection')
    plt.axis('off')

    # Canny Edge Detection
    plt.subplot(2, 2, 4)
    plt.imshow(canny, cmap='gray')
    plt.title('Canny Edge Detection')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


# Read an image
img = cv2.imread('image2.jpg', 0)

if img is None:
    print("Error: Image not found")
else:
    # Sobel Operator
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)

    # Prewitt Operator
    kernelx = np.array([[1, 1, 1],
                        [0, 0, 0],
                        [-1, -1, -1]])

    kernely = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

    prewittx = cv2.filter2D(img, -1, kernelx)
    prewitty = cv2.filter2D(img, -1, kernely)
    prewitt_combined = prewittx + prewitty

    # Canny Edge Detection
    canny_edges = cv2.Canny(img, 100, 200)

    # Display the results
    show_comparison(
        img,
        np.uint8(np.absolute(sobel_combined)),
        prewitt_combined,
        canny_edges
    )
