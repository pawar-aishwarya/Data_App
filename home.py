import streamlit as st
from PIL import Image
import numpy as np 
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import tensorflow as tf

st.set_page_config(page_title='app',layout="wide",page_icon='👩‍🎓')


photo_url=Image.open("C:/Users/HP/Desktop/data_science_internship/proj_2/dp.jpg")
st.title('welcome to my App')

st.title('HI, this is **:blue[AISHWARYA PAWAR]**')
st.subheader('Data Science Enthusiastic')
st.title('Data Science Intern At :red[INNOMATICS] RESEARCH LAB')
st.subheader('Wish to connect?')
st.write('Email: aishwaryapwar399@gmail.com')
st.write('Linkedin:https://www.linkedin.com/in/aishwarya-pawar-733a97231')
st.write('github:https://github.com/pawar-aishwarya')


