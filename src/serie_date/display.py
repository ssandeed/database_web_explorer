import streamlit as st

from src.serie_date.logics import DateColumn


def display_dates():
    """
    --------------------
    Description
    --------------------
    -> display_dates (function): Function that displays all the relevant information for every datetime column of a table

    --------------------
    Parameters
    --------------------
    -> No Parameters

    --------------------
    Pseudo-Code
    --------------------
    -> Variables to store session_state value
    -> Store dataset in session_state
    -> Call set_date_columns method to set attributes values
    -> Create a variable to store the column names
    -> Set expanders for each column and display the relevant information

    --------------------
    Returns
    --------------------
    -> None

    """
    dt = st.session_state.data
    dt.set_date_columns()
    date_cols = dt.date_cols

    if date_cols is not None:
        for column_name in date_cols:
            with st.expander(column_name, expanded=False):
                display_date(column_name, None)

def display_date(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_date (function): Function that instantiates a DateColumn class from a dataframe column and displays all the relevant information for a single datetime column of a table

    --------------------
    Parameters
    --------------------
    -> col_name(str): column name to create the DateColumn class
    -> i(str): redunctant

    --------------------
    Pseudo-Code
    --------------------
    -> Variables to store session_state value
    -> Store dataset in session_state
    -> Call set_date_columns method
    -> Set Date Column Summary title
    -> Call get_summary_df and display table in the streamlit app
    -> Set a bar chart title
    -> Show the barchart using altair package in the streamlit app
    -> Set a title for Most Frequent Values
    -> Call frequent method of the DateColumn class and display it in the streamlit app

    --------------------
    Returns
    --------------------
    None

    """
    session = st.session_state
    date_col = DateColumn(session.schema_selected, session.table_selected, col_name, session.db, session.data.df[col_name])
    date_col.set_data()

    st.text('Date Column Summary')
    st.table(date_col.get_summary_df())

    st.text('Bar Chart')
    st.altair_chart(date_col.barchart)

    st.text('Most Frequent Values')
    st.dataframe(date_col.frequent)
