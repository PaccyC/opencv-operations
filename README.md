# OpenCV operations

The repository which shows how we can use OpenCV to do different actions on the images

---
##  Features

- **Basic Operations**: Image reading, resizing, cropping, and color transformations, drawing and Annotation
- **Image Transformations**: Rotation, scaling, and perspective transformations.
- **Feature Detection**: Detecting keypoints using SIFT, SURF, and ORB.
- **Object Detection and Tracking**: Implementing YOLO, Haar cascades, and template matching.
---

## Getting Started

### Prerequisites
- Python 3.9 or later
- OpenCV library (see installation below)


### Installing OpenCV library
Follow these steps to install OpenCV:

1. **Install OpenCV via pip**:
```bash
   pip install opencv-python
```

2.	**(Optional) Install Additional Modules:**
    For more functionalities, such as reading advanced image/video formats:

```bash
    pip install opencv-python-headless 
```

3.	**Verify Installation:**
Run the following script to confirm OpenCV is installed:

```bash
import cv2
print(cv2.__version__)
```

4.	**For Conda Users:**
If you’re using Anaconda:
```bash
conda install -c conda-forge opencv
```