# Face Recognition Attendance System

## Introduction

This is a Python application built using the Tkinter GUI toolkit and OpenCV library for face recognition. It allows users to mark attendance by recognizing faces through a webcam. The system captures images, processes them, and matches them with stored images to identify individuals.

## Features

- Face recognition for attendance marking.
- GUI interface built with Tkinter.
- Utilizes OpenCV for image processing.
- Converts images to PNG format for better processing.

## Installation

1. Clone the repository to your local machine:

    ```bash
    https://github.com/Dhahlan3890/Face_Recognition_app.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python face_recognition_attendance.py
    ```

## Usage

1. Launch the application by running `gui.py`.
2. Click the button to start the attendance marking process.
3. The system will use the webcam to capture images and recognize faces.
4. Upon successful recognition, the person's name will be displayed, and attendance will be marked.
5. Repeat the process for other individuals.

## Customization

- Add more images to the `Images` folder for better face recognition accuracy.
- Modify the GUI elements in `FaceRecognitionApp` class in `gui.py` to suit your preferences.
- Adjust the duration of face recognition in the `open_camera_for_duration` function according to your needs.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.


## Acknowledgments

- Special thanks to [OpenCV](https://opencv.org/) for the face recognition functionality.
- Thanks to the developers of [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI toolkit.

## Contact

For any inquiries or support, please contact [Ahamed Dhahlan](mailto:ahameddhahlan2000@gmail.com).

--- 

Feel free to adjust the content as needed, adding more sections or details according to your project's specific requirements.
