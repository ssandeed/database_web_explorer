import streamlit as st

from src.config import set_app_config, set_session_states, display_session_state
from src.database.display import display_db_connection_menu, display_table_selection
from src.dataframe.display import display_overall, display_dataframes
from src.serie_numeric.display import display_numerics
from src.serie_text.display import display_texts
from src.serie_date.display import display_dates


set_session_states(['db', 'db_host', 'db_name', 'db_port', 'db_user', 'db_pass', 'db_status', 'db_infos_df', 'schema_selected', 'table_selected', 'data', 'msg', 'schema_table_selected'])

set_app_config()
st.title("Database Explorer")

# Add Debugger
with st.expander("Streamlit Session State", expanded=False):
    display_session_state()

# Add Menu
with st.expander("ℹ️ - Streamlit application for performing data exploration on a database", expanded=True):
    display_db_connection_menu()

if st.session_state.db_status:
    display_table_selection() 
    
    if st.session_state.data is not None:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overall", "Explore", "Numeric", "Text", "Date"])

        with tab1:
            display_overall()
        with tab2:
            display_dataframes()
        with tab3:
            display_numerics()
        with tab4:
            display_texts()
        with tab5:
            display_dates()
