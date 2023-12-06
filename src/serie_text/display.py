import streamlit as st

from src.serie_text.logics import TextColumn

def display_texts():
    """
    --------------------
    Description
    --------------------
    -> display_texts (function): Function that displays all the relevant information for every text column of a table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """
    ses = st.session_state
    text = ses.data
    text.set_text_columns()
    text_cols = text.text_cols

    if text_cols is not None:
        for col in text_cols:
            with st.expander(col, expanded=False):
                display_text(col, None) 


def display_text(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_text (function): Function that instantiates a TextColumn class from a dataframe column and displays all the relevant information for a single text column of a table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """
    ses = st.session_state
    txt_column = TextColumn(ses.schema_selected, ses.table_selected, col_name, ses.db, ses.data.df[col_name])
    txt_column.set_data()

    st.text('Text Column Summary')
    st.table(txt_column.get_summary_df())

    st.text('Bar Chart')
    st.altair_chart(txt_column.barchart)

    st.text('Most Frequent Values')
    st.dataframe(txt_column.frequent)


