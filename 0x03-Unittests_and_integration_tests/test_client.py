#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Define a sample return value for the mock
        mock_get_json.return_value = {"key": "value"}

        # Instantiate the GithubOrgClient with the org name
        client = GithubOrgClient(org_name)

        # Call the org property
        result = client.org

        # Check that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

        # Assert that the result of calling org is what the mock returned
        self.assertEqual(result, {"key": "value"})
