import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_date.queries import get_min_date_query, get_weekend_count_query, get_1900_count_query

class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column loaded from Postgres

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
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """

    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.col_max = None
        self.col_min = None
        self.n_unique = None
        self.n_missing = None
        self.n_weekday = None
        self.n_weekend = None
        self.n_empty_1900 = None
        self.n_empty_1970 = None
        self.n_future = None
        self.frequent = None
        self.barchart = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

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
        self.set_unique()
        self.set_missing()
        self.set_min()
        self.set_max()
        self.set_weekend()
        self.set_weekday()
        self.set_future()
        self.set_empty_1900()
        self.set_empty_1970()
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
        -> No parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Computes null values in the dataframe
        -> Checks if dataframe is empty or not
        -> Display if the number of null values in the dataframe is not 0
        -> If none of them, then return False

        --------------------
        Returns
        --------------------
        -> (str): Display information
        -> (boolean): Check if Dataframe is neither empty or has null

        """

        count = pd.isnull(self.serie).sum()
        if self.df.empty:
            print("Serie is empty")
        elif count != 0:
            print(f"Serie has {count} null")
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
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> With n_unique method of pandas serie, sets the attribute

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_unique = self.serie.nunique()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Computes the number of missing values in panda serie and store in attribute

        --------------------
        Returns
        --------------------
        -> None


        """
        self.n_missing = pd.isnull(self.serie).sum()

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie using a SQL query (get_min_date_query())

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Run sql query to retrieve the minimum value in the serie
        -> Store the value in a new variable
        -> Convert the minimum value in the column to datetime type and set the relevant attribute

        --------------------
        Returns
        -> None

        """
        col_min = self.db.run_query(get_min_date_query(self.schema_name, self.table_name, self.col_name)).iloc[0]['min_date']
        self.col_min = pd.to_datetime(col_min)

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Max function to get the maximum value in that data.serie and set the relevant attribute

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_max = max(self.serie)

    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend using a SQL query (get_weekend_count_query())

        --------------------
        Parameters
        --------------------
        -> No Parameters


        --------------------
        Pseudo-Code
        --------------------
        -> Run sql query to get weekend count in the database class
        -> Get the value of the dataframe result
        -> Set the attribute

        --------------------
        Returns
        --------------------
        -> None

        """
        schema_name = self.schema_name
        table_name = self.table_name
        col_name = self.col_name
        query = get_weekend_count_query(schema_name, table_name,col_name)
        serie_weekend = self.db.run_query(query)
        self.n_weekend = serie_weekend.iloc[0]['count']

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend

        --------------------
        Parameters
        --------------------
        -> No Parameters
        
        --------------------
        Pseudo-Code
        --------------------
        -> Weekday count = length of the serie - the number of weekend

        --------------------
        Returns
        --------------------
        -> None
        
        """
        count_day = len(self.serie)
        self.n_weekday = count_day - self.n_weekend

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Filter out the dates larger than today and set the attribute

        --------------------
        Returns
        --------------------
        -> None

        """
        d_series = self.serie
        df = d_series[d_series > pd.to_datetime("today")]
        self.n_future = df.size

    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' using a SQL query (get_1900_count_query())

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Run sql query to get date with 1900 year count in the database class
        -> Get the value of the dataframe result
        -> Set the attribute value
        
        --------------------
        Returns
        --------------------
        -> None

        """
        schema_name = self.schema_name
        table_name = self.table_name
        col_name = self.col_name
        query = get_1900_count_query(schema_name, table_name, col_name)
        serie_1900 = self.db.run_query(query)
        self.n_empty_1900 = serie_1900.size

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has dates equal to '1970-01-01'

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Filter out the serie that has a date value equals to 1970-01-01
        -> Count the rows of the serie
        -> Set the attribute value

        --------------------
        Returns
        --------------------
        -> None

        """
        d_series = self.serie
        df = d_series[d_series == pd.Timestamp(1970, 1, 1)]
        self.n_empty_1970 = df.size

    def set_barchart(self):
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        -> No Parameters

        --------------------
        Pseudo-Code
        --------------------
        -> Store the count of unique values in the serie
        -> Reset the index for easy plot
        -> Plot a bar chart and set the attribute value

        --------------------
        Returns
        --------------------
        -> None

        """

        df_serie = self.serie.value_counts()
        df = df_serie.reset_index()
        print(df)
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
        end(int): The number of dataframe rows that user wants to inspect 

        --------------------
        Pseudo-Code
        --------------------
        -> Dataframe is created with value_counts method and index is reset
        -> Column names are created
        -> For each value occurrence,their proportionate value is computed
        -> Computed Values are store in as df

        --------------------
        Returns
        --------------------
        -> None

        """
        df = pd.DataFrame(self.serie.value_counts())
        df = df.reset_index()
        df.columns = ['value', 'occurrence']
        for i in range(len(df.occurrence)):
            df.loc[i,'percentage'] = df.loc[i,'occurrence']/sum(df.occurrence)
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
        None 
        --------------------
        Pseudo-Code
        --------------------
        -> pd.Dataframe is created and following information is displayed
        -> Dataframe values are converted into strings

        --------------------
        Returns
        --------------------
        -> summary (pd.Dataframe): It shows all the requested information in string format

        """
        data = [["Name of Unique Values", self.n_unique],
                ["Number of Rows with Missing Values", self.n_missing],
                ["Number of Weekend Dates", self.n_weekend],
                ["Number of Weekday Dates", self.n_weekday],
                ["Number of Dates in Future", self.n_future],
                ["Number of rows with 1900-01-01", self.n_empty_1900],
                ["Number of rows with 1970-01-01", self.n_empty_1970],
                ["Minimum Value", self.col_min],
                ["Maximum Value", self.col_max]]

        summary = pd.DataFrame(data, columns=['Description', 'Value'])

        return summary.astype(str)
