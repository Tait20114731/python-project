# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:46:09 2024

@author: Tatenda Marimo 20114731
@description: unittest module includes tests for each function, It ensures values can be added, deleted, sorted, and searched correctly. 
@version: 1.0

"""

# Importing the unittest module and your dictionary_ass2 module
import unittest
import dictionary_ass2

# Grouping the tested functions in a class
class TestDictionaryAss2(unittest.TestCase):
    
    #Test adding a value to the dictionary.
    def test_add_value(self):
        test_dict = {}
        result = dictionary_ass2.add_value(test_dict, 'Key1', 'Value1')
        self.assertIn('Key1', result)
        self.assertEqual(result['Key1'], 'Value1')
    #Test deleting an existing key from the dictionary
    def test_delete_value_existing_key(self):
        test_dict = {'Key1': 'Value1'}
        result = dictionary_ass2.delete_value(test_dict, 'Key1')
        self.assertNotIn('Key1', result)
    #Test deleting a key that doesn't exist in the dictionary.
    def test_delete_value_nonexistent_key(self):
        test_dict = {'Key1': 'Value1'}
        result = dictionary_ass2.delete_value(test_dict, 'Key2')
        self.assertEqual(result, test_dict)  # Dictionary should remain unchanged
    #Test sorting the dictionary in ascending order.
    def test_sort_dict_ascending(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3}
        result = dictionary_ass2.sort_dict(test_dict, 'ascending')
        expected_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(result, expected_dict)
    #Test sorting the dictionary in descending order.
    def test_sort_dict_descending(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3}
        result = dictionary_ass2.sort_dict(test_dict, 'descending')
        expected_dict = {'c': 3, 'b': 2, 'a': 1}
        self.assertEqual(result, expected_dict)
    #Test sorting the dictionary with an invalid sort order.
    def test_sort_dict_invalid_order(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3}
        with self.assertRaises(ValueError):
            dictionary_ass2.sort_dict(test_dict, 'invalid_order')
    #Test binary search for an existing key in the dictionary.
    def test_binary_search_dict_found(self):
        test_dict = {'alpha': 'A', 'bravo': 'B', 'charlie': 'C'}
        result = dictionary_ass2.binary_search_dict(test_dict, 'bravo')
        self.assertEqual(result, ('bravo', 'B'))
    #Test binary search for a key that doesn't exist in the dictionary.  
    def test_binary_search_dict_not_found(self):
        test_dict = {'alpha': 'A', 'bravo': 'B', 'charlie': 'C'}
        result = dictionary_ass2.binary_search_dict(test_dict, 'delta')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
