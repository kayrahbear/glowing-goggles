import unittest
from unittest.mock import MagicMock, patch
from cli_functions import get_album_data


class TestCliFunctions(unittest.TestCase):

    @patch('cli_functions.requests')
    def test_find_single_album_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            "albumId": 1,
            "id": 1,
            "title": "A Very Lovely Photo",
            "url": "www.averygreatphoto.com",
            "thumbnailUrl": "www.averygreatthumbnail.com",
        }]

        mock_requests.get.return_value = mock_response

        response = get_album_data("1")

        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]["title"], "A Very Lovely Photo")

    @patch('cli_functions.requests')
    def test_find_album_range_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "albumId": 1,
                "id": 1,
                "title": "A Very Lovely Photo",
                "url": "www.averygreatphoto.com",
                "thumbnailUrl": "www.averygreatthumbnail.com",
            },
            {
                "albumId": 1,
                "id": 2,
                "title": "A Pretty Nice Photo",
                "url": "www.averygreatphoto.com",
                "thumbnailUrl": "www.averygreatthumbnail.com",
            },
            {
                "albumId": 2,
                "id": 12,
                "title": "Another Very Lovely Photo",
                "url": "www.averygreatphoto.com",
                "thumbnailUrl": "www.averygreatthumbnail.com",
            },
        ]

        mock_requests.get.return_value = mock_response

        response = get_album_data("1-2")

        self.assertEqual(len(response), 3)

    @patch('cli_functions.requests')
    def test_find_album_failure(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = None

        mock_requests.get.return_value = mock_response

        response = get_album_data("10000")

        self.assertIsNone(response)
