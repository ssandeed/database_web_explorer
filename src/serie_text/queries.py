def get_missing_query(schema_name, table_name, col_name):
    """
  
    --------------------
    Description
    --------------------
    -> get_missing_query (method): Function that returns the query used for computing the number of missing values of a column from a Postgres table

    --------------------
    Parameters


    --------------------
    Pseudo-Code


    --------------------
    Returns


    """
    return f"SELECT COUNT({col_name}) FROM {schema_name}.{table_name} WHERE '{col_name}' IS NULL";

 
def get_mode_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_mode_query (method): Function that returns the query used for computing the mode value of a column from a Postgres table

    --------------------
    Parameters

    --------------------
    Pseudo-Code

    --------------------
    Returns

    --------------------

    """
    return f"SELECT MODE() WITHIN GROUP (ORDER BY {col_name}) FROM {schema_name}.{table_name}";

def get_alpha_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_alpha_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has only alphabetical characters

    --------------------
    Parameters

    --------------------
    Pseudo-Code

    --------------------
    Returns

    --------------------

    """

    return f"SELECT COUNT({col_name}) FROM {schema_name}.{table_name} WHERE {col_name} ~* '[A-Z]'"
