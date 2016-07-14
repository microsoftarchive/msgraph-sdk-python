"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

from __future__ import generators, unicode_literals
import json
from .error import GraphError


class HttpResponse(object):

    def __init__(self, status, headers, content):
        """Initialize the HttpResponse class returned after
        an HTTP request is made

        Args:
            status (int): HTTP status (ex. 200, 201, etc.)
            headers (dict of (str, str)): The headers in the
                response
            content (str): The body of the response
        """
        self._status = status
        self._headers = headers
        self._content = content

        if self.content and (self.status < 200 or self.status >= 300):
            message = json.loads(self.content)
            if "error" in message:
                if type(message["error"]) == dict:
                    raise GraphError(message["error"], self.status)
                else:
                    raise Exception(str(message["error"]))

    def __str__(self):
        properties = {
            'Status': self.status,
            'Headers': self.headers,
            'Content': self.content
            }
        ret = ""
        for k, v in properties.items():
            ret += "{}: {}\n".format(k, v)
        return ret

    @property
    def status(self):
        """The HTTP status of the response

        Returns:
            int: HTTP status
        """
        return self._status

    @property
    def headers(self):
        """The headers of the response

        Returns:
            dict of (str, str):
                The headers used by the response
        """
        return self._headers

    @property
    def content(self):
        """The content of the response

        Returns:
            str: The body of the response
        """
        return self._content
