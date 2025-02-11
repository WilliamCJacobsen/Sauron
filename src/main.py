from sauron import Sauron
from convolution_nn import ConvolutionNN
import cv2
import os
import time
import numpy as np
#from picamera import PiCamera


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
FACE_CASCADES = cv2.CascadeClassifier(os.path.join(PROJECT_ROOT, "cascades/data/haarcascade_frontalface_alt2.xml"))

if __name__ == "__main__":
    conv = ConvolutionNN(cv2, FACE_CASCADES, 64)
    conv.model_summary()
#
#    conv.train();
    the_eye = Sauron(conv)
    
    while True:
        the_eye.recoginze()
    

"""
    cam = PiCamera(resolution=RESOLUTION)
#    cam.rotation = 180 # uncomment to rotate (valid values are 0, 90, 180, 270)

    # buffer width and height have to be multiples of 32 and 16 respectively
    # but we can slice off the padding pixels later (without copying)
    # opencv numpy array images have dimensions (y, x, channel)
    def ceil_mul(x, mul):
        mod = x % mul
        return x if mod == 0 else x + mul - mod

    # opencv python bindings use numpy arrays for images. dimensions are (y, x, channel)
    shape = (ceil_mul(RESOLUTION[1], 16), ceil_mul(RESOLUTION[0], 32), 3)
    buf = np.empty(shape, dtype=np.uint8)

    while True:
        cam.capture(buf, format="bgr", use_video_port=USE_VIDEO_PORT)
        frame = buf[:RESOLUTION[1],:RESOLUTION[0]] # slice off padding pixels
        assert frame.base is buf # make sure slicing doesn't copy
        value = conv.recoginze(frame)
        print(value)""";