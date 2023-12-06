import streamlit as st

from src.serie_numeric.logics import NumericColumn

def display_numerics():
    """
    --------------------
    Description
    --------------------
    -> display_numerics (function): Function that displays all the relevant information for every numerical column of a table

    --------------------
    Parameters
    --------------------
    df:extract the data from configuration and restore as a variable names "df"

    col_list:call method set_numeric_columns from class Dataset by variable "df", restore the return and names "col_list"


    --------------------
    Pseudo-Code
    --------------------
    

    if input argument "col_list" is not None
        then try to run coding below
            apply st.selectbox() with input arguments: 'Select numeric columns to display' and col_list, to diplay a select box with the list in "col_list". Save the selected object as a variable names "option".
            apply st.write() with argument: 'You selected:' and option, to diplay a phrase " You selected +  selected column"
            apply display_numeric() with argument: option and None, to display the summary table, histogram chart and frequency table
        if error
            apply st.write() to show a phrase "Numerical columns are not available in this table"
   

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """
    df = st.session_state.data
    df.set_numeric_columns()
    col_list = df.num_cols


    if col_list is not None:
        try:
          
            option = st.selectbox('Select numeric columns to display',col_list)  
            st.write('You selected:', option)
            display_numeric(option, None)
        except :
            
            st.write('Numerical columns are not available in this table')
        

def display_numeric(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_numeric (function): Function that instantiates a NumericColumn class from a dataframe column and displays all the relevant information for a single numerical column of a table

    --------------------
    Parameters
    --------------------
    numeric_column: Instantation of NumericColumn() class with input argument st.session_state.schema_selected, st.session_state.table_selected, col_name, st.session_state.db, st.session_state.data.df[col_name].

    --------------------
    Pseudo-Code
    --------------------
    Apply set_date() by numeric_column to refresh all the attributes of the class NumericColumn()

    Apply st.title() with argument 'Summary', to set up a title for the summary table
    Apply st.table() with argument: apply numeric_column.get_summary_df(), to call the summary table

    Apply st.title() with argument: 'Histogram Chart', to set up a title for the Histogram Chart
    Apply st.table() with argument: numeric_column.histogram, to call the Histogram Chart

    Apply st.title() with argument: 'Most Frequent Values', to set up a title for the Most Frequent Values table
    Apply st.table() with argument: numeric_column.frequent, to call the Most Frequent Values table


    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """
    numeric_column = NumericColumn(st.session_state.schema_selected, st.session_state.table_selected, col_name, st.session_state.db, st.session_state.data.df[col_name])
    numeric_column.set_data()

    st.title('Summary')
    st.table(numeric_column.get_summary_df())
    st.title('Histogram Chart')
    st.altair_chart(numeric_column.histogram)
    st.title('Most Frequent Values')
    st.dataframe(numeric_column.frequent)