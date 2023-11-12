# DIP-Workshop

# Hand Gesture Controlled Media Player

This project allows you to control your media player using hand gestures. It uses OpenCV, Mediapipe, and pyautogui 
to create an interactive experience where you can pause/play, skip tracks, and more with simple hand movements.

## Project Overview

- Captures live video of user and converts it into black and white using threshold value.
- Calculates contour reagion of user's hand and finds its centroid.
- Tracks hand movements and calculates hand velocity(By calculating velocity of its centroid).
- Simulates key presses to control a media player using PyAutoGUI

## How to Use

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/hand-gesture-media-player.git
   cd hand-gesture-media-player
   
2. Install Dependencies:
    pip install opencv-python
    pip install mediapipe
    pip install pyautogui
   
3. Run the Script:
    python hand_gesture_media_player.py
   
4. Gesture Controls:
    Make a fist: Pause/Play
    Move hand left: Previous track
    Move hand right: Next track
   
6. Exit the Application:
    Press 'Esc' key to exit the application
   
Customization : 
    Adjust velocity thresholds and key presses in the script based on your preferences.
    Explore additional features or gestures by extending the code.
    
Contributing :
    Feel free to contribute to this project. Open an issue or submit a pull request to suggest improvements or add new features.
