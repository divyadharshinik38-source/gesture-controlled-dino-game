# Gesture-Controlled Dino Game Using Computer Vision

A real-time computer vision project that enables touchless gameplay of the Chrome Dino Game using hand gestures captured through a webcam. The system detects raised fingers in real time and maps gestures to keyboard actions, allowing users to control the game without touching the keyboard.

## Features

- Real-time hand gesture recognition using OpenCV
- Finger counting based on contour analysis and convexity defects
- Touchless game control through PyAutoGUI
- Webcam-based gesture tracking
- Configurable gesture-to-key mapping
- Visual ROI (Region of Interest) tracking for gesture detection

## Technologies Used

- Python
- OpenCV
- NumPy
- PyAutoGUI

## Project Workflow

1. Capture live video from webcam
2. Detect hand region inside ROI
3. Apply image preprocessing and thresholding
4. Extract hand contours and convex hull defects
5. Count raised fingers
6. Map finger count to keyboard actions
7. Control the Chrome Dino Game in real time
   
## Demo

🎥 Demo Video: [https://youtu.be/your-video-id](https://www.linkedin.com/posts/divyadharshinik291126_computervision-python-opencv-ugcPost-7413110607660421120-hNjy/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFKVwnYBoZ_a7pru4c8ObXOEoHcre-9CFxA)


## Installation

1. Clone the repository

```bash
git clone https://github.com/divyadharshinik38-source/gesture-controlled-dino-game.git
