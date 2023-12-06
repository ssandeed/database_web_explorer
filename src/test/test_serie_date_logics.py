import os
import sys
import datetime
import unittest
import pandas as pd

from unittest import mock
from src.database.logics import PostgresConnector
from src.serie_date.logics import DateColumn

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))


@mock.patch('src.database.logics.PostgresConnector')
class TestInstantiation(unittest.TestCase):
    def test_instantiation(self, test_db):
        schema_name = "public"
        table_name = "orders"
        col_name = "order_id"
        db = test_db
        serie = test_db.load_table(schema_name, table_name)[col_name]

        data_serie = DateColumn(schema_name, table_name, col_name, db, serie)
        self.assertEqual(data_serie.schema_name, schema_name)
        self.assertEqual(data_serie.table_name, table_name)
        self.assertEqual(data_serie.db, db)
        self.assertEqual(data_serie.serie, serie)


@mock.patch('src.serie_date.logics.DateColumn.is_serie_none')
class TestNone(unittest.TestCase):
    def test_empty(self, none):
        none.return_value = "Serie is empty"
        serie = DateColumn(None, None, None, None, None)
        result = serie.is_serie_none()
        expect = none.return_value
        self.assertEqual(result, expect)

    def test_null(self, null):
        count_null = 3
        null.return_value = f"Serie has {count_null} null"
        serie = DateColumn(None, None, None, None, None)
        result = serie.is_serie_none()
        expect = "Serie has 3 null"
        self.assertEqual(result, expect)


class TestUnique(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([1, 2, 3, 4, 5, 5, 7, 7], name="serie1")

    def test_unique(self):
        self.serie.set_unique()
        result = self.serie.n_unique
        expect = 6
        self.assertEqual(result, expect)


class TestMissing(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([1, None, 3, None, 5], name="serie2")

    def test_missing(self):
        self.serie.set_missing()
        result = self.serie.n_missing
        expect = 2
        self.assertEqual(result, expect)


@mock.patch('src.database.logics.PostgresConnector.run_query')
class TestMax(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([1, 2, 3, 6, 7, 9], name="date_max")
        self.serie.set_max()
        result = self.serie.col_max
        expect = 6
        self.assertEqual(result, expect)


@mock.patch('src.database.logics.PostgresConnector.run_query')
class TestWeekend(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.db = PostgresConnector(None, None, None, None)

    def test_set_weekend(self, mock_run):
        mock_run.return_value = pd.DataFrame([2, 3], columns=["count"])
        self.serie.set_weekend()
        result = self.serie.n_weekend
        expect = 2
        self.assertEqual(result, expect)


class TestWeekday(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([1, 2, 3, 4, 5, 6, 7], name="day")
        self.serie.n_weekend = 2

    def test_weekday(self):
        self.serie.set_weekday()
        result = self.serie.n_weekday
        expect = 5
        self.assertEqual(result, expect)


class TestFuture(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([datetime.datetime(2020, 3, 30, 0, 0), datetime.datetime(2025, 1, 1, 0, 0)],
                                     name="date")

    def test_future(self):
        self.serie.set_future()
        result = self.serie.n_future
        expect = 1
        self.assertEqual(result, expect)

class TestEmpty1970(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([datetime.date(1970, 1, 3),
                                      datetime.date(1970, 2, 2),
                                      datetime.date(1970, 1, 1)],
                                     name='test')

    def test_1970(self):
        self.serie.set_empty_1970()
        result = self.serie.n_empty_1970
        expect = 1
        self.assertEqual(result, expect)


class TestFrequent(unittest.TestCase):
    def setUp(self):
        self.serie = DateColumn(None, None, None, None, None)
        self.serie.serie = pd.Series([3, 3, 4, 4, 6, 6, 9, 9], name='test')

    def test_set_frequent(self):
        self.serie.set_frequent()
        result = self.serie.frequent
        expect = pd.DataFrame([[3, 2, 0.25], [4, 2, 0.25],
                               [6, 2, 0.25], [9, 2, 0.25]],
                              columns=['value', 'occurrence', 'percentage'])
        pd.testing.assert_frame_equal(result, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
