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
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

with open(config_file_path, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
