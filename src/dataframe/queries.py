def get_numeric_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_numeric_tables_query (method): Function that returns the query used for extracting the list of numeric columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to select the numeric column names

    --------------------
    Returns
    --------------------
    -> A query which can extract the numeric column names in the database

    """
    numeric_query = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema = '{schema_name}' AND " \
                    f"table_name = '{table_name}' AND c.data_type in ('smallint', 'integer', 'bigint', 'decimal', " \
                    f"'numeric', 'real', 'double precision', 'smallserial', 'serial', 'bigserial', 'money') AND " \
                    f"c.table_schema not in ('information_schema', 'pg_catalog'); "
    return numeric_query

def get_text_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_text_tables_query (method): Function that returns the query used for extracting the list of text columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to select the text column names

    --------------------
    Returns
    --------------------
    -> A query which can extract the text column names in the database

    """
    text_query = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema = '{schema_name}' AND " \
                 f"table_name = '{table_name}' AND c.data_type in ('character','character varying','varchar','char'," \
                 f"'text') AND c.table_schema not in ('information_schema', 'pg_catalog'); "
    return text_query

def get_date_tables_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_date_tables_query (method): Function that returns the query used for extracting the list of datetime columns from a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name(str): Schema name of the selected table in the database
    -> table_name(str): Table name of the selected table in the database

    --------------------
    Pseudo-Code
    --------------------
    -> Get SQL query to select the date column names

    --------------------
    Returns
    --------------------
    -> A query which can extract the date column names in the database

    """
    date_query = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema ='{schema_name}' AND " \
                 f"table_name = '{table_name}' AND c.data_type in ('date','timestamp','time','interval', " \
                 f"'timestampz', 'timetz') AND c.table_schema not in ('information_schema', 'pg_catalog'); "
    return date_query
