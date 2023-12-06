def get_tables_list_query():
    """
    --------------------
    Description
    --------------------
    -> get_tables_list_query (method): Function that returns the query used for extracting the list of tables from a Postgres table

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
    ->


    """
    return "SELECT t.table_schema, t.table_name FROM information_schema.tables t WHERE t.table_schema not in (" \
           "'information_schema', 'pg_catalog', 'pgagent') "


def get_table_data_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_table_data_query (method): Function that returns the query used for extracting the content of a Postgres table

    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of selected schema
    -> table_name  (str): Name of selected table

    --------------------
    Pseudo-Code
    --------------------
    ->

    --------------------
    Returns
    --------------------
    ->

    """
    return f"SELECT * FROM {schema_name}.{table_name}";


def get_table_schema_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_table_schema_query (method): Function that returns the query used for extracting the list of columns from a Postgres table and their information

    --------------------
    Parameters
    --------------------
    -> schema_name (str): Name of selected schema
    -> table_name  (str): Name of selected table

    --------------------
    Pseudo-Code
    --------------------
    ->

    --------------------
    Returns
    --------------------
    ->

    """
    return f"SELECT c.table_name, c.column_name, c.data_type, CASE WHEN EXISTS(SELECT 1 FROM " \
           f"INFORMATION_SCHEMA.constraint_column_usage k WHERE c.table_name = k.table_name and k.column_name = " \
           f"c.column_name) THEN TRUE ELSE FALSE END as primary_key, CASE WHEN c.is_nullable = 'YES' THEN TRUE ELSE " \
           f"FALSE END AS is_nullable, c.character_maximum_length, c.numeric_precision FROM " \
           f"INFORMATION_SCHEMA.COLUMNS c WHERE table_schema = '{schema_name}' and table_name = '{table_name}'; "
