# -*- coding: utf-8 -*-

# External Python Modules
import cv2
import streamlit as st
from datetime import datetime

if __name__ == "__main__":
    st.title("Webcam")
    start = st.button("Start Camera")

    if start:
        cam_image = st.image([])
        video = cv2.VideoCapture(0) # 0 to use the main camera (integrated to laptop). Otherwise 1
        stop = st.button("Stop Camera")

        while not stop:
            check, frame = video.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            now = datetime.now()
            cv2.putText(img=frame, text=now.strftime("%A %d/%m/%Y"), org=(30,25),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255),
                        thickness=1, lineType=cv2.LINE_AA)
            cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30,50),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,0,0),
                        thickness=1, lineType=cv2.LINE_AA)
            cam_image.image(frame)
        video.release()