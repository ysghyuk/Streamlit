import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit for sin and cos fuctioni visualiztion')

x_start = st.slider('x 시작값' ,  0.0, 10.0, 0.0)
x_end = st.slider('x 시작값' ,  10.0, 20.0, 10.0)


x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)

import matplotlib.pyplot as plt # 시각화 라이브러리
fig, ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin','cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.set_title('sin and cos fuction')


st.pyplot(fig) 

@st.cache
def expensive_computation(x):
    return np.sin(x) + np.cos(x)    

result=expensive_computation(x)

