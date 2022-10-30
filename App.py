import streamlit as st
import cv2
import numpy as np
import os
import io
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.success("Select a demo above.")

st.write("""
# This Web App is the tutorial
This app predicts the **What Aditya says**!
""")

