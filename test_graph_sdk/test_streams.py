import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import msgraph
from msgraph import HttpResponse
import json


class TestStreams(unittest.TestCase):

    @patch('msgraph.HttpProvider')
    @patch('msgraph.AuthProvider')
    def test_put(self, MockHttpProvider, MockAuthProvider):

        response = HttpResponse(200, None, json.dumps({"name":"test1", "folder":{}, "id":"test!id"}))

        instance = MockHttpProvider.return_value
        instance.send.return_value = response

        instance = MockAuthProvider.return_value
        instance.authenticate.return_value = "blah"
        instance.authenticate_request.return_value = None

        http_provider = msgraph.HttpProvider()
        auth_provider = msgraph.AuthProvider()
        client = msgraph.GraphClient("/", http_provider, auth_provider)

        response_item = client.drives["me"].items["root"].children["newFile.txt"].content.request().upload("./myPath/myFile.txt")

        assert client.http_provider.send.call_args[1]["path"] == "./myPath/myFile.txt"
        assert client.http_provider.send.call_args[0][2] == "/drives/me/items/root/children/newFile.txt/content"
        assert all(item in response_item._prop_dict.items() for item in json.loads(response.content).items())

    @patch('msgraph.HttpProvider')
    @patch('msgraph.AuthProvider')
    def test_download(self, MockHttpProvider, MockAuthProvider):

        path = "./myPath/myFile.txt"
        response = HttpResponse(200, None, None)

        instance = MockHttpProvider.return_value
        instance.download.return_value = response

        instance = MockAuthProvider.return_value
        instance.authenticate.return_value = "blah"
        instance.authenticate_request.return_value = None

        http_provider = msgraph.HttpProvider()
        auth_provider = msgraph.AuthProvider()
        client = msgraph.GraphClient("/", http_provider, auth_provider)
        client.drives["me"].items["root"].children["newFile.txt"].content.request().download(path)

        assert client.http_provider.download.call_args[0][2] == path
        assert client.http_provider.download.call_args[0][1] == "/drives/me/items/root/children/newFile.txt/content"
