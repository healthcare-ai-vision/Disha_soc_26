import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def add_gaussian_noise(image, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)


def process_image(image_path):
    image_name = image_path.stem

    image = cv2.imread(str(image_path))

    if image is None:
        print(f"Could not read {image_path}")
        return

    # OpenCV reads image in BGR format
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. Grayscale conversion
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Histogram visualization
    plt.figure(figsize=(6, 4))
    plt.hist(gray_image.ravel(), bins=256, range=(0, 256))
    plt.title(f"Histogram - {image_name}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig(OUTPUT_DIR / f"{image_name}_histogram.png")
    plt.close()

    # 3. Image resizing
    resized_image = cv2.resize(rgb_image, (224, 224))

    # 4. Edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # 5. Noise addition
    noisy_image = add_gaussian_noise(gray_image)

    # 6. Noise removal using Gaussian filter
    denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

    # Save separate outputs
    cv2.imwrite(str(OUTPUT_DIR / f"{image_name}_grayscale.png"), gray_image)
    cv2.imwrite(str(OUTPUT_DIR / f"{image_name}_edges.png"), edges)
    cv2.imwrite(str(OUTPUT_DIR / f"{image_name}_noisy.png"), noisy_image)
    cv2.imwrite(str(OUTPUT_DIR / f"{image_name}_denoised.png"), denoised_image)

    # Save one combined comparison image
    plt.figure(figsize=(14, 8))

    images = [
        (rgb_image, "Original"),
        (gray_image, "Grayscale"),
        (resized_image, "Resized 224x224"),
        (edges, "Edge Detection"),
        (noisy_image, "Gaussian Noise Added"),
        (denoised_image, "Gaussian Filter Denoising"),
    ]

    for i, (img, title) in enumerate(images):
        plt.subplot(2, 3, i + 1)

        if len(img.shape) == 2:
            plt.imshow(img, cmap="gray")
        else:
            plt.imshow(img)

        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{image_name}_comparison.png")
    plt.close()

    print(f"Processed {image_path.name}")


image_files = list(IMAGE_DIR.glob("*.jpg")) + list(IMAGE_DIR.glob("*.png")) + list(IMAGE_DIR.glob("*.jpeg"))

if len(image_files) < 2:
    print("Please add at least two images inside the images folder.")
else:
    for image_path in image_files[:2]:
        process_image(image_path)

    print("Done. Check the outputs folder.")