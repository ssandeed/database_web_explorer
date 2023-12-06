
import streamlit as st
import pandas as pd
import altair as alt
from src.database.logics import PostgresConnector
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column loaded from Postgres

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
    -> col_mean (int): Average value of a serie (optional)
    -> col_std (int): Standard deviation value of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> col_median (int): Median value of a serie (optional)
    -> n_zeros (int): Number of times a serie has values equal to 0 (optional)
    -> n_negatives (int): Number of times a serie has negative values (optional)
    -> histogram (int): Altair histogram displaying the count for each bin value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name, table_name, col_name ,db , serie):
        self.schema_name=schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = None
        self.frequent = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information
         from self.serie to be displayed in the Numeric section of Streamlit app 
        --------------------
        Pseudo-Code
        --------------------
        if the return of self.is_serie_none() is equal to True, apply the methods below
            self.set_unique()   
            self.set_missing()
            self.set_zeros()
            self.set_negatives()
            self.set_mean()
            self.set_std()
            self.set_min()
            self.set_max()
            self.set_median()
            self.set_histogram()
            self.set_frequent()
        else
            print The serie has x null
        --------------------

        """
        if self.is_serie_none() == True:
            self.set_unique()   
            self.set_missing()
            self.set_zeros()
            self.set_negatives()
            self.set_mean()
            self.set_std()
            self.set_min()
            self.set_max()
            self.set_median()
            self.set_histogram()
            self.set_frequent()
        else :
            print(f"The serie has {self.count_null} null.")
 

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

       

        --------------------
        Pseudo-Code
        --------------------
        apply pd.isnull() with argument:self.serie, and apply sum() for the return. Save the final return as a new class attribute names self.count_null

        if self.count_null is equal to 0
            then return True

      

        """

        self.count_null = pd.isnull(self.serie).sum()
        if self.count_null == 0:
            return True
        else:
            return False
        

     

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column using a SQL query (get_unique_query())
        --------------------
        Pseudo-Code
        --------------------
        apply get_unique_query() with input arguments:self.schema_name, self.table_name, self.col_name, to get a query for number of distinct values of the column.  Save the query as a variable names query
        
        apply self.db.run_query with input argument query to get the result and save the return as variable names "df"
        
        replace the value of self.n_unique with df
        --------------------
      
        """
        query = get_unique_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.n_unique = df.iloc[0]['count']


    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie
        --------------------
        Pseudo-Code
        --------------------
        apply pd.isnull() with argument self.serie and return the list with all the Null values. Save the return as a variable names df
        
        apply appling sum() to df and get the return of sum of the number of Null values, and replace the self.n_missing with the return
        --------------------
       

        """
        df = pd.isnull(self.serie)
        self.n_missing = df.sum()

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0
        --------------------
        Pseudo-Code
        --------------------
        
        apply sum() with condition when self.serie is equal to 0, get the return to replace the self.n_missing with the return

        
        """
        self.n_zeros = (self.serie == 0).sum()

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values using a SQL query (get_negative_number_query())
        --------------------
        Pseudo-Code
        --------------------
        apply get_unique_query() with input arguments:self.schema_name, self.table_name, self.col_name, to get a query for number of negative values of the column.  Save the query as a variable names query
        
        apply self.db.run_query with input argument query to get the result and save the return as variable names "df"
        
        replace the value of self.n_negative with df

        """
        query = get_negative_number_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.n_negatives = df.iloc[0]['count']

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie
        --------------------
        Pseudo-Code
        --------------------
        apply mean() to self.serie to get a average and round up the return into 2 digits. Replace self.col_mean with the final return

        --------------------
       
        """

        self.col_mean = round(self.serie.mean(),2)

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie using a SQL query (get_std_query)
        --------------------
        Pseudo-Code
        --------------------
        apply get_unique_query() with input arguments:self.schema_name, self.table_name, self.col_name, to get a query for caculate the standard deviation of the column.  Save the query as a variable names query
        
        apply self.db.run_query with input argument query to get the result and save the return as variable names "df"
        
        replace the value of self.col_std with rounding up 2 digits of df

        """
        query = get_std_query(self.schema_name, self.table_name, self.col_name)
        df = self.db.run_query(query)
        self.col_std = round(df.iloc[0]['stddev'],2)
    
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie
        --------------------
        Pseudo-Code
        --------------------
        apply min() to self.serie to get a minimum value. Replace self.col_min with the return

    
        """

        self.col_min = min(self.serie)

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie
        --------------------
        Pseudo-Code
        --------------------
        apply max() to self.serie to get a minimum value. Replace self.col_max with the return
        --------------------
      
        """

        self.col_max = max(self.serie)

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie
        --------------------
        Pseudo-Code
        --------------------
        apply median() to self.serie to get a median and round up the return into 2 digits. Replace self.col_median with the final return

        
        """

        self.col_median = round(self.serie.median(),2)

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie
        --------------------
        Pseudo-Code
        --------------------
        call pd.DataFrame() with argument:self.serie.value_counts() to extract the column/list into a pd.datafram type. Save the return as varibale df
        
        reset the index of the column/list from df

        call alt.Chart(df).mark_bar().encode with arguments :
            x = alt.X('index', 
            title =f'{self.col_name}'),
            y = alt.Y(f'{self.col_name}', 
            title = f'Count of {self.col_name}')).transform_bin(f'{self.col_name}', 
            field = f'{self.col_name}', bin = alt.Bin(maxbins=50),
        to display a histogram chart. Replace self.histogram with the return

        --------------------
        

        """

        df = pd.DataFrame(self.serie.value_counts())
        df.reset_index(inplace = True)
        self.histogram = alt.Chart(df).mark_bar().encode(
            x = alt.X('index', title =f'{self.col_name}'),
            y = alt.Y(f'{self.col_name}', title = f'Count of {self.col_name}')).transform_bin(f'{self.col_name}', field = f'{self.col_name}', bin = alt.Bin(maxbins=50))

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie
        --------------------
        Parameters
        --------------------
        end(int) : number of the rows to display 
        --------------------
        Pseudo-Code
        --------------------
        Apply pd.DataFrame().astype with input argument:self.serie.value_counts().head(end) and int, to extract the column/list into a pandas.datafram type with head 20 rows. Save the return as a variable name fre
        
        Reset the index of the column/list from df

        Given rename the column name for fre with "value" and "occurence" 

        Create a new column to fre by given define : new column "percentage" = column "occurence" divided by sum of column "occurence"

        Refresh self.frequent with fre

        return self.frequent

        
        """
        
        fre = pd.DataFrame(self.serie.value_counts().head(end)).astype(int)
        fre.reset_index(inplace = True)
        fre.columns = ['value','occurence']
        
        fre["percentage"] = fre["occurence"] / sum(fre["occurence"])

        self.frequent = fre
        return self.frequent 

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

    
        --------------------
        Pseudo-Code
        --------------------
        Form a table as given keys and values, which values are call from the attributes of class NumericColumn and Save as a variable names summary
        
        Apply pd.DataFrame() to convert the summry as the type of pandas.dataframe and save as variable names summary_df
        
        return summary_df



        --------------------
        

        """
        
        summary = {'Description': ['number of unique values', 'number of missing values','number of occurrence of 0 value','number of negative values','the average value','the standard deviation value','the minimum value','the maximum value','the median value'], 
        'Value': [self.n_unique, self.n_missing,self.n_zeros,self.n_negatives,self.col_mean,self.col_std,self.col_min,self.col_max,self.col_median]}
        summary_df = pd.DataFrame(data=summary).astype(str)
        return summary_df