# Computer Vision Lab 5 — Edge Detection

This project demonstrates edge detection on a grayscale image using **OpenCV, NumPy, and Matplotlib**.

## Objective

To detect and compare image edges using:

- Sobel Edge Detection
- Prewitt Edge Detection
- Canny Edge Detection

## Libraries Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Python Code

The complete program is available in [cv_lab_5.py](cv_lab_5.py).

## How It Works

The program reads the input image in grayscale and applies three edge detection techniques.

### Sobel

Calculates image gradients in the X and Y directions and combines them to detect edges.

### Prewitt

Uses horizontal and vertical 3×3 kernels to detect changes in image intensity.

### Canny

Detects thin and connected edges using a multi-stage edge detection process.

## How to Run

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

Place your input image in the project folder as:

```text
image2.jpg
```

Run:

```bash
python cv_lab_5.py
```

This version uses a normal local image path. **No Google Colab or Google Drive connection is required.**

## Output

The program displays four images:

1. Original Grayscale Image
2. Sobel Edge Detection
3. Prewitt Edge Detection
4. Canny Edge Detection

### Output Image

![Edge Detection Output](output.png)

## Result

The output demonstrates how Sobel, Prewitt, and Canny methods detect different intensity boundaries and edges in the grayscale image.

## Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
