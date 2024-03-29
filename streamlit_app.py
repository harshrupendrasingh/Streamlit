import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title('Basic Streamlit App')

# Header
st.header('This is a header')

# Subheader
st.subheader('This is a subheader')

# Text
st.write('This is some text.')

# Markdown
st.markdown('**This** is markdown.')

# Line break
st.write('\n')

# Data display
st.write('Display a DataFrame:')
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.write(df)

# Interactive widgets
st.write('Interactive Widgets:')
number = st.number_input('Enter a number:', value=1)
st.write('You entered:', number)
st.set_option('deprecation.showPyplotGlobalUse', False)
slider = st.slider('Select a range:', 0, 10, (3, 7))
st.write('Selected range:', slider)

# Plotting
st.write('Plot:')
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot()

# Checkbox
st.write('Checkbox:')
if st.checkbox('Show/hide text'):
    st.write('The checkbox is checked.')

# Button
if st.button('Click me'):
    st.write('Button clicked.')

# Selectbox
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Select an option:', options)
st.write('You selected:', selected_option)

# Multiselect
options = ['Option 1', 'Option 2', 'Option 3']
selected_options = st.multiselect('Select multiple options:', options)
st.write('You selected:', selected_options)

# File upload
st.write('File upload:')
file = st.file_uploader('Upload a file:')
if file is not None:
    st.write('File uploaded.')

# Display raw code
st.write('Display raw code:')
st.code("""
import streamlit as st

st.title('Streamlit App')
""")

# Display JSON
st.write('Display JSON:')
json_data = {'name': 'John', 'age': 30}
st.json(json_data)
