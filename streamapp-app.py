import streamlit as st
from skimage import io
import matplotlib.pyplot as plt
import cv2 as cv

# st.write("Some default urls to use - ")
# this also works - st.image(image = "url")
# https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html

st.header("Image Processing")

URL_user = st.text_input("Image URL goes here")
filter = st.selectbox("Which filter/Algorthm would you like to use",('Non Local Means Denoising Algorithm','Gaussian Filter'))


def NLMD(img):
    h = st.slider("how powerful should the filter be(10 preferably)",1,100,10,1)
    dst = cv.fastNlMeansDenoisingColored(img,None,h,10,7,21)
    st.image(image=dst,caption = "after fast NL means denoising filter")
    
col1,col2 = st.columns(2)

with col1:
    img = io.imread(URL_user)
    st.image(image=img,caption = "before")

with col2:
    if filter == 'Non Local Means Denoising Algorithm':
        NLMD(img)
    else:
        st.write("Choose a filter you dumb bitch")

