# Digital Image Processing

A collection of Python examples covering common digital image processing operations, filters, image analysis techniques, and basic image steganography.

## Requirements

- Python 3
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- SortedContainers

Install the dependencies with:

```bash
pip install opencv-python numpy matplotlib sortedcontainers
```

## Running the Examples

Run each script from the project root because the scripts use relative image paths:

```bash
python 1_threshold.py
```

The scripts open image or plot windows when executed. Press `Ctrl+C` or close the plot window to stop a script.

## Examples

| Script | Description | Input image |
|---|---|---|
| `1_threshold.py` | Applies thresholding to a grayscale image | `1_threashold.png` |
| `2_clipping.py` | Clips pixel intensity values to a selected range | `2_clipping.png` |
| `3_negative.py` | Produces the negative of an image | `3_negative.jpg` |
| `4_contrast_stretching.py` | Stretches contrast across the available intensity range | `4_contrast_stretching.jpg` |
| `5_bit_plane_slicing.py` | Displays the bit-plane representation of an image | `5_bit_plane_slicing.jpg` |
| `6_histogram_equalization.py` | Equalizes the image histogram to improve contrast | `6_histogram_equalization.jpg` |
| `7_histogram_matching.py` | Matches an image histogram to a target distribution | `7_histogram_matching.jpg` |
| `8_smoothing_filter.py` | Applies smoothing by spatial filtering | `8_smoothing_filter.jpg` |
| `9_black_and_white.py` | Converts an image to a binary black-and-white result | `9_black_and_white.jpg` |
| `10_assignment.py` | Identifies connected components and joins nearby components | `10_assignment.png` |
| `11_sharpning_filter.py` | Applies a spatial sharpening filter | `11_sharpning_filter.jpg` |
| `12_angle.py` | Computes Sobel gradient angles for a small sample matrix | `12_angle.py` |
| `13_Hough_Tranform.py` | Detects line segments using the probabilistic Hough transform | `13_Hough_Transform.png` |

## Image Steganography

The steganography scripts use the least significant bit of each grayscale pixel.

1. Place or update the carrier image as `encrypt_img.jpg`.
2. Encrypt a message:

   ```bash
   python encrypt.py
   ```

3. Enter the secret message when prompted. The output is saved as `secret.png`.
4. Extract the message:

   ```bash
   python decrypt.py
   ```

## Project Files

- Python examples are in the project root.
- `Originals/` contains source images used for selected operations.
- Output images and screenshots are stored in the project root alongside their corresponding scripts.
