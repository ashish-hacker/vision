from helper import *                       #importing all the helper fxn from helper.py which we will create later
import streamlit as st
import re
import sys
import os
from streamlit.cli import main
# import pyttsx3
from PIL import Image

# engine = pyttsx3.init()


def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('static/images',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0

def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Caption Generator</h1>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center; color: Black;'>describing the content of the image</h4><br><br>", unsafe_allow_html=True)
    st.sidebar.header("What is this Project about?")
    st.sidebar.text("It a Web app that would help the user generate caption from an image. In other words it shows the ability of computers to visualize images conceptually.")
    st.sidebar.header("What tools where used to make this?")
    st.sidebar.text("The Model was trained using the Flickr8k dataset on google colab. We made use of Deep Neural Networks to train the model.")
    

    uploaded_file = st.file_uploader("Select image to generate caption")
    

    if st.button('Generate Caption'): #making and printing our prediction
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(uploaded_file, width=500)
            caption = generate_caption(img)
            # st.image(uploaded_file, width=264)
            st.markdown(f"<h3 style='text-align: left; color: Black;'>{caption[5:-3]}</h3>", unsafe_allow_html=True)
            # engine.say(caption[5:-3])
            # engine.runAndWait()
        else:
            st.error('Select an image to generate caption')




if __name__ =='__main__':
    main()
    
