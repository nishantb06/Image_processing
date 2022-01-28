import streamlit as st
from skimage import io,img_as_float
import matplotlib.pyplot as plt
import cv2 as cv
import bm3d
import numpy as np
# st.write("Some default urls to use - ")
# this also works - st.image(image = "url")
# https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html

st.header("Image Processing")
st.markdown ("A few links for referece - [1](https://dynamic-image-resizer.sharechat.com/imageResizer/%E0%A4%AE%E0%A5%8B%E0%A4%B9%E0%A4%AC%E0%A5%8D%E0%A4%AC%E0%A4%A4%E0%A4%A6%E0%A4%BF%E0%A4%B2%E0%A4%B8%E0%A5%87_2f7f27e1_1642514168134_sc_atrbtd.jpg)")
st.markdown("[2](https://dynamic-image-resizer.sharechat.com/imageResizer/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3%E0%A4%95%E0%A4%A5%E0%A4%BE%E0%A4%8F%E0%A4%82_35279ab8_1642535570715_sc_atrbtd.jpg) link for reference")
URL_user = st.text_input("Image URL goes here")
filter = st.selectbox("Which filter/Algorthm would you like to use",('Non Local Means Denoising Algorithm','Bilateral Filter',
                                                                        'Gaussian Filter',"Median Filter","BM3D Filter","All"))


def NLMD(img,mode = "single"):
    
    h = st.slider("how powerful should the filter be(10 preferably)",1,100,10,1)
    dst = cv.fastNlMeansDenoisingColored(img,None,h,10,7,21)

    if mode == "single":
        col1,col2 = st.columns(2)
        with col1:
            st.image(image=img,caption = "before")

        with col2:
            st.image(image=dst,caption = "after fast NL means denoising filter")
    
    else:
        return dst
    

def BilateralFilter(img,mode = "single"):
    dst = cv.bilateralFilter(img, 5, 10, 10)

    if mode == "single":
        col1,col2 = st.columns(2)
        with col1:
            st.image(image=img,caption = "before")

        with col2:
            st.image(image=dst,caption = "after Bilateral filter")
    else:
        return dst

def GaussianFilter(img,mode = "single"):
    dst = cv.GaussianBlur(img, (9, 9), 0)

    if mode == "single":
        col1,col2 = st.columns(2)
        with col1:
            st.image(image=img,caption = "before")

        with col2:
            st.image(image=dst,caption = "after Gaussian filter")
    else:
        return dst


def MedianFilter(img,mode = "single"):
    dst = cv.medianBlur(img, 9)

    if mode == "single":
        col1,col2 = st.columns(2)
        with col1:
            st.image(image=img,caption = "before")

        with col2:
            st.image(image=dst,caption = "after Gaussian filter")
    else:
        return dst

def BM3DFilter(img,mode = "single"):
    img = img_as_float(img)
    #dst = bm3d.bm3d(img,sigma_psd = 0.05,stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)
    # dst = np.clip(dst,0,1)

    sigma = st.slider("how powerful should the filter be(10 preferably)",min_value=0,max_value=100,value = 10,step=1)
    dst = bm3d.bm3d(img,sigma_psd = sigma/100,stage_arg=bm3d.BM3DStages.ALL_STAGES)

    if mode == "single":
        col1,col2 = st.columns(2)
        with col1:
            st.image(image=img,caption = "before")

        with col2:
            st.image(image=dst,caption = "after BM3D filter",clamp  =True)
    else:
        return dst

    
img = io.imread(URL_user)
if filter == "Non Local Means Denoising Algorithm":
    nlmd_img = NLMD(img)
elif filter == "Bilateral Filter" :
    bilateral_img = BilateralFilter(img)
elif filter == 'Gaussian Filter':
    gaussian_img = GaussianFilter(img)
elif filter =="Median Filter":
    median_img = MedianFilter(img)
elif filter == "BM3D Filter":
    bm3d_img = BM3DFilter(img)
elif filter == "All":
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(img,caption = "original")
        bilateral_img = BilateralFilter(img,mode = "double")
        st.image(bilateral_img,caption = "bilateral")
    with col2:
        median_img = MedianFilter(img,mode = "double")
        st.image(median_img,caption = "Median")
        guassian_img = GaussianFilter(img,mode = "double")
        st.image(guassian_img,caption  = "Gaussian")   
    with col3:
        bm3d_img = BM3DFilter(img,mode = "double")
        st.image(bm3d_img,caption = "BM3d",clamp = True)
        nlmd_img = NLMD(img,mode = "double")
        st.image(nlmd_img,caption = "NLMD")
    