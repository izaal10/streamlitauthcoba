import streamlit as st
import streamlit_authenticator as stauth
import os
import yaml
from yaml import SafeLoader

script_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_directory, '../config.yml')

with open(config_file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # Random password should be transferred to the user securely
    else:
        st.error('Username not found')
except Exception as e:
    st.error(e)
