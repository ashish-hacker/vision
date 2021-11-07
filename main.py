from helper import *                       #importing all the helper fxn from helper.py which we will create later
import streamlit as st
import re
import sys
import os
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="darkgrid")
# sns.set()
# from PIL import Image
st.title('Caption Generator')

#loading our model
#model = pickle.load(open('model.pkl','rb'))

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('static/images',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Caption Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: Black;'>Submission for The Project</h4>", unsafe_allow_html=True)
    st.sidebar.header("What is this Project about?")
    st.sidebar.text("It a Web app that would help the user generate caption from an image. In other words it shows the ability of computers to visualize images conceptually.")
    st.sidebar.header("What tools where used to make this?")
    st.sidebar.text("The Model was made using a dataset from Google along with using Google colab to train the model. We made use of Deep Neural Networks to train the model.")
    inputs = [[]]

    if st.button('Predict'): #making and printing our prediction
        # result = model.predict(inputs)
        # updated_res = result.flatten().astype(float)
        st.success('The Probability of getting admission is {}'.format(1))



if __name__ =='__main__':
    main()
