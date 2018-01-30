"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

from __future__ import generators, unicode_literals
from .version import __version__
from .options import *
from .graph_object_base import GraphObjectBase

try:
    from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
except ImportError:
    from urlparse import urlparse, parse_qsl, urlunparse
    from urllib import urlencode


class RequestBase(object):

    def __init__(self, request_url, client, options):
        """Initialize a request to be sent

        Args:
            request_url (str): The URL to send the request to
            client (:class:`GraphClient<microsoft.requests.one_drive_client.GraphClient>`):
                The client used to make the requests
            options (list of :class:`Option<microsoft.options.Option>`):
                A list of options to add to the request
        """
        self._client = client
        self._request_url = request_url
        self._headers = {}
        self._query_options = {}
        self.content_type = None

        if (options):
            header_list = [
                pair for pair in options if isinstance(pair, HeaderOption)]
            self._headers = {pair.key: pair.value for pair in header_list}

            query_list = [
                pair for pair in options if isinstance(pair, QueryOption)]
            self._query_options = {pair.key: pair.value for pair in query_list}

    @property
    def request_url(self):
        """Gets the request URL with query string appended

        Returns:
            str: The request URL
        """
        url_parts = list(urlparse(self._request_url))
        query_dict = dict(parse_qsl(url_parts[4]))
        self._query_options.update(query_dict)
        url_parts[4] = urlencode(self._query_options)
        return urlunparse(url_parts)

    @property
    def content_type(self):
        """Gets and sets the content-type header of the request
        (ex. application/x-www-form-urlencoded)

        Returns:
            str: The request content-type
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value

    @property
    def method(self):
        """Gets and sets the HTTP method by which to send the
        request (ex. PUT, GET)

        Returns:
            str: The HTTP method
        """
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    def append_option(self, option):
        """Appends an option to the request

        Args:
            option (:class:`Option<microsoft.options.Option>`):
                The option to append to the request
        """
        if isinstance(option, HeaderOption):
            self._headers[option.key] = option.value
        elif isinstance(option, QueryOption):
            self._query_options[option.key] = option.value

    def send(self, content=None, path=None):
        """Send the request using the client specified
        at request initialization

        Args:
            content (str): Defaults to None, the body of the request
                that will be sent
            path (str): Defaults to None, the local path of the file which
                will be sent

        Returns:
            :class:`HttpResponse<microsoft.http_response.HttpResponse>`:
                The response to the request
        """
        self._client.auth_provider.authenticate_request(self)

        self.append_option(HeaderOption("X-RequestStats",
                                        "SdkVersion=Graph-python-"+__version__))

        if self.content_type:
            self.append_option(HeaderOption("Content-Type", self.content_type))

        if path:
            response = self._client.http_provider.send(
                self.method,
                self._headers,
                self.request_url,
                path=path)
        else:
            content_dict = None

            if content:
                content_dict = content.to_dict() if isinstance(
                    content, GraphObjectBase) else content

            response = self._client.http_provider.send(
                self.method,
                self._headers,
                self.request_url,
                content=content_dict)

        return response

    def download_item(self, path):
        """Download a file to a local path

        Args:
            path (str): The local path to download the file

        Returns:
            :class:`HttpResponse<microsoft.http_response.HttpResponse>`:
                The response to the request
        """
        self._client.auth_provider.authenticate_request(self)

        self.append_option(HeaderOption("X-RequestStats",
                                        "SDK-Version=python-v"+__version__))

        if self.content_type:
            self.append_option(HeaderOption("Content-Type", self.content_type))

        response = self._client.http_provider.download(
            self._headers,
            self.request_url,
            path)

        return response


    def _set_query_options(self, search=None, select=None, expand=None,
                           order_by=None, filter=None, top=None, skip=None,
                           skip_token=None, count=False):
        """Adds query options from a set of known parameters
        Args:
            search (str): Default None, a property and value pair separated
                by a colon.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
            filter (str): Default None, filters the response based on a set
                of criteria.
            top (int): Default None, the number of items to return in a result.
            skip (int): Default None, the number of items to skip in a result
                set.
            skip_token (str): Default None, paging token that is used to get
                the next set of results.
            count (bool): Default False, a collection and the number of items
                in the collection.
        """

        if search:
            self.append_option(QueryOption("$search", search))

        if select:
            self.append_option(QueryOption("$select", select))

        if order_by:
            self.append_option(QueryOption("$orderby", order_by))

        if expand:
            self.append_option(QueryOption("$expand", expand))

        if filter:
            self.append_option(QueryOption("$filter", filter))

        if top:
            self.append_option(QueryOption("$top", str(top)))

        if skip:
            self.append_option(QueryOption("$skip", str(skip)))

        if skip_token:
            self.append_option(QueryOption("$skipToken", skip_token))

        if count:
            self.append_option(QueryOption("$count", str(count).lower()))
