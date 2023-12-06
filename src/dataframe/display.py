import streamlit as st
from src.dataframe.logics import Dataset


def read_data():
    """
    --------------------
    Description
    --------------------
    -> read_data (function): Function that loads the content of the Postgres table selected, extract its schema information and instantiate a Dataset class accordingly

    --------------------
    Parameters
    --------------------
    -> No parameters

    --------------------
    Pseudo-Code
    --------------------
    -> Variables to store session_state value
    -> Create dataset class
    -> Store dataset in session_state

    --------------------
    Returns
    --------------------
    -> None
    
    """
    database = st.session_state.db
    ses = st.session_state

    schema = ses.schema_selected
    table = ses.table_selected

    load_table = database.load_table(schema, table)
    ses.data = Dataset(schema, table, database, load_table)

def display_overall():
    """
    --------------------
    Description
    --------------------
    -> display_overall (function): Function that displays all the information on the Overall section of the streamlit app

    --------------------
    Parameters
    --------------------
    -> No parameters

    --------------------
    Pseudo-Code
    --------------------
    -> Calling set_data method
    -> Creating header for overall information table
    -> Call get_summary_df
    -> Display overall information
    -> Creating header for table schema
    -> Call get_table_schema and display schemas

    --------------------
    Returns
    --------------------
    -> None

    """
    database = st.session_state.db
    ses = st.session_state

    ses.data.set_data()

    st.subheader("Overall Information")
    st.table(st.session_state.data.get_summary_df())

    st.subheader("Table Schema:")
    st.dataframe(database.get_table_schema(ses.schema_selected, ses.table_selected))

def display_dataframes():
    """
    --------------------
    Description
    --------------------
    -> display_dataframes (function): Function that displays all the information on the Explore section of the streamlit app

    --------------------
    Parameters
    --------------------
    -> No parameters

    --------------------
    Pseudo-Code
    --------------------
    -> Create title for explore part of the app
    -> Create slider and then radio button
    -> Display head, tail or sample data according to user selections
    
    --------------------
    Returns
    --------------------
    -> None

    """
    ses = st.session_state

    st.subheader('Explore Dataframe')
    num_row = st.slider('Select the number of rows to be displayed', 5, 50)
    exp_method = st.radio('Exploration Method', ('Head', 'Tail', 'Sample'))


    if exp_method == 'Head':
        try:
            st.write('Top Rows of Selected Table')
            st.dataframe(ses.data.get_head(num_row))
        except:
            st.write('The rows select is out of range')
    elif exp_method == 'Tail':
        try:
            st.write('Bottom Rows of Selected Table')
            st.dataframe(ses.data.get_tail(num_row))
        except:
            st.write('The rows select is out of range')
    else:
        try:
            st.write('Random Sample Rows of Selected Table')
            st.dataframe(ses.data.get_sample(num_row))
        except:
            st.write('The rows selection is out of range')  

    
    

