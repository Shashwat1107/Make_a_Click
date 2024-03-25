# Make_a_Click

Make_a_Click is a Python project that enables users to control their computer's mouse cursor using their index finger and perform a click action by making a specific gesture. This project utilizes Python along with OpenCV for finger tracking and PyAutoGUI for mouse control.

## Features

- **Finger Tracking:** Uses OpenCV to detect and track the movement of the user's index finger.
- **Mouse Control:** Maps the movement of the finger to control the mouse cursor on the desktop.
- **Click Action:** Recognizes a specific gesture, such as bringing the thumb and index finger together, to simulate a click action.
- **Customizable:** The project can be easily customized and extended to suit specific user preferences or requirements.

## Requirements

- Python <3.11 (64-bits)
- opencv-python (4.9.0.80)
- pyautogui (0.9.54) 
- mediapipe (0.10.11)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/Make_a_Click.git
    ```

2. Install the required Python packages:

    ```
    pip install mediapipe opencv-python pyautogui
    ```

3. Run the main script:

    ```
    python make_a_click.py
    ```

## Usage

1. Launch the script by running `FingerToCursor.py`.
2. Position your index finger in front of the camera.
3. Move your finger to control the mouse cursor.
4. To click, make the specified gesture (e.g., bring your thumb and index finger together).

   **CAUTION: if the index finger moves, the mouse moves along, mis placed clicks might happen.**
6. Press `q` to exit the application.

## Contribution

Contributions are very welcome! If you want to contribute to this project, feel free to submit a pull request.
As It's till under construction And NEEDs Improvements.
---
