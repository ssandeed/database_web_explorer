import os
import sys
import datetime
import unittest
import pandas as pd

from unittest import mock
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.serie_numeric.logics import NumericColumn
from src.database.logics import PostgresConnector


@mock.patch('src.database.logics.PostgresConnector')
class TestInstantiation(unittest.TestCase):
    def test_instantiation(self, test_db):
        db = test_db
        serie = test_db.load_table("public", "orders")["order_id"]

        data_serie = NumericColumn("public", "orders", "order_id", db, serie)
        self.assertEqual(data_serie.schema_name, "public")
        self.assertEqual(data_serie.table_name, "orders")
        self.assertEqual(data_serie.db, db)
        self.assertEqual(data_serie.serie, serie)


@mock.patch('src.serie_date.logics.NumericColumn.is_serie_none')
class TestIfNone(unittest.TestCase):
    def test_IfNullReturnFalse(self, none):
        serie = NumericColumn(None, None, None, None, None)
        result = serie.is_serie_none()
        expect = False
        self.assertEqual(result, expect)


#class TestSetUnique(unittest.TestCase):
    def setUp(self):
        check = pd.Series([1, 2, 3, 4, 5, 5, 7, 7], name="serie1")
        self.serie = NumericColumn(None, None, None, None, check)
        

    def test_unique(self):
        self.serie.set_unique()
        result = self.serie.n_unique
        expect = 6
        self.assertEqual(result, expect)



@mock.patch('src.database.logics.PostgresConnector.run_query')
class TestSetUnique(unittest.TestCase):
    def setUp(self):
        self.serie = NumericColumn(None, None, None, None, None)
        self.serie.db = PostgresConnector(None, None, None, None)

    def setUp(self,mock_run):
        mock_run.return_value = pd.DataFrame([2, 3], columns=["count"])
        self.serie.set_unique()
        result = self.serie.n_unique
        expect = 2
        self.assertEqual(result, expect)



class TestSetStd(unittest.TestCase):
    def setUp(self):
        check = pd.Series([1, 2, 3, 4, 5, 6, 7], name="serie")
        self.serie = NumericColumn(None, None, None, None, check)
        
        

    def test_STD(self):
        
        expect = 2
        self.assertEqual(self.serie.set_std(), expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
