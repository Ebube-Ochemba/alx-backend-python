#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json) -> None:
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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            # Set the return value of the org property to a mock payload
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }

            # Create an instance of GithubOrgClient with any organization name
            client = GithubOrgClient("google")

            # Assert that the _public_repos_url property returns the correct...
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Tests the public_repos method."""

        # Define a mock payload for the get_json function
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]

        # Use a context manager to patch _public_repos_url
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/users/google/repos"
        ):
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the public_repos method without specifying a license
            result = client.public_repos()

            # Assert the list of repo names is what we expect
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Call the public_repos method with a specific license
            result_with_license = client.public_repos(license="mit")

            # Assert the list of repo names with MIT license
            self.assertEqual(result_with_license, ["repo1", "repo3"])

            # Check that the mocked _public_repos_url was called once
            self.assertEqual(mock_get_json.call_count, 1)

            # Check that the mocked get_json was called once
            mock_get_json.assert_called_once_with(
                "https://api.github.com/users/google/repos"
                )
