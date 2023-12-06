import sys
import logging
import os
import unittest
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from serie_numeric.queries import * 

class TestNumber_query(unittest.TestCase):
    """
    --------------------
    Description
    --------------------
    -> TestNumber_query(class): to test the all the method in query.py of serie numeric  
    --------------------
   
    """
    def test_get_std_query(self):
        """
        --------------------
        Description
        --------------------
        -> test_get_std_query(method): to test the method get_std_query 
        --------------------
        Pseudo-Code
        --------------------
        Save a string "SELECT STDDEV(student_id) FROM uts.student_id" and names it as expected
        apply get_std_query with input arguments:'uts' and 'student_id' and name as result
        apply self.assertEqual() with input arguments:expected and result, to obtain the logic True or False that whether expected is equal to result or not 
        --------------------
        """


        expected = f'SELECT STDDEV(student_id) FROM uts.student'
        result = get_std_query('uts','student','student_id')
        self.assertEqual(expected,result)
    
    def test_get_unique_query(self):

        """
        --------------------
        Description
        --------------------
        -> test_get_unique_query(method): to test the method get_unique_query 
        --------------------
        Pseudo-Code
        --------------------
        Save a string "SELECT COUNT(DISTINCT student_id) FROM uts.student_id" and name it as expected
        apply get_unique_query with input arguments:'uts' and 'student_id' and name as result
        apply self.assertEqual() with input arguments:expected and result, to obtain the logic True or False that whether expected is equal to result or not 
        --------------------
        """
        expected = f'SELECT COUNT(DISTINCT student_id) FROM uts.student'
        result = get_unique_query('uts','student','student_id')
        self.assertEqual(expected,result)


    def test_get_negative_number_query(self):  
        """
        --------------------
        Description
        --------------------
        -> test_get_negative_number_query(method): to test the method get_negative_number_query 
        --------------------
        Pseudo-Code
        --------------------
        Save a string "SELECT COUNT(student_id) as count FROM uts.student_id WHERE student_id < 0" and names it as expected
        apply get_negative_number_query with input arguments:'uts' and 'student_id' and name as result
        apply self.assertEqual() with input arguments:expected and result, to obtain the logic True or False that whether expected is equal to result or not 
        --------------------
        """

        expected = f'SELECT COUNT(student_id) as count FROM uts.student WHERE student_id < 0'
        result = get_negative_number_query('uts','student','student_id')
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main(verbosity=2)