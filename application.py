# import the necessary packages
import numpy as np
import cv2

from camera import VideoCamera
from flask import Flask,render_template,Response, request,redirect, url_for



application=Flask(__name__)


def gen(camera):

    while True:
        frame=camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+ frame
               + b'Content-Type: \r\n\r\n'
               + b'\r\n\r\n')

@application.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@application.route('/')
def First():
    return render_template('detect.html')


if __name__=="__main__":
	
    application.run(port=5000, debug=True)


