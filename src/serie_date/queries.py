
def get_min_date_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_min_date_query (method): Function that returns the query used for computing the earliest date of a datetime column from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database
    -> col_name(str): Column name of the selected column in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to find minimun date from a date column

    --------------------
    Returns
    --------------------
    -> A query which can extract the numeric column names in the database

    """
    query = f"SELECT MIN({col_name}) as min_date FROM {schema_name}.{table_name}"
    return query

def get_weekend_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_weekend_count_query (method): Function that returns the query used for computing the number of times a date of a datetime column falls during weekends

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database
    -> col_name(str): Column name of the selected column in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to count weekend date from a date column

    --------------------
    Returns
    --------------------
    -> A query which can extract the count of weekend dates in a date column

    """
    query = f"SELECT COUNT({col_name}) FROM {schema_name}.{table_name} WHERE EXTRACT(ISODOW FROM {col_name}) IN (6, 7);"
    return query

def get_1900_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_1900_count_query (method): Function that returns the query used for computing the number of times a datetime column has the value '1900-01-01'

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database
    -> col_name(str): Column name of the selected column in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to get date which is equal to '1900-01-01'

    --------------------
    Returns
    --------------------
    -> A query which can extract the count of '1900-01-01' dates in a date column

    """
    query = f"SELECT COUNT({col_name}) FROM {schema_name}.{table_name} WHERE {col_name} = '1900-01-01';"
    return query
