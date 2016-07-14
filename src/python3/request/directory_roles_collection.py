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

class DirectoryRolesCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DirectoryRolesCollectionRequest
        
        Args:
            request_url (str): The url to perform the DirectoryRolesCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRolesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DirectoryRolesCollectionPage

        Returns: 
            :class:`DirectoryRolesCollectionPage<msgraph.request.directory_roles_collection.DirectoryRolesCollectionPage>`:
                The DirectoryRolesCollectionPage
        """
        self.method = "GET"
        collection_response = DirectoryRolesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the DirectoryRolesCollectionPage in async

        Yields: 
            :class:`DirectoryRolesCollectionPage<msgraph.request.directory_roles_collection.DirectoryRolesCollectionPage>`:
                The DirectoryRolesCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class DirectoryRolesCollectionRequestBuilder(RequestBuilderBase):

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
        """Builds the DirectoryRolesCollectionRequest
        
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
            :class:`DirectoryRolesCollectionRequest<msgraph.request.directory_roles_collection.DirectoryRolesCollectionRequest>`:
                The DirectoryRolesCollectionRequest
        """
        req = DirectoryRolesCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(order_by=order_by, )
        return req

    def get(self):
        """Gets the DirectoryRolesCollectionPage

        Returns: 
            :class:`DirectoryRolesCollectionPage<msgraph.request.directory_roles_collection.DirectoryRolesCollectionPage>`:
                The DirectoryRolesCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the DirectoryRolesCollectionPage in async

        Yields: 
            :class:`DirectoryRolesCollectionPage<msgraph.request.directory_roles_collection.DirectoryRolesCollectionPage>`:
                The DirectoryRolesCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class DirectoryRolesCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DirectoryRolesCollectionPage<msgraph.request.directory_roles_collection.DirectoryRolesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DirectoryRolesCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DirectoryRolesCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the DirectoryRole at the index specified
        
        Args:
            index (int): The index of the item to get from the DirectoryRolesCollectionPage

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole at the index
        """
        return DirectoryRole(self._prop_list[index])

    def directory_roles(self):
        """Get a generator of DirectoryRole within the DirectoryRolesCollectionPage
        
        Yields:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The next DirectoryRole in the collection
        """
        for item in self._prop_list:
            yield DirectoryRole(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DirectoryRolesCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DirectoryRolesCollectionRequest(next_page_link, client, options)
