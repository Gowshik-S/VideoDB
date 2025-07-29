
import streamlit as st
import requests
import os

st.set_page_config(page_title='VidCraftAI', page_icon='🎬', layout='wide')

st.title('🎬 VidCraftAI')

api_url = os.getenv('API_URL', 'http://localhost:8000')

# Authentication guard
if 'id_token' not in st.session_state:
    st.warning('You must log in from the sidebar to access VidCraftAI.')
    st.stop()

# Main application content
st.subheader('Backend Utilities')

if st.button('Ping Backend'):
    response = requests.get(f"{api_url}/chat/ping", headers={"Authorization": f"Bearer {st.session_state['id_token']}"})
    st.write(response.json())

# Logout control
if st.button('Logout'):
    st.session_state.clear()
    st.experimental_rerun()
