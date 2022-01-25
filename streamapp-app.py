import streamlit as st
from skimage import io
import matplotlib.pyplot as plt




st.header("Image Processing")


#URL_user = st.text_input("Image URL goes here")

img = io.imread("https://img.search.brave.com/Zp6LqdKNaQBBggKGYdp0Yn-ogwHhdzv23fc69PkZ9n8/rs:fit:1068:588:1/g:ce/aHR0cHM6Ly93d3cu/bGlmZWRlci5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTkv/MTEvWmlndXJhdC1k/ZS1Vci1mb3RvLWxp/ZmVkZXItbWluLTEw/Njh4NTg4LmpwZw")

#if URL_user:
#    img = io.imread(URL_user)

    

st.image(image=img,caption = "this was read with io.imread(url)")
# this also works - st.image(image = "url")
