from streamlit import session_state as state
import openai

MODEL = 'gpt-3.5-turbo' # gpt-4 is restricted yet


# Quick Start: https://platform.openai.com/docs/api-reference/authentication
def login() -> None:
    openai.organization = state.org_id
    openai.api_key = state.api_key
    openai.Model.list() # won't work if API key or organization id is incorrect


# Input parameters documentation: https://platform.openai.com/docs/api-reference/chat/create
# Output description: https://platform.openai.com/docs/guides/gpt/chat-completions-response-format
def call(**kwargs) -> str:
    completion = openai.ChatCompletion.create(
        model=MODEL,
        **kwargs
    )
    return completion.choices[0].message.content


def pick_random_topic() -> None:

    '''
    Generates a random song topic with ChatGPT.
    '''

    # tell ChatGPT which role it should imitate
    role = 'You are a famous and influencial song writer. The lyrics of the songs that you\'ve created are known by millions.'
    
    # user request
    request = 'Give me a random lyrics topic. Return only the topic with no additional info.'

    temperature = 2 # 0 to 2 from less to more creative
    max_tokens = 30 # a short topic
    messages = [
        {
            'role':     'system',
            'content':  role
        }, # first assign the role
        {
            'role':     'user',
            'content':  request
        } # now send the request
    ]

    # Input parameters documentation: https://platform.openai.com/docs/api-reference/chat/create
    # Output description: https://platform.openai.com/docs/guides/gpt/chat-completions-response-format
    topic = call(
        temperature=temperature,
        max_tokens=max_tokens,
        messages=messages
    ) # will send the request and process the output, returns a string

    state.topic = topic
    # return topic


def generate_lyrics() -> None:

    '''
    Generates lyrics with ChatGPT.
    '''

    # tell ChatGPT which role it should imitate
    role = 'You are a famous and influencial song writer. The lyrics of the songs that you\'ve created are known by millions.'

    # user request
    decade = '' if state.decade is None else f'Let the lyrics be as if it would\'ve been written in {state.decade}-s.'
    request = f'Write lyrics for a song about {state.topic} in the {state.genre} genre. {decade} Return only the lyrics.'

    temperature = 0.5 # make it more strict to the request
    messages = [
        {
            'role':     'system',
            'content':  role
        }, # first assign the role
        {
            'role':     'user',
            'content':  request
        } # now send the request
    ]

    lyrics = call(
        temperature=temperature,
        messages=messages
    )

    state.lyrics = lyrics
    # return lyrics