"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""


import abc


class HttpProviderBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(self, method, headers, url, data=None, content=None, path=None):
        """Send the built request using all the specified
        parameters.

        Args:
            method (str): The HTTP method to use (ex. GET)
            headers (dict of (str, str)): A dictionary of name-value
                pairs for headers in the request
            url (str): The URL for the request to be sent to
            data (str): Defaults to None, data to include in the body
                of the request which is not in JSON format
            content (dict): Defaults to None, a dictionary to include
                in JSON format in the body of the request
            path (str): Defaults to None, the path to the local file
                to send in the body of the request

        Returns:
            :class:`HttpResponse<microsoft.http_response.HttpResponse>`:
                The response to the request
        """
        pass

    @abc.abstractmethod
    def download(self, headers, url, path):
        """Downloads a file to the stated path

        Args:
            headers (dict of (str, str)): A dictionary of name-value
                pairs to be used as headers in the request
            url (str): The URL from which to download the file
            path (str): The local path to save the downloaded file

        Returns:
            :class:`HttpResponse<microsoft.http_response.HttpResponse>`:
                The response to the request
        """
        pass
