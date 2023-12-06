import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.dataframe.queries import *


class TestDataframeQueries(unittest.TestCase):

    def test_numeric(self):
        self.schema_name = 'public'
        self.table_name = 'test'

        result = get_numeric_tables_query(self.schema_name, self.table_name)
        expect = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema = '{self.schema_name}' AND " \
                 f"table_name = '{self.table_name}' AND c.data_type in ('smallint', 'integer', 'bigint', 'decimal', " \
                 f"'numeric', 'real', 'double precision', 'smallserial', 'serial', 'bigserial', 'money') AND " \
                 f"c.table_schema not in ('information_schema', 'pg_catalog'); "
        self.assertEqual(result, expect)

    def test_text(self):
        self.schema_name = 'public'
        self.table_name = 'test'

        result = get_text_tables_query(self.schema_name, self.table_name)
        expect = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema = '{self.schema_name}' AND " \
                 f"table_name = '{self.table_name}' AND c.data_type in ('character','character varying','varchar','char'," \
                 f"'text') AND c.table_schema not in ('information_schema', 'pg_catalog'); "
        self.assertEqual(result, expect)

    def test_date(self):
        self.schema_name = 'public'
        self.table_name = 'test'

        result = get_date_tables_query(self.schema_name, self.table_name)
        expect = f"SELECT c.column_name FROM information_schema.columns c WHERE table_schema ='{self.schema_name}' AND " \
                 f"table_name = '{self.table_name}' AND c.data_type in ('date','timestamp','time','interval', " \
                 f"'timestampz', 'timetz') AND c.table_schema not in ('information_schema', 'pg_catalog'); "
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
