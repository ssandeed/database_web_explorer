# Database Web Explorer App using Streamlit

## Description
In this project, developed an interactive web application using Streamlit and will connect to a Postgres database and perform some exploratory data analysis on selected tables. The web application needs to be containerised with Docker and will be running using python 3.8.2.

## How to Setup
1.Unzip the file
2.Open the Unix command and use command "cd "the path of the main folder" to relocate the wokring path   

Run by python 3.8.2
  
Packages requirement:
  1. streamlit
  2. pandas
  3. numpy
  4. altair
  5. psycopg2

## How to Run the Program

Clone the repository
  
```bash
git clone git@github.com:ssandeed/dsp_at3_14.git
```
  
1. Open new project with all the supported files in an python IDE
  
2. In the terminal, make sure current directory is the project file directory
  
3. Run **docker build .**  in the terminal to builds Docker images from Dockerfile 
  
4. Lastly run **docker-compose up -d** and compose will start
  
5. To run the app, open any browser and go to **http://localhost:8501/**
  
6. When web app opens, then provide database credentials to access database
  
7. For accessing local machine Postgres Database, Database Host should be: **host.docker.internal**
  
Whenever any change happens in the app/streamlit_app.py, the steamlit application will update too. 

To stop the application the application, either

```bash
docker-compose stop
```

to stop the application, or use 

```bash
docker-compose down --rmi all
```

to stop the application, remove the stopped containers and optionally `--rmi all` / remove all images associated in the docker-compose.yml file.

## Project Structure

```
./
│
├── app/
│   └── streamlit_app.py            <- main script used for displaying the final application in the Docker container
│
├── src/
│   ├── database
│   │   ├── test_data.py            <- python script for testing code from data.py
│   │   ├── test_datetime.py        <- python script for testing code from datetime.py
│   │   ├── test_numeric.py         <- python script for testing code from numeric.py                                   
│   │   └── test_text.py            <- python script for testing code from text.py 
│   │                                   
│   ├── dataframe
│   │   ├── __init__.py             <- turns dataframe folder into a package for importing in main script
│   │   ├── display.py              <- contains the code for displaying the "Overall information" section
│   │   ├── logics.py               <- contains the code for calculation of all dataframe logics                              
│   │   └── query.py                <- contains the code for getting query for numeric, text and date columns                              
│   │
│   ├── serie_date
│   │   ├── __init__.py             <- turns serie_date folder into a package for importing in main script
│   │   ├── display.py              <- contains the code for displaying the Date tab of the app
│   │   ├── logics.py               <- contains the code for calculation of all serie_date logics                              
│   │   └── query.py                <- contains the code for getting query for weekend count, min date and 1900 year count                                
│   │
│   ├── serie_numeric
│   │   ├── __init__.py             <- turns serie_date folder into a package for importing in main script
│   │   ├── display.py              <- contains the code for displaying the numeric tab of the app
│   │   ├── logics.py               <- contains the code for calculation of all serie_numeric logics                              
│   │   └── query.py                <- contains the code for getting query for standard deviation, number of unique values and number of negative values                                 
│   │
│   ├── serie_text
│   │   ├── test_data.py            <- python script for testing code from data.py
│   │   ├── test_datetime.py        <- python script for testing code from datetime.py
│   │   ├── test_numeric.py         <- python script for testing code from numeric.py                                   
│   │   └── test_text.py            <- python script for testing code from text.py  
│   │                                      
│   ├── test
│   │   ├── test_database_logics.py       <- python script for testing code from test_database_logics.py
│   │   ├── test_database_queries.py      <- python script for testing code from test_database_queries.py
│   │   ├── test_dataframe_logics.py      <- python script for testing code from test_dataframe_logics.py
│   │   ├── test_dataframe_queries.py     <- python script for testing code from test_dataframe_queries.py
│   │   ├── test_serie_date_logics.py     <- python script for testing code from test_serie_date_logics.py
│   │   ├── test_serie_date_queries.py    <- python script for testing code from test_serie_date_queries.py
│   │   ├── test_serie_numeric_logics.py  <- python script for testing code from test_serie_numeric_logics.py
│   │   ├── test_serie_numeric_queries.py <- python script for testing code from test_serie_numeric_queries.py
│   │   ├── test_serie_text_logics.py     <- python script for testing code from test_serie_text_logics.py
│   │   ├── test_serie_text_queries.py    <- python script for testing code from test_serie_text_queries.py                               
│   │   └── __init__.py                   <- turns test folder into a package for importing in main script 
│   │                                     
│   ├── __init__.py              <- turns src folder into a package for importing in main script
│   │     
│   └── config.py                <- contains the code for displaying the "Overall information" section
│   
├── .gitignore                   <- avoids unecessary files pushed to the repository
├── Dockerfile                   <- file used to build a Docker image
├── docker-compose.yml           <- a YAML file to configure the application's services
├── README.md                    <- a markdown file containing student details, a description of this project and instructions for running the application
└── requirements.txt             <- a file to specify the versions of all the packages in python needed when running the application

```
                               
## Citations

1. Apply function to every row in a Pandas DataFrame. (2018, December 11). GeeksforGeeks. https://www.geeksforgeeks.org/apply-function-to-every-row-in-a-pandas-dataframe/

2. Count nan or missing values in pandas dataframe. (2020, July 1). GeeksforGeeks. https://www.geeksforgeeks.org/count-nan-or-missing-values-in-pandas-dataframe/

3. Counting number of rows with missing values in Pandas DataFrame. (n.d.). Retrieved October 20, 2022, from https://www.skytowner.com/explore/counting_number_of_rows_with_missing_value_in_pandas_dataframe

4. Find all numeric columns in postgresql database—Postgresql data dictionary queries. (n.d.). Retrieved October 22, 2022, from https://dataedo.com/kb/query/postgresql/find-all-numeric-columns

5. klin. (2018, April 5). Answer to “Include primary key on schema information in Postgres.” Stack Overflow. https://stackoverflow.com/a/49682741

6. Python | Pandas Series.dt.dayofweek. (2019, March 18). GeeksforGeeks. https://www.geeksforgeeks.org/python-pandas-series-dt-dayofweek/

7. Streamlit • The fastest way to build and share data apps. (n.d.). Retrieved November 6, 2022, from https://streamlit.io/

8. Docker documentation. (2022, November 8). Docker Documentation. https://docs.docker.com/




