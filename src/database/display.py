import streamlit as st

from src.database.logics import PostgresConnector
from src.dataframe.display import read_data


def display_db_connection_menu():
    """
    --------------------
    Description
    --------------------
    -> display_db_connection_menu (function): Function that displays the menu for connecting to a database and triggers the database connection

    --------------------
    Parameters
    --------------------
    No parameter

    --------------------
    Pseudo-Code
    --------------------
    ->

    --------------------
    Returns
    --------------------
    -> None

    """
    st.subheader("Database Connection Details")

    st.text_input(
        'Username:',
        key='db_user',
    )

    st.text_input(
        'Password:',
        key='db_pass',
        type="password"
    )

    st.text_input(
        'Database Host:',
        key='db_host',
    )

    st.text_input(
        'Database Name:',
        key='db_name',
    )

    st.text_input(
        'Database Port:',
        key='db_port',
    )
    if st.button("Connect"):
        connect_db()
        st.experimental_rerun()

    if st.session_state.msg is not None:
        if st.session_state.db_status:
            st.success(st.session_state.msg)
        else:
            st.error(st.session_state.msg)


def connect_db():
    """
    --------------------
    Description
    --------------------
    -> connect_db (function): Function that connects to a database and instantiate a PostgresConnector class accordingly

    --------------------
    Parameters
    --------------------
    No parameter

    --------------------
    Pseudo-Code
    --------------------
    ->

    --------------------
    Returns
    --------------------
    -> None

    """
    ses = st.session_state
    pgadmin = PostgresConnector(ses.db_name, ses.db_user, ses.db_pass, ses.db_host, ses.db_port)
    output = pgadmin.open_connection()
    ses.msg = output['msg']
    ses.db_status = output['status']
    ses.db = pgadmin
    ses.data = None


def display_table_selection():
    """
    --------------------
    Description
    --------------------
    -> display_table_selection (function): Function that displays the selection box for selecting the table to be analysed and triggers the loading of data (read_data())

    --------------------
    Parameters
    --------------------
    No parameter

    --------------------
    Pseudo-Code
    --------------------


    --------------------
    Returns
    --------------------
    -> None

    """
    database = st.session_state.db
    schemas_tables = database.list_tables()
    new_col = schemas_tables.apply(lambda row: str(row["table_schema"]) + "." + str(row["table_name"]), axis=1)
    st.selectbox('Select a table name', new_col, key='schema_table_selected', on_change=select_schema_table)


def select_schema_table():
    ses = st.session_state
    schema_table = ses.schema_table_selected.split('.')
    ses.schema_selected = schema_table[0]
    ses.table_selected = schema_table[1]
    read_data()
