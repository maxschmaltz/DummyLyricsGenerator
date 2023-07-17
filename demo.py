import streamlit as st
from streamlit import session_state as state

from _pages import welcome, params, generate


def init() -> None:

    '''
    Initializes variables needed for the workflow.
    '''

    # `streamlit.session_state` documentation: https://docs.streamlit.io/library/api-reference/session-state
    state.api_key = None # most of the parameters are not necessary and declared just for inference
    state.org_id = None

    state.logged_in = None # not boolean because it should be `None` at first to prevent error message in case of `False`
    state.generating = False

    state.topic = None
    state.genre = None
    state.specify_decade = None
    state.decade = None

    state.lyrics = None

    state.initialized = True


def main():

    if 'initialized' not in state: init()

    menu = {
        'About': 'A simple lyrics generator.'
    }

    # `streamlit.set_page_config` documentation: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
    st.set_page_config(
        page_title='Lab 11. WebApp with ChatGPT',
        initial_sidebar_state='collapsed',
        menu_items=menu
    )
    
    # the workflow: note the scheme!
    if not state.logged_in: welcome.show()
    else: params.show()
    if state.generating: generate.show()


if __name__ == '__main__':
    main()