#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map method"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int],
    ) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
    ) -> None:
        """Test access_nested_map method for KeyError exceptions."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check if the raised KeyError contains the expected message
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests the get_json function"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
        mock_get,
    ) -> None:
        """Test get_json with mock requests.get"""

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Tests the memoize decorator"""

    @patch.object(TestClass, "a_method")
    def test_memoize(self, mock_a_method):
        """Test that memoize caches the result of a method"""
        mock_a_method.return_value = 42  # Mock the return value of a_method

        test_instance = TestClass()  # Create an instance of TestClass

        # Call a_property twice
        result_first_call = test_instance.a_property
        result_second_call = test_instance.a_property

        # Assert that the results of both calls are correct
        self.assertEqual(result_first_call, 42)
        self.assertEqual(result_second_call, 42)

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()
