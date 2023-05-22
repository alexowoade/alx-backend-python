#!/usr/bin/env python3
"""
<<<<<<< HEAD
This module contains unit tests for the access_nested_map function in utils.py.
=======
Unittests for utils.access_nested_map function.
>>>>>>> 6b06815783610bf670cda836ff9154801a4208df
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
<<<<<<< HEAD
    TestAccessNestedMap class contains unit tests for access_nested_map function.
=======
    Test case for access_nested_map function.
>>>>>>> 6b06815783610bf670cda836ff9154801a4208df
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
<<<<<<< HEAD
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
=======
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...],
                               expected_result: Any) -> None:
>>>>>>> 6b06815783610bf670cda836ff9154801a4208df
        """
        Test access_nested_map function with different inputs.

        Args:
<<<<<<< HEAD
            nested_map (dict): The nested map.
            path (tuple): The path to access the value in the nested map.
            expected_result: The expected result after accessing the nested map.

        Returns:
            None.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

=======
            nested_map: The nested map to access.
            path: The path to the desired value within the map.
            expected_result: The expected result of accessing the nested map.

        Returns:
            None.

        Raises:
            AssertionError: If the actual result doesn't match the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()

>>>>>>> 6b06815783610bf670cda836ff9154801a4208df
