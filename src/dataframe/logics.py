import pandas as pd
import streamlit as st

from src.database.logics import PostgresConnector
from src.dataframe.queries import get_numeric_tables_query, get_text_tables_query, get_date_tables_query


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> df (pd.Dataframe): Pandas dataframe where the table content has been loaded (mandatory)
    -> n_rows (int): Number of rows of dataset (optional)
    -> n_cols (int): Number of columns of dataset (optional)
    -> n_duplicates (int): Number of duplicated rows of dataset (optional)
    -> n_missing (int): Number of missing values of dataset (optional)
    -> num_cols (list): List of columns of numerical type (optional)
    -> text_cols (list): List of columns of text type (optional)
    -> date_cols (list): List of columns of datetime type (optional)
    """

    def __init__(self, schema_name=None, table_name=None, db=None, df=None):

        self.schema_name = schema_name
        self.table_name = table_name
        self.df = df
        self.db = db
        self.n_duplicates = None
        self.n_missing = None
        self.n_rows = None
        self.n_cols = None
        self.num_cols = None
        self.text_cols = None
        self.date_cols = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Overall section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> No parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Calling of given method of this class to set the attributes values

        --------------------
        Returns
        --------------------
        -> None

        """
        self.set_dimensions()
        self.set_duplicates()
        self.set_missing()
        self.set_numeric_columns()
        self.set_text_columns()
        self.set_date_columns()

    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        -> No parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Check if the dataframe is empty or not, accordingly print the information

        --------------------
        Returns
        --------------------
        "DataFrame is empty!"
        "DataFrame is NOT empty!"

        """

        if self.df.empty:
            return "DataFrame is empty!"
        else:
            return "DataFrame is NOT empty!"

    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df and store them as attributes (self.n_rows, self.n_cols)

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Get count of rows of the dataframe from index 0
        -> Get count of clomuns of the dataframe from index 1

        --------------------
        Returns
        --------------------
        ->None

        """
        dim = self.df.shape
        self.n_rows = dim[0]
        self.n_cols = dim[1]

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store it as attribute (self.n_duplicates)

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Computes the count of the duplicated rows

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_duplicates = self.df.duplicated(keep=False).sum()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store it as attribute (self.n_missing)

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Computes the number of missing values in dataframe and store in attribute

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_missing = self.df.isnull().sum().sum()

    def set_numeric_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric_columns (method): Class method that extract the list of numeric columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.num_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> From query get the numeric column names and set the attribute
        -> Create variable to convert the result dataframe into list
        -> Convert the numeric columns into integer format
        
        --------------------
        Returns
        --------------------
        -> None

        """

        self.num_cols = self.db.run_query(get_numeric_tables_query(self.schema_name, self.table_name))
        iterables = self.num_cols.values.tolist()
        a = []
        for i in iterables:
            for element in i:
                if element is not None:
                    a.append(element)
        self.num_cols = list(a)
        self.df[self.num_cols] = self.df[self.num_cols].fillna(0)
        self.df[self.num_cols] = self.df[self.num_cols].astype('int')

    def set_text_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_text_columns (method): Class method that extract the list of text columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.text_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> From query get the text column names and set the attribute
        -> Create variable to convert the result dataframe into list
        -> Convert the numeric columns into string format

        --------------------
        Returns
        --------------------
        -> None

        """

        self.text_cols = self.db.run_query(get_text_tables_query(self.schema_name, self.table_name))
        iterables = self.text_cols.values.tolist()
        a = []
        for i in iterables:
            for element in i:
                if element is not None:
                    a.append(element)
        self.text_cols = list(a)
        self.df[self.text_cols] = self.df[self.text_cols].fillna(' ')
        self.df[self.text_cols] = self.df[self.text_cols].astype('string')

    def set_date_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_date_columns (method): Class method that extract the list of datetime columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.date_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> From query get the date column names and set the attribute
        -> Create variable to convert the result dataframe into list
        -> Convert the numeric columns into date format

        --------------------
        Returns
        --------------------
        -> None

        """

        self.date_cols = self.db.run_query(get_date_tables_query(self.schema_name, self.table_name))
        iterables = self.date_cols.values.tolist()
        a = []
        for i in iterables:
            for element in i:
                if element is not None:
                    a.append(element)
        self.date_cols = list(a)
        self.df[self.date_cols] = self.df[self.date_cols].fillna(pd.Timestamp(0))
        self.df[self.date_cols] = self.df[self.date_cols].astype('datetime64[ns]')

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        -> n(int): number of rows for user wants to check

        --------------------
        Pseudo-Code
        --------------------
        -> Function to retrieve the first n rows in the dataframe

        --------------------
        Returns
        --------------------
        -> (dataframe): The first n rows of the dataframe

        """
        return self.df.head(n)

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        -> n(int): number of rows for user wants to check

        --------------------
        Pseudo-Code
        --------------------
        -> Function to retrieve the last n rows in the dataframe

        --------------------
        Returns
        --------------------
        -> (dataframe): The last n rows of the dataframe

        """
        return self.df.tail(n)

    def get_sample(self,n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        -> n(int): number of rows for user wants to check

        --------------------
        Pseudo-Code
        --------------------
        -> Function to retrieve the sample n rows in the dataframe

        --------------------
        Returns
        --------------------
        -> (dataframe): The sample n rows of the dataframe

        """
        return self.df.sample(n)

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Create a dataframe to display Overall section of Streamlit app

        --------------------
        Returns
        --------------------
        -> summary (pd.Dataframe): description

        """
        self.set_data()

        dt = {'a': self.table_name,
              'b': self.n_rows,
              'c': self.n_cols,
              'd': self.n_duplicates,
              'e': self.n_missing
              }

        name_list = ["Name of Table", "Number of Rows", "Number of Columns", "Number of Duplicated Rows",
                     "Number of Rows with Missing Values"]
        value_list = []

        for key in dt:
            value_list.append(dt[key])

        data = {"Description": name_list,
                "Value": value_list}
        summary = pd.DataFrame(data)
        return summary
