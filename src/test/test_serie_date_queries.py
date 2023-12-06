import unittest
import pandas as pd
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.serie_date.queries import *


class TestDateQueries(unittest.TestCase):
    def test_min_date(self):
        self.schema_name = 'public'
        self.table_name = 'orders'
        self.col_name = 'order_date'

        result = get_min_date_query('test', 'test', 'test')
        expect = f"SELECT MIN({self.col_name}) as min_date FROM {self.schema_name}.{self.table_name}"
        self.assertEqual(result, expect)

    def test_weekend_count(self):
        self.schema_name = 'public'
        self.table_name = 'orders'
        self.col_name = 'order_date'

        result = get_weekend_count_query('test', 'test', 'test')
        expect = f"SELECT COUNT({self.col_name}) FROM {self.schema_name}.{self.table_name} WHERE EXTRACT(ISODOW FROM {self.col_name}) IN (6, 7);"
        self.assertEqual(result, expect)

    def test_1900_count(self):
        self.schema_name = 'public'
        self.table_name = 'orders'
        self.col_name = 'order_date'

        result = get_1900_count_query('test', 'test', 'test')
        expect = f"SELECT COUNT({self.col_name}) FROM {self.schema_name}.{self.table_name} WHERE {self.col_name} = '1900-01-01';"
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
