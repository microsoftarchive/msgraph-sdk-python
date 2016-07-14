# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import directory_role_request_builder 
from ..model.directory_role import DirectoryRole
import json
import asyncio

class DirectoryRoleCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DirectoryRoleCollectionRequest
        
        Args:
            request_url (str): The url to perform the DirectoryRoleCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DirectoryRoleCollectionPage

        Returns: 
            :class:`DirectoryRoleCollectionPage<msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        self.method = "GET"
        collection_response = DirectoryRoleCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the DirectoryRoleCollectionPage in async

        Yields: 
            :class:`DirectoryRoleCollectionPage<msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class DirectoryRoleCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DirectoryRoleRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DirectoryRoleRequestBuilder for
        
        Returns: 
            :class:`DirectoryRoleRequestBuilder<msgraph.request.directory_role_request_builder.DirectoryRoleRequestBuilder>`:
                A DirectoryRoleRequestBuilder for that key
        """
        return directory_role_request_builder.DirectoryRoleRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,order_by=None, options=None):
        """Builds the DirectoryRoleCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DirectoryRoleCollectionRequest<msgraph.request.directory_role_collection.DirectoryRoleCollectionRequest>`:
                The DirectoryRoleCollectionRequest
        """
        req = DirectoryRoleCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(order_by=order_by, )
        return req

    def get(self):
        """Gets the DirectoryRoleCollectionPage

        Returns: 
            :class:`DirectoryRoleCollectionPage<msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the DirectoryRoleCollectionPage in async

        Yields: 
            :class:`DirectoryRoleCollectionPage<msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class DirectoryRoleCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DirectoryRoleCollectionPage<msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DirectoryRoleCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DirectoryRoleCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the DirectoryRole at the index specified
        
        Args:
            index (int): The index of the item to get from the DirectoryRoleCollectionPage

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole at the index
        """
        return DirectoryRole(self._prop_list[index])

    def directory_role(self):
        """Get a generator of DirectoryRole within the DirectoryRoleCollectionPage
        
        Yields:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The next DirectoryRole in the collection
        """
        for item in self._prop_list:
            yield DirectoryRole(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DirectoryRoleCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DirectoryRoleCollectionRequest(next_page_link, client, options)
