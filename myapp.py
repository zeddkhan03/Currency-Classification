import streamlit as st
from PIL import Image
st.title("Indian Currency Classifier")
st.header("Classifies 6 types of Indian Currency 10,20,50,100,500,1000")
st.text("Upload image of Indian Currency note")

from img_classification import currency_classification

uploaded_file = st.image(Image.open('100.jpeg'))

#uploaded_file = st.file_uploader("upload here",type="jpg")
#file = st.file_uploader("Please choose a file")
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    # Continue with the rest of your code for image classification

##if uploaded_file is not None:
##    print(type(uploaded_file))
##    image = Image.open(uploaded_file)
##    st.image(image, caption='Uploaded Note', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    st.write("Just a minute")
    label = currency_classification(image, 'model.h5')
    switcher = {
            0: "Five Hundred", 
            1: "Fifty",
            2: "hundred",
            3: "ten",
            4: "thousand",
            5: "twenty"
    }
    s=switcher.get(label, "Not Maching")
    st.write("Done..")
    if s=="Not Maching":
        st.write("Enter valid Image")
    else :
        st.write("This is ", s," rupees note")