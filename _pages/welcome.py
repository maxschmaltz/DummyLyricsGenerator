import streamlit as st
from streamlit import session_state as state
import json

from backend import login, pick_random_topic

with open('./_pages/help.json') as h: _help = json.load(h)


def st_login() -> None:
    try:
        login()
        state.logged_in = True
        pick_random_topic()
    except:
        state.logged_in = False
        state.api_key = None
        state.org_id = None
        

def show() -> None:

    '''
    Show welcome page with explanations.
    '''
    
    st.title('Lab 11. WebApp with ChatGPT')
    st.header('About')
    st.markdown(_help['about'])
    back_col, front_col = st.columns(2) # two equal columns
    with back_col: 
        with st.expander('Backend', expanded=True): st.markdown(_help['backend'])
    with front_col: 
        with st.expander('Frontend', expanded=True): st.markdown(_help['frontend'])

    with st.expander('Login', expanded=True):

        st.markdown(_help['login'])
        key_col, id_col = st.columns(2) # two equal columns
        with key_col: state.api_key = st.text_input(label='API key')
        with id_col: state.org_id = st.text_input(label='Organization id')
        
        # will call `st_login()` on click
        if st.button('Login', on_click=st_login): pass
        if state.logged_in is False: st.error('API key or organization id is incorrect.')