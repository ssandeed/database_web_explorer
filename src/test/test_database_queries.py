##updata the file "test_database_queries.py" by Shihao Li##

import unittest
import pandas as pd

from queries import *

from logics import PostgresConnector

if __name__ == '__main__':

    postcon=PostgresConnector()
    tablelist=get_tables_list_query(postcon)
    print(tablelist)

    df=get_table_data_query(["customer_id","company_name"],'customers',postcon)
    print(df)

    schemas=get_table_schema_query('customers',postcon)
    print(schemas)
