import streamlit as st
from streamlit import session_state as state
import json

with open('./_pages/help.json') as h: _help = json.load(h)

from backend import pick_random_topic


def show() -> None:

    '''
    Show parameters page where user either input parameters or sees the chosen ones.
    '''

    st.header('Parameters')

    with st.expander('Parameters Explanation', expanded=not state.generating): st.markdown(_help['params'])

    if not state.generating: # let choose the parameters

        topic_col, params_col = st.columns([3, 2]) # two columns of widths 3/5 and 2/5 respectively

        with topic_col:

            st.subheader('Topic')

            if st.button('Random topic'): pick_random_topic()
            state.topic = st.text_input('Input Topic', value=state.topic)

        with params_col:

            st.subheader('Parameters')

            state.genre = st.selectbox(label='Genre', options=['Pirate Metal', 'Nerdcore', 'German Reggae', 'Chillwave', 'Wizard Rock'])
            state.specify_decade = st.checkbox(label='Specify Decade')
            if state.specify_decade:
                state.decade = st.slider(label='Decade', min_value=1700, max_value=2300, value=2020, step=10)

        if st.button('Generate', on_click=setattr, args=(state, 'generating', True)): pass

    else: # show chosen parameters in the JSON format

        # params = pd.DataFrame(
        #     data={
        #         'value': [state.topic, state.genre, state.decade]
        #     },
        #     index=['Topic', 'Genre', 'Decade'],  
        # )
        # params.dropna(axis=0, inplace=True) # so that decade drops if not assigned
        # st.dataframe(params)

        params = {
            'Topic': state.topic,
            'Genre': state.genre,
            # 'Decade': state.decade
        }
        if state.decade is not None: params['Decade'] = state.decade
        st.json(params)