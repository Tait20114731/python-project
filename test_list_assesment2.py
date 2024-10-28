# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:30:25 2024

@author: Tatenda Marimo 20114731
@description: unittest module includes tests for each function, It ensures values can be added, deleted, sorted, and searched correctly. 
@version: 1.0
"""
#importing the unittest and list_assesment2 documents.
import unittest
import list_assesment2  

#grouping the tested functions in a class.
class TestListAssessment2(unittest.TestCase):
    #testing add_value function.
    def test_add_value(self):
        sample_list = []
        result = list_assesment2.add_value(sample_list, 'Test Value')
        self.assertIn('Test Value', result)
    #testing delete_value function.
    def test_delete_value(self):
        sample_list = ['Test Value']
        result = list_assesment2.delete_value(sample_list, 'Test Value')
        self.assertNotIn('Test Value', result)
    #testing sort_value_ascending function.
    def test_sort_value_ascending(self):
        sample_list = [3, 1, 2]
        result = list_assesment2.sort_value(sample_list, 'ascending')
        self.assertEqual(result, [1, 2, 3])
    #testing sort_value_descending function.
    def test_sort_value_descending(self):
        sample_list = [1, 3, 2]
        result = list_assesment2.sort_value(sample_list, 'descending')
        self.assertEqual(result, [3, 2, 1])
    #testing list_value function.
    def test_list_values(self):
        result = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.assertEqual(result, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    #testing search_value_found function.
    def test_binary_search_found(self):
        sample_list = [1, 2, 3, 4, 5]
        result = list_assesment2.binary_search(sample_list, 3)
        self.assertEqual(result, 2)  # Index of 3 in the sorted list [1, 2, 3, 4, 5]
    #testing search_value_found function.
    def test_binary_search_not_found(self):
        sample_list = [1, 2, 3, 4, 5]
        result = list_assesment2.binary_search(sample_list, 6)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
