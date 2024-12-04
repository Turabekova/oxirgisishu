import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Tilni aniqlash modeli")
input_test = st.text_input("Bu yerga text kiriting", 'Hello my name is Jamila ')

button_clicked = st.button("Tilni aniqlash")
if button_clicked:
	st.text(Lrdetect_Model.predict([input_test]))
