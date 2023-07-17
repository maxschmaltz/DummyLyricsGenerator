# DummyLyricsGenerator: A dummy web app for generating funny lyrics with ChatGPT.

[![Generic badge](https://img.shields.io/badge/streamlit-red.svg)](https://dummy-lyrics-generator.streamlit.app/)

----------

### Contents:

* [Intro](#intro)
* [Quick Start](#quick-start)
* [Parameters](#parameters)
* [Acknowledgements](#acknowledgements)

----------

## Intro

`DummyLyricsGenerator` is solution of the Lab 11 for the Statistical Language Processing II course at Eberhard Karls Universität Tübingen in the SoSe23. The aim of the lab is to teach students basics of simple web app development with [`streamlit`](https://streamlit.io) and to introduce [ChatGPT API](https://platform.openai.com). In the lab, the students are given a starter code, where they should fill in the certain parts related both to `streamlit` and ChatGPT. The starter code is omitted in this repo.

The app is created exclusively for the course and is introduced to the students at the Lab 11 on 20.07.23.


## Quick Start

The app is implemented with `streamlit` and is therefore hosted on [Streamlit Cloud](https://share.streamlit.io). It is available under https://dummy-lyrics-generator.streamlit.app/. Note that in order to access it, you need a OpenAI account and API key.

## Parameters

The parameters are input in the respective widgets of the web app. More detailed explanations are given there.

topic : `str`
    topic of the song to generate lyrics for

genre : `str`
    genre of the song

specify_decade : `bool`
    if `True`, the lyrics will imitate lyrics of the specified decade

decade : `int`, `1700` to `2300`
    the decade to imitate lyrics of; applies only if `specify_decade` is `True`


## Acknowledgements

I'd like to thank Marie Hinrichs and Prof. Dr. Erhard Hinrichs (both: Seminar für Sprachwissenschaft, Eberhard Karls Universität Tübingen) for giving me an opportunity to share my knowledge and skills as a tutor at the Statistical Language Processing II course in the SoSe23. That was a great chance to both sharpen my competencies and offer them to the students. In process of creating and evaluating labs and assignments, I kept opening new things which definitely gave me new insight in the area and enriched my background.
