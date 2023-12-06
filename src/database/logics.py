import psycopg2
import pandas as pd

from src.database.queries import get_tables_list_query, get_table_data_query, get_table_schema_query

class PostgresConnector:
    """
    --------------------
    Description
    --------------------
    -> PostgresConnector (class): Class that manages the connection to a Postgres database

    --------------------
    Attributes
    --------------------
    -> database (str): Name of Postgres database (mandatory)
    -> user (str): Username used for connecting to Postgres database (mandatory)
    -> password (str): Password used for connecting to Postgres database (mandatory)
    -> host (str): URL of Postgres database (mandatory)
    -> port (str): Port number of Postgres database (mandatory)
    -> conn (psycopg2._psycopg.connection): Postgres connection object (optional)
    -> cursor (psycopg2._psycopg.connection.cursor): Postgres cursor for executing query (optional)
    -> excluded_schemas (list): List containing the names of internal Postgres schemas to be excluded from selection (information_schema, pg_catalog)
    """

    def __init__(self, database="postgres", user='postgres', password='password', host='127.0.0.1', port='5432'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None
        self.excluded_schemas = ['information_schema', 'pg_catalog', 'pgagent']

    def open_connection(self):
        """
        --------------------
        Description
        --------------------
        -> open_connection (method): Class method that creates an active connection to a Postgres database

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
        if self.conn is not None:
            self.close_connection()
        try:
            self.conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )

        except psycopg2.OperationalError as e:
            output = {'status': False, 'msg': f"Connection to server at {self.host}, port {self.port} failed: {e}"}
            return output
        else:
            output = {'status': True, 'msg': 'Connection to database established'}
            return output

    def close_connection(self):
        """
        --------------------
        Description
        --------------------
        -> close_connection (method): Class method that closes an active connection to a Postgres database

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
        self.conn.close()

    def open_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> open_cursor (method): Class method that creates an active cursor to a Postgres database 

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
        self.cursor = self.conn.cursor()

    def close_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> close_cursor (method): Class method that closes an active cursor to a Postgres database 

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
        self.cursor.close()

    def run_query(self, sql_query):
        """
        --------------------
        Description
        --------------------
        -> run_query (method): Class method that executes a SQL query and returns the result as a Pandas dataframe

        --------------------
        Parameters
        --------------------
        -> sql_query (str): The sql command that will be executed.

        --------------------
        Pseudo-Code
        --------------------
        ->

        --------------------
        Returns
        --------------------
        ->

        """
        try:
            self.open_cursor()
            self.cursor.execute(sql_query)
        except psycopg2.OperationalError as e:
            self.close_cursor()
            result = pd.DataFrame([], columns=[])
            return result
        else:
            output = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            self.close_cursor()
            result = pd.DataFrame(output, columns=columns)
            return result

    def list_tables(self):
        """
        --------------------
        Description
        --------------------
        -> list_tables (method): Class method that extracts the list of available tables using a SQL query (get_tables_list_query())

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
        query = get_tables_list_query()
        df = self.run_query(query)
        return df

    def load_table(self, schema_name, table_name):
        """
        --------------------
        Description
        --------------------
        -> load_table (method): Class method that load the content of a table using a SQL query (get_table_data_query())

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

        query = get_table_data_query(schema_name, table_name)
        df = self.run_query(query)
        return df

    def get_table_schema(self, schema_name, table_name):
        """
        --------------------
        Description
        --------------------
        -> get_table_schema (method): Class method that extracts the schema information of a table using a SQL query (get_table_schema_query())

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

        query = get_table_schema_query(schema_name, table_name)
        df = self.run_query(query)
        return df
