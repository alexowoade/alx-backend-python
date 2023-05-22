#!/usr/bin/env python3
"""
This module contains unit tests for the access_nested_map function in utils.py.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class contains unit tests for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested map.
            path (tuple): The path to access the value in the nested map.
            expected_result: The expected result after accessing the nested map.

        Returns:
            None.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

