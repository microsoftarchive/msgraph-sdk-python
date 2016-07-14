"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""


class RequestBuilderBase(object):

    def __init__(self, request_url, client):
        """Initialize a request builder which returns a request
        when request() is called

        Args:
            request_url (str): The URL to construct the request
                for
            client (:class:`GraphClient<microsoft.requests.one_drive_client.GraphClient>`):
                The client with which the request will be made
        """
        self._request_url = request_url
        self._client = client

    def append_to_request_url(self, url_segment):
        """Appends a URL portion to the current request URL

        Args:
            url_segment (str): The segment you would like to append
                to the existing request URL.
        """
        return self._request_url + "/" + url_segment
