# Face and Eye Detection Project

> **🇹🇷 Türkçe versiyon için [README_TR.md](README_TR.md) dosyasına bakın**
A real-time face and eye detection application using OpenCV and Haar Cascade classifiers.

## Features

- Real-time face detection using webcam
- Eye detection within detected faces
- Support for video file input
- Green rectangles around detected faces
- Red rectangles around detected eyes

## Requirements

- Python 3.7+
- OpenCV
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Semihkulekcioglu/face_eyes_detection.git
cd face_eyes_detection
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Webcam Mode
```bash
python face_eyes_detection.py
```

### Video File Mode
To use with video files, uncomment and modify this line in the code:
```python
cap = cv2.VideoCapture("video1.mp4")
```

## Controls

- Press `ESC` key to exit the application

## Project Structure

- `face_eyes_detection.py.py` - Main application file
- `requirements.txt` - Python dependencies
- `video1.mp4`, `video2.mp4`, `video3.mp4` - Sample video files for testing

## How It Works

The application uses Haar Cascade classifiers to detect faces and eyes:
1. Captures video from webcam or video file
2. Converts frames to grayscale for processing
3. Detects faces using `haarcascade_frontalface_default.xml`
4. For each detected face, detects eyes using `haarcascade_eye.xml`
5. Draws bounding boxes around detected faces and eyes
6. Limits eye detection to maximum 2 eyes per face

## License

This project is licensed under the MIT License - see the LICENSE file for details.
