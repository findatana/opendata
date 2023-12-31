import streamlit as st
import streamlit.components.v1 as components

# Open the HTML file and read its contents
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Display the HTML content in the Streamlit app
components.html(html_content)