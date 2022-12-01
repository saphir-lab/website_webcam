# -*- coding: utf-8 -*-

# External Python Modules
import cv2
import streamlit as st

if __name__ == "__main__":
    st.title("Webcam")
    start = st.button("Start Camera")

    if start:
        cam_image = st.image([])
        video = cv2.VideoCapture(0) # 0 to use the main camera (integrated to laptop). Otherwise 1
        stop = st.button("Stop Camera")

        while not stop:
            check, frame = video.read()
            cam_image.image(frame)
        video.release()