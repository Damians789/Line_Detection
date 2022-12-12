# Line_Detection
Python program to detect road lines from a video

Used:
- Python
- cv2
- numpy

Example:
![obraz](https://user-images.githubusercontent.com/92166393/207157005-5203badd-0b46-44a5-af66-dc156952a518.png)

About:
Before detection can be started, we need to first preprocess our working material. This part includes things such as finding the best ROI (region of interest), because we only need selected part of frame. To do that we need to mask the image using build in functions, as fillPolly or bitwise_and from cv2 package. To find edges it is advised to use grayscaled version, so we can make a better use of Canny technique. Lines detection is done with Hough transofrm technique and then put on the original frames.

Additionally it counts the number of frames and prints out my name
