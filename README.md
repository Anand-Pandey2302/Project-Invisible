# Project-Invisible

# 🧙 Invisible Cloak using OpenCV

## 📌 Project Description

**Invisible Cloak** is a computer vision project built using **Python and OpenCV** that creates an invisibility effect in real time. The project captures the background before starting the main process and then detects a specific **red-colored cloak** using HSV color segmentation.

When the red cloak is detected, that portion of the live video is replaced with the previously captured background, creating an **invisible cloak effect**. The project demonstrates the practical use of **image processing, color detection, masking, and real-time video processing**.

## 🚀 Features

* Real-time camera-based invisibility effect
* Red color detection using HSV color space
* Background frame capturing
* Noise removal using morphological operations
* Image masking and background replacement
* Live video processing using OpenCV

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* HSV Color Space
* Image Processing
* Real-Time Computer Vision

## ⚙️ How It Works

1. The webcam captures the background without the cloak.
2. The captured background is stored for later use.
3. The live camera feed is converted from BGR to HSV.
4. Red-colored regions are detected using HSV thresholds.
5. A mask is created for the detected cloak.
6. The cloak area is replaced with the stored background.
7. The remaining part of the live frame is combined with the background to create the invisibility effect.

## ▶️ How to Run

Install the required libraries:

```bash
pip install opencv-python numpy
```

Run the Python file:

```bash
python invisible_cloak.py
```

Press **ESC** to close the application.

## 📂 Project Structure

```text
Invisible-Cloak/
│
├── invisible_cloak.py
├── README.md
└── requirements.txt
```

## 🎯 Learning Outcomes

This project helped in understanding **real-time computer vision, color segmentation, masking, morphological operations, background subtraction, and webcam-based image processing** using Python and OpenCV.
