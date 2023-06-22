from enum import Enum
from io import BytesIO, StringIO
from typing import Union
import pandas as pd
import streamlit as st
from PIL import Image

from img_classification import currency_classification

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

st.title("Indian Currency Classifier")
st.header("Classifies 6 types of Indian Currency 10,20,50,100,500,1000")
st.text("Upload image of Indian Currency note")

class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        image = Image.open(file)
        st.image(image, caption='Uploaded Note', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        st.write("Just a minute")
        label = currency_classification(image, 'model.h5')
        switcher = {
            0 : "fifty", 
            1: "fivehundred",
            2: "hundred",
            3: "ten",
            4:"thousand",
            5:"twenty"
        }



        # file.close()

if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()