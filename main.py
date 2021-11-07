from helper import *                       #importing all the helper fxn from helper.py which we will create later
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import os
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="darkgrid")
# sns.set()
# from PIL import Image
# st.title('Caption Generator')

#loading our model
#model = pickle.load(open('model.pkl','rb'))

def save_img(img):
    try:
        with open(os.path.join('static/images',img.name),'wb') as f:
            f.write(img.getbuffer())
        return 1
    except:
        return 0

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Caption Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: Black;'>Upload Image.</h3>", unsafe_allow_html=True)
    img = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
    # st.image(img,width=250,height=250)
    # st.markdown("<h4 style='text-align: center; color: Black;'>Submission for The Project</h4>", unsafe_allow_html=True)

    file = img.getvalue()
    st.sidebar.header("What is this Project about?")
    st.sidebar.text("It a Web app that would help the user generate caption from an image. In other words it shows the ability of computers to visualize images conceptually.")
    st.sidebar.header("What tools where used to make this?")
    st.sidebar.text("The Model was made using a dataset from Google along with using Google colab to train the model. We made use of Deep Neural Networks to train the model.")
    max_length = 32


    tokenizer = load(open("tokenizer.p", "rb"))
    model = load_model('models/model_9.h5')
    xception_model = Xception(include_top=False, pooling="avg")
    path = '/home/ashish/Pictures/Heavy Metal -Memes.jpeg'
    photo = extract_features(file, xception_model)
    

    description = generate_desc(model, tokenizer, photo, max_length)
    print("\n\n")
    print(description)
    plt.imshow(img)

    # if st.button('Predict'): #making and printing our prediction
    #     # result = model.predict(inputs)
    #     # updated_res = result.flatten().astype(float)
    #     st.success('The Probability of getting admission is {}'.format(1))



if __name__ =='__main__':
    main()
