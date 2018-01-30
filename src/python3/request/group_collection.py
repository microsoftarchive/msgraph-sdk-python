# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import group_request_builder 
from ..model.group import Group
import json
import asyncio

class GroupCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the GroupCollectionRequest
        
        Args:
            request_url (str): The url to perform the GroupCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(GroupCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the GroupCollectionPage

        Returns: 
            :class:`GroupCollectionPage<msgraph.request.group_collection.GroupCollectionPage>`:
                The GroupCollectionPage
        """
        self.method = "GET"
        collection_response = GroupCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the GroupCollectionPage in async

        Yields: 
            :class:`GroupCollectionPage<msgraph.request.group_collection.GroupCollectionPage>`:
                The GroupCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class GroupCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the GroupRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a GroupRequestBuilder for
        
        Returns: 
            :class:`GroupRequestBuilder<msgraph.request.group_request_builder.GroupRequestBuilder>`:
                A GroupRequestBuilder for that key
        """
        return group_request_builder.GroupRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, filter=None, top=None, order_by=None, options=None):
        """Builds the GroupCollectionRequest
        
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
            :class:`GroupCollectionRequest<msgraph.request.group_collection.GroupCollectionRequest>`:
                The GroupCollectionRequest
        """
        req = GroupCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, filter=filter, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the GroupCollectionPage

        Returns: 
            :class:`GroupCollectionPage<msgraph.request.group_collection.GroupCollectionPage>`:
                The GroupCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the GroupCollectionPage in async

        Yields: 
            :class:`GroupCollectionPage<msgraph.request.group_collection.GroupCollectionPage>`:
                The GroupCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class GroupCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`GroupCollectionPage<msgraph.request.group_collection.GroupCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = GroupCollectionPage(self._prop_dict["value"])

        return self._collection_page


class GroupCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Group at the index specified
        
        Args:
            index (int): The index of the item to get from the GroupCollectionPage

        Returns:
            :class:`Group<msgraph.model.group.Group>`:
                The Group at the index
        """
        return Group(self._prop_list[index])

    def group(self):
        """Get a generator of Group within the GroupCollectionPage
        
        Yields:
            :class:`Group<msgraph.model.group.Group>`:
                The next Group in the collection
        """
        for item in self._prop_list:
            yield Group(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the GroupCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = GroupCollectionRequest(next_page_link, client, options)
