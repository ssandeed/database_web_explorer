def get_negative_number_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for 
    computing the number of times a column from a Postgres table has negative values 
    --------------------
   
    --------------------
    Pseudo-Code
    --------------------
    return a form of SQL query with input arguments:schema_name, table_name, col_name, to count the specific input column given condition column is less than 0
    -----------
    
    """
       
    return f"SELECT COUNT({col_name}) as count FROM {schema_name}.{table_name} WHERE {col_name} < 0";



def get_std_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_std_query (method): Function that returns the query used for computing the standard deviation value of
     a column from a Postgres table
   
    --------------------
    Pseudo-Code
    --------------------
    return a form of SQL query with input arguments:schema_name, table_name, col_name, to caculated the standard deviation of the specific input column
    --------------------
    """
 
    return f"SELECT STDDEV({col_name}) FROM {schema_name}.{table_name}";

def get_unique_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_unique_query (method): Function that returns the query used for computing the number of
     unique values of a column from a Postgres table
    --------------------
    Pseudo-Code
    --------------------
    return a form of SQL query with input arguments:schema_name, table_name, col_name, to count the distinct number of rows of the specific in putcolumn
    --------------------
   
    """
    return f"SELECT COUNT(DISTINCT {col_name}) FROM {schema_name}.{table_name}";