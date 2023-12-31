
import pandas as pd
import numpy as np
import streamlit as st

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns = ['data'])
st.line_chart(chart_data)
