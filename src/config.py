import os
import streamlit as st


def set_app_config():
    """
    --------------------
    Description
    --------------------
    -> set_app_config (function): Function that sets the configuration of the Streamlit app

    --------------------
    Parameters
    -> No parameter

    --------------------
    Pseudo-Code
    ->

    --------------------
    Returns
    -> None

    --------------------

    """
    st.set_page_config(
        page_title="94692 DSP Spring 2022 - AT3: Database Explorer Web App",
        layout="centered",
        menu_items={
            'About': "In this project, Group-14 developed an interactive web application using Streamlit and will "
                     "connect to a Postgres database and perform some exploratory data analysis on selected tables. "
                     "The web application needs to be containerised with Docker and will be running using python "
                     "3.8.2. "
        }
    )


def set_session_state(key, value):
    """
    --------------------
    Description
    --------------------
    -> set_session_state (function): Function that saves a key-value pair to the Streamlit session state

    --------------------
    Parameters
    ->

    --------------------
    Pseudo-Code

    --------------------
    Returns
    -> (None)

    --------------------

    """
    if key not in st.session_state:
        if key == 'db_user':
            st.session_state[key] = os.environ['POSTGRES_USER']
        elif key == 'db_pass':
            st.session_state[key] = os.environ['POSTGRES_PASSWORD']
        elif key == 'db_host':
            st.session_state[key] = os.environ['POSTGRES_HOST']
        elif key == 'db_name':
            st.session_state[key] = os.environ['POSTGRES_DB']
        elif key == 'db_port':
            st.session_state[key] = os.environ['POSTGRES_PORT']
        else:
            st.session_state[key] = value


def set_session_states(keys, value=None):
    """
    --------------------
    Description
    --------------------
    -> set_session_states (function): Function that saves a list of key-value pairs to the Streamlit session state using set_session_state() (default value: None)

    --------------------
    Parameters
    --------------------
    -> value (None): Default value of the session state's keys. 

    --------------------
    Pseudo-Code
    --------------------
    -> Iterate over all keys in session state and set default values to them. 

    --------------------
    Returns
    --------------------
    -> (None)

    """
    for key in keys:
        set_session_state(key, value)


def display_session_state():
    """
    --------------------
    Description
    --------------------
    -> display_session_state (function): Function that displays the current values of Streamlit session state

    --------------------
    Parameters
    --------------------
    No parameter

    --------------------
    Pseudo-Code
    ->

    --------------------
    Returns
    --------------------
    -> None

    """
    st.write(st.session_state)
