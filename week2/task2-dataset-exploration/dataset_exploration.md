# Task 2 - Medical Imaging Dataset Exploration

## Dataset 1: NIH Chest X-ray14 Dataset

### 1. Type of Imaging Data
The NIH Chest X-ray14 dataset contains chest X-ray images. These are frontal-view radiographs used for detecting thoracic diseases.

### 2. Number of Images
The dataset contains 112,120 chest X-ray images from 30,805 patients.

### 3. Available Classes / Labels
Images can have either "No Finding" or one or more disease labels. The disease labels include:

- Atelectasis
- Cardiomegaly
- Effusion
- Infiltration
- Mass
- Nodule
- Pneumonia
- Pneumothorax
- Consolidation
- Edema
- Emphysema
- Fibrosis
- Pleural Thickening
- Hernia

This is a multi-label dataset, meaning one image can have more than one disease label.

### 4. Dataset Imbalance
The dataset is imbalanced. Some findings such as "No Finding" and common thoracic abnormalities appear much more frequently than rare diseases like Hernia. This can make model training difficult because the model may learn the majority classes better than the minority classes.

### 5. Challenges Observed
- The dataset is multi-label, so one image may contain multiple diseases.
- Some diseases have similar visual patterns in X-rays.
- The labels were generated using NLP from radiology reports, so there can be label noise.
- Class imbalance is a major issue.
- X-ray images can have variation in brightness, contrast, and patient positioning.

### Brief Summary
NIH Chest X-ray14 is a large-scale chest X-ray dataset useful for thoracic disease classification. It is highly relevant for medical computer vision because it contains real-world X-ray images and multiple disease labels. However, the dataset is challenging due to multi-label classification, class imbalance, and possible label noise.


---

## Dataset 2: HAM10000 Skin Lesion Dataset

### 1. Type of Imaging Data
The HAM10000 dataset contains dermatoscopic images of skin lesions. These images are used for skin cancer and skin disease classification.

### 2. Number of Images
The dataset contains 10,015 dermatoscopic images.

### 3. Available Classes / Labels
The dataset has 7 diagnostic classes:

- Melanocytic nevi (NV)
- Melanoma (MEL)
- Benign keratosis-like lesions (BKL)
- Basal cell carcinoma (BCC)
- Actinic keratoses / Bowen’s disease (AKIEC)
- Vascular lesions (VASC)
- Dermatofibroma (DF)

### 4. Dataset Imbalance
The dataset is strongly imbalanced. The NV class has the highest number of images, while DF and VASC have very few images.

Approximate class distribution:

- NV: 6705 images
- MEL: 1113 images
- BKL: 1099 images
- BCC: 514 images
- AKIEC: 327 images
- VASC: 142 images
- DF: 115 images

Because of this imbalance, a model may become biased toward predicting the majority class NV.

### 5. Challenges Observed
- Strong class imbalance.
- Some skin lesion classes look visually similar.
- Images may contain artifacts like hair, shadows, or uneven lighting.
- Lesions can vary in shape, size, color, and texture.
- Minority classes may need augmentation or balancing techniques.

### Brief Summary
HAM10000 is a dermatoscopic skin lesion dataset used for skin disease and skin cancer classification. It is useful for learning medical image classification because it has multiple real-world skin lesion categories. The major challenge is class imbalance, especially because the NV class dominates the dataset while DF and VASC have very few samples.


---

## Overall Learning

Through this task, I understood that medical imaging datasets are different from normal image datasets because they often have class imbalance, noisy labels, visually similar classes, and high clinical importance. Before training any deep learning model, it is important to understand the dataset structure, label distribution, and possible data quality issues.