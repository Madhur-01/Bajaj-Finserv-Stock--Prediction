# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 20:21:24 2023

@author: madhu
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import sklearn
import os


path = os.path.dirname(__file__)
my_file = path+'/trained_model.pkl'

model = pickle.load(open(my_file, 'rb'))

df = pd.read_excel("C:/Users/madhu/Dropbox/My PC (LAPTOP-9DI2D1AT)/Documents/GitHub/Stock-Price-Predction/BAJAJFINSV.csv")

df[''] = pd.to_datetime(df['Date'], format='%Y')
df.set_index(['Date'], inplace=True)

st.set_page_config(layout='centered')
image = Image.open('/content/Add a heading.jpg')
st.image(image)

year = st.slider("Select number of Years",1,30,step = 1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Predict"):

        col1, col2 = st.columns([2,3])
        with col1:
             st.dataframe(pred)
        with col2:
            fig, ax = plt.subplots()
            df['CO2'].plot(style='--', color='gray', legend=True, label='known')
            pred['CO2'].plot(color='b', legend=True, label='prediction')
            st.pyplot(fig)