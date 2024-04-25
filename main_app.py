import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
import base64
import requests

from read_image import read_im
from PIL import Image
from typing import List, Dict

""" 
# xxx

 ¡Bienvenido al Dermo-metro! 

Cada año, 16,000 mexicanos se enteran que tienen algún tipo de
cancer de piel. 
Sus principales causas incluyen exposición a radiación UV, 
desde largas jornadas bajo el sol como exposición a 

""" 

read_im()

st.header('Imagenes de Ejemplo')

col1, col2, col3 = st.columns(3)
with col1:
    img1_path = os.path.join(os.path.dirname(__file__), "images/melanoma.jpg")
    st.image(img1_path)
    img1_button = st.button("Score Image", key='1')
with col2:
    img2_path = os.path.join(os.path.dirname(__file__), "images/skinc.jpeg")
    st.image(img2_path)
    img2_button = st.button("Score Image", key='2')
with col3:
    img3_path = os.path.join(os.path.dirname(__file__), "images/tomato_leafspot")
    st.image(img3_path)
    img3_button = st.button("Score Image", key='3')
