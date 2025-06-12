import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

try:
    st.title("Information Display Robot")
    st.markdown("#It will display the information you enter as an image or dataframe.")

    upload = st.file_uploader("upload file for data")
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'windows-1254']
    for enc in encodings:
        try:
            upload.seek(0) # Dosya işaretçisini başa al, tekrar okuma yaparken önemli!
            data = pd.read_csv(upload, encoding=enc)
            break 
        except UnicodeDecodeError:
            pass

    vote = st.selectbox("select mod",["Picture","Dataset"])

    def columns_create():
        columns = [] 
        for i in data.columns:
            columns.append(i)
        option1 = st.selectbox("select column1",columns)
        option2 = st.selectbox("select column2",columns)
        return option1,option2

    def dataPandas():
        option1,option2 =  columns_create()
        new_data = {
            option1:data[option1],
            option2:data[option2]
        }
        second_data = pd.DataFrame(data=new_data)
        st.dataframe(second_data)

    def image():  
            option1, option2 = columns_create()
            fig, ax = plt.subplots()
            ax.scatter(data[option1], data[option2])
            ax.set_xlabel(option1)
            ax.set_ylabel(option2)
            st.pyplot(fig)

    if vote == "Picture":
        image()
    elif vote == "Dataset":
        dataPandas()

except:
    st.title("upload file")