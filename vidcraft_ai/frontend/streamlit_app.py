
import streamlit as st
import requests
import os

st.set_page_config(page_title='VidCraftAI', page_icon='🎬', layout='wide')

st.title('🎬 VidCraftAI')

api_url = os.getenv('API_URL', 'http://localhost:8000')

if 'id_token' not in st.session_state:
    st.session_state['id_token'] = 'REPLACE_WITH_FIREBASE_ID_TOKEN'

if st.button('Ping Backend'):
    response = requests.get(f"{api_url}/chat/ping", headers={"Authorization": f"Bearer {st.session_state['id_token']}"})
    st.write(response.json())
