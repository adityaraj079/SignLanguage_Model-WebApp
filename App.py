import streamlit as st
import cv2
import numpy as np
import os
import io
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from PIL import Image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
import av
from streamlit_webrtc import webrtc_streamer
import webbrowser

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Sign Language Recognition using Action Detection - WebApp")

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   The *Sign Language detection* app is used to detect sign language by studying the action of the subject using machine learning algorithm *Holistic media pipeline* [MediaPipe Holistic](https://google.github.io/mediapipe/solutions/holistic.html) used in this model for accurate and flawless operation
-   It uses a LSTM training technique that leverages multiple NLP embeddings and relies on [Tensorflow](https://www.tensorflow.org/) to train the model using data frames in video form and make proper decisions.
	    """
    )

    st.markdown("")

st.subheader('* This app is made for demonstration purposes only')
st.markdown("")
st.subheader('Head over to the Model.py page to experience the model in real time')
st.write('NOTE - Use this web app on a desktop system only with an working webcam')
st.title('Some working examples are:')

with st.expander("Images ", expanded=True):
    col1, col2 = st.columns(2)
    col1.image('Images\img1.png')
    col2.image('Images\img2.png')
    st.image('Images\img3.png')
    

with st.expander("Videos ", expanded=True):
    col1, col2 = st.columns(2)
    col1.video('Videos\midsem.mp4')
    col2.video('Videos\endsem.mp4')

github_url = 'https://github.com/adityaraj079/SignLanguage_Model-WebApp'
model_url = 'https://github.com/adityaraj079/Minor_2'
creater_url = 'https://www.linkedin.com/in/aditya-raj-7b2632191/'

st.title('Basic Info:')
col1, col2, col3=st.columns(3)
if col1.button('Github Code'):
    webbrowser.open_new_tab(github_url)
if col2.button('Model Code'):
    webbrowser.open_new_tab(model_url)
if col3.button('Creater'):
    webbrowser.open_new_tab(creater_url)