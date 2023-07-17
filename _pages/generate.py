import streamlit as st
from streamlit import session_state as state
import time

from backend import pick_random_topic, generate_lyrics


def reset() -> None:

    '''
    Reset the workflow and erase all generated / input data.
    '''

    # state.logged_in = True
    state.generating = False

    # reset all generated / input data
    pick_random_topic()
    state.genre = None
    state.specify_decade = False
    state.decade = None

    state.lyrics = None


def show() -> None:

    '''
    Generate and show lyrics.
    '''

    st.header('Generated Lyrics')

    placeholder = st.empty()
    placeholder.info('Generating...') # this will inform user in a disappearing placeholder
    generate_lyrics()
    placeholder.info('Generated!'); time.sleep(1.5)
    placeholder.empty() # placeholder disappears

    with st.expander('Lyrics', expanded=True):
        st.write(state.lyrics)

    st.download_button('Download Lyrics', data=state.lyrics, file_name='Lyrics.txt', mime='txt')

    if st.button('Rerun Model', on_click=reset): pass