# MissShutdown


# Peace Sign Shutdown

This project allows you to shut down your computer by showing a peace sign in front of your camera using hand gestures. It uses **OpenCV**, **MediaPipe**, and **NumPy** for hand tracking and image processing. When a peace sign is detected, the system will initiate a shutdown of your computer.

## Features

- Detects the peace sign using hand gestures.
- Initiates a shutdown command when the peace sign is detected.
- Supports Windows, Linux, and macOS (Darwin).
- Simple, real-time hand gesture recognition through your webcam.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- **OpenCV**: For handling video capture and image processing.
- **MediaPipe**: For hand tracking.
- **NumPy**: For array manipulation and math operations.
- **Platform**: For determining the operating system.

You can install the necessary packages using pip:

```bash
pip install opencv-python mediapipe numpy
```

## How It Works

1. The script uses the webcam to capture live video.
2. MediaPipe Hand tracking is used to detect the position of fingers in real-time.
3. The script checks if the middle finger is raised (which forms a peace sign) and triggers a shutdown.
4. The script will attempt to shut down the system based on the OS being used.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/shruti-madhav/MissShutdown.git
cd peace-sign-shutdown
```

2. Run the script:

```bash
python main.py
```

3. Show the peace sign in front of your webcam to trigger the shutdown.
4. Press `q` to exit the program.

## Supported Operating Systems

- Windows
- Linux
- macOS (Darwin)

The script uses the platform-specific shutdown command to shut down the system.

## Notes

- This program uses your webcam, so make sure you have it properly set up.
- The peace sign gesture detection is based on the position of the fingers, specifically the middle finger (when raised).

## Future Improvements

- Add a visual indicator (e.g., countdown) before the shutdown.
- Make the program user specific