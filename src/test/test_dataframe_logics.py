import os
import sys

import pandas as pd
import unittest

from numpy import NAN
from unittest import mock
from src.dataframe.logics import Dataset

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))


@mock.patch('src.database.logics.PostgresConnector')
class TestInstantiation(unittest.TestCase):
    def test_instanciation(self, mock_db):
        schema_name = 'public'
        table_name = 'products'
        db = mock_db
        df = mock_db.load_table(schema_name, table_name)

        dataset = Dataset('public', 'products', db, df)
        self.assertEqual(dataset.schema_name, schema_name)
        self.assertEqual(dataset.table_name, table_name)
        self.assertEqual(dataset.db, db)
        self.assertEqual(dataset.df, df)


@mock.patch('src.dataframe.logics.Dataset.is_df_none')
class TestNone(unittest.TestCase):
    def test_empty(self, value):
        value.return_value = "DataFrame is empty!"
        dataset = Dataset(None, None, None, None)
        result = dataset.is_df_none()
        expect = value.return_value
        self.assertEqual(result, expect)

    def test_several_null(self, none):
        count_null = 8
        none.return_value = f"Dataframe has {count_null} null"
        dataset = Dataset(None, None, None, None)
        result = dataset.is_df_none()
        expect = "Dataframe has 8 null"
        self.assertEqual(result, expect)

    def test_null(self, null):
        null.return_value = False
        dataset = Dataset(None, None, None, None)
        result = dataset.is_df_none()
        self.assertFalse(result)


class TestDimensions(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset(None, None, None, None)

    def test_n_dimensions(self):
        sample_df = pd.DataFrame([[1, 2, 3], [7, 8, 9]], columns=['A', 'B', 'C'])
        self.dataset.df = sample_df
        self.dataset.set_dimensions()
        self.assertEqual(self.dataset.n_cols, 3)
        self.assertEqual(self.dataset.n_rows, 2)


class TestDuplicates(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset(None, None, None, None)

    def test_duplicates(self):
        sample_df = pd.DataFrame([[4, 3, 7], [9, 1, 2], [9, 1, 2], [0, 3, 4]], columns=['A', 'B', 'C'])
        self.dataset.df = sample_df
        self.dataset.set_duplicates()
        self.assertEqual(self.dataset.n_duplicates, 2)


class TestMissing(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset(None, None, None, None)

    def test_missing(self):
        sample_df = pd.DataFrame([[1, NAN, 5, NAN, 6, NAN],
                                  [1, 2, NAN, NAN, NAN, NAN]],
                                 columns=['A', 'B', 'C', 'D', 'E', 'F'])
        self.dataset.df = sample_df
        self.dataset.set_missing()
        result = self.dataset.n_missing
        self.assertEqual(result, 7)


class TestGet(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset(None, None, None, None)
        self.dataset.df = pd.DataFrame([[1, 2], [1, 2], [3, 4], [3, 4]], columns=['A', 'B'])

    def test_head_data(self):
        result = self.dataset.get_head(2)
        expect = self.dataset.df.head(2)
        pd.testing.assert_frame_equal(result, expect)

    def test_tail_data(self):
        result = self.dataset.get_tail(3)
        expect = self.dataset.df.tail(3)
        pd.testing.assert_frame_equal(result, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
