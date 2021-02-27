# Invisibility-Cloak

## About
Hello there 👋! I am [Sakshi Gupta](https://www.linkedin.com/in/sakshi-gupta-49ab8b179/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3B3wtZ8RY%2FR1KWRtb%2FZ0qBew%3D%3D) a backend developer and Machine Learning Enthusiast. After attending a super fun boot-camp about Data Science and Machine Learning I learned how to work around with python libraries like [OpenCv](https://opencv.org/) and [Numpy](https://numpy.org/).

## Logic
The basic idea of this project is to build a invisibility cloak which will:
1. 📸 Capture the background image and save it. 
2. 🏃‍♀️ Read input video frame by frame and Replace all the pixels of the cloth (here I have used a *red* colored cloth) with those of the background image.

## Languages & Libraries Used
The complete project is created using one language i.e [Python](https://www.python.org/). There are two python libraries used:
1. [OpenCV](https://opencv.org/) : It is a huge open-source library for the computer vision, machine learning, and image processing and it plays a major role in real-time operation which is very important in today's systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human.
2. [Numpy](https://numpy.org/): It is an open-source numerical Python library. NumPy contains a multi-dimensional array and matrix data structures. It can be utilised to perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines.

Install the latest version of [Python3](https://www.python.org/downloads/)

```
pip install opencv-python      #installs opencv
pip install numpy              #installs numpy

```

## Steps
- [background.py](https://github.com/sakshigupta265/Invisibility-Cloak/blob/master/background.py)
    1. Capture the background image.
    2. Save it.
- [invisibility_cloak.py](https://github.com/sakshigupta265/Invisibility-Cloak/blob/master/invisibility_cloak.py)
    1. Read input video frame by frame.
    2. Convert the frame from bgr to hsv (best for color detection).
    3. Set the bgr value of red color in a numpy array.
    4. Convert it into hsv.
    5. Determine the threshold values for detecting red color (basically used to determine the shades of red).
    6. Create masks to detect the red color only.
    7. Refine the masks by using [morphology techniques](https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html)
    8. Create anti-mask to determine all the colors except red.
    9. Combine the background and the current frame.
    10. Let the magic begin!


## How to run this code?
* Fork this repository.
* Download soource code.
* Open command prompt.
* Switch to the directory where the project is stored.
* Run the [background.py]() file using `python background.py`
* Run the [invisibility_cloak]() file using `python invisibility_cloak.py`

## Demo

## Thanks! 🎉

