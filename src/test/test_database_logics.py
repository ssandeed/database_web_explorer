##update of file “test_database_logics.py” by Shihao Li##

import unittest
import pandas as pd

from logics import PostgresConnector


if __name__ == '__main__':
    a=PostgresConnector()
    tablist=a.list_tables()
    print("1:",tablist)
    result=a.run_query("select * from customers")
    print("2:",result)
    schemas=a.get_table_schema("customers")
    print("3:",schemas)
    df=a.load_table(["customer_id","company_name"],'customers')
    print(df)
