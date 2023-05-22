#!/usr/bin/env python3
"""
Unittests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...],
                               expected_result: Any) -> None:
        """
        Test access_nested_map function with different inputs.

        Args:
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


