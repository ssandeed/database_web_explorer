from src import database
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_text.queries import get_missing_query, get_mode_query, get_alpha_query


class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> col_name (str): Name of the column (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (mandatory)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> n_empty (int): Number of times a serie has empty value (optional)
    -> n_mode (int): Mode value of a serie (optional)
    -> n_space (int): Number of times a serie has only space characters (optional)
    -> n_lower (int): Number of times a serie has only lowercase characters (optional)
    -> n_upper (int): Number of times a serie has only uppercase characters (optional)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (optional)
    -> n_digit (int): Number of times a serie has only digit characters (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """

    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.n_unique = None
        self.n_missing = None
        self.n_empty = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = None
        self.frequent = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Text section of Streamlit app 

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code

        --------------------


        --------------------
        Returns

        --------------------

        """

        self.set_unique()
        self.set_missing()
        self.set_empty()
        self.set_mode()
        self.set_whitespace()
        self.set_lowercase()
        self.set_uppercase()
        self.set_alphabet()
        self.set_digit()
        self.set_barchart()
        self.set_frequent()

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code
        --------------------


        --------------------
        Returns

        --------------------

        """

        count_null = pd.isnull(self.serie).sum()
        if self.df.empty:
            print(f'The serie is empty')
        elif count_null != 0:
            print(f"The serie has {count_null} null.")
        else:
            return False

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        create an object containing number of unique values in the dataframe
        then return the result of the object showing the number of unique values in the dataframe

        --------------------
        Returns
        --------------------
        int: the number of unique values

        """
        self.n_unique = self.serie.nunique()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie using a SQL query (get_missing_query())

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code
        --------------------

        --------------------
        Returns


        --------------------

        """

        query = get_missing_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.n_missing = df.iloc[0]['count']

    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------

        --------------------
        Returns


        --------------------

        """

        self.n_empty = self.serie.isnull().sum()

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie using a SQL query (get_mode_query())

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code


        --------------------
        Returns


        --------------------


        """

        query = get_mode_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.n_mode = df.iloc[0]['mode']

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code
        --------------------

        --------------------
        Returns


        --------------------
        """

        cnt = 0
        for a in self.serie:
            if a is not None:
                if a.isspace():
                    cnt += 1
                else:
                    cnt += 0
        self.n_space = cnt

    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters

        --------------------
        Parameters
        --------------------

        --------------------
        Pseudo-Code
        --------------------

        --------------------
        Returns

        --------------------
        """
        lt = []
        for i in self.serie:
            if i is np.NaN:
                None
            else:
                if i.isalpha():
                    lt.append(i)
        final = pd.Series(lt)

        if final.empty:
            cnt = 0
        else:
            cnt = sum(final.str.islower().fillna(False))

        self.n_lower = cnt


    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------


        --------------------
        Returns

        --------------------

        """

        lt = []
        for i in self.serie:
            if i is np.NaN:
                None
            else:
                if i.isalpha():
                    lt.append(i)
        final = pd.Series(lt)

        if final.empty:
            cnt = 0
        else:
            cnt = sum(final.str.isupper().fillna(False))

        self.n_upper = cnt

    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters using a SQL query (get_alpha_query())

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code


        --------------------
        Returns

        --------------------

        """

        query = get_alpha_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.n_alpha = df.iloc[0]['count']

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code


        --------------------
        Returns

        --------------------


        """
        cnt = 0
        try:
            for a in self.serie:
                if a.isdigit():
                    cnt += 1
        except:
            cnt += 0

        self.n_digit = cnt

    def set_barchart(self):
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------


        --------------------
        Pseudo-Code

        

        --------------------
        Returns
        --------------------

        """

        value = self.serie.value_counts()
        df = pd.DataFrame(value)
        df = df.reset_index()
        self.barchart = alt.Chart(df).mark_bar().encode(
            x=alt.X('index', title=f'{self.col_name}'),
            y=alt.Y(f'{self.col_name}', title='Number of Occurrences')
        )

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------

        --------------------
        Pseudo-Code
        --------------------
         


        --------------------
        Returns

        --------------------

        """

        value = self.serie.value_counts()
        df = pd.DataFrame(value)
        df = df.reset_index()
        df.columns = ['Value', 'occurrence']
        for i in range(len(df.occurrence)):
            df.loc[i, 'Percentage'] = df.loc[i, 'occurrence'] / sum(df.occurrence)
        df = df.head(end)
        self.frequent = df

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters

        --------------------
        Pseudo-Code


        --------------------
        Returns
        --------------------

        """

        data = [['Number of Unique Values', self.n_unique],
                ['Number of Rows with Missing Values', self.n_missing],
                ['Number of Empty Rows', self.n_empty],
                ['Number of Rows with Only Whitespaces', self.n_space],
                ['Number of Rows with Only Lowercases', self.n_lower],
                ['Number of Rows with Only Uppercases', self.n_upper],
                ['Number of Rows with Only alphabet', self.n_alpha],
                ['Number of Rows with Only digits', self.n_digit]]

        summary = pd.DataFrame(data, columns=['Description', 'Value'])

        return summary.astype(str)
