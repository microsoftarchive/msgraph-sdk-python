# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import drive_item_request_builder 
from ..model.drive_item import DriveItem
import json
import asyncio

class ItemsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ItemsCollectionRequest
        
        Args:
            request_url (str): The url to perform the ItemsCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ItemsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ItemsCollectionPage

        Returns: 
            :class:`ItemsCollectionPage<msgraph.request.items_collection.ItemsCollectionPage>`:
                The ItemsCollectionPage
        """
        self.method = "GET"
        collection_response = ItemsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the ItemsCollectionPage in async

        Yields: 
            :class:`ItemsCollectionPage<msgraph.request.items_collection.ItemsCollectionPage>`:
                The ItemsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class ItemsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DriveItemRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DriveItemRequestBuilder for
        
        Returns: 
            :class:`DriveItemRequestBuilder<msgraph.request.drive_item_request_builder.DriveItemRequestBuilder>`:
                A DriveItemRequestBuilder for that key
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the ItemsCollectionRequest
        
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
            :class:`ItemsCollectionRequest<msgraph.request.items_collection.ItemsCollectionRequest>`:
                The ItemsCollectionRequest
        """
        req = ItemsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the ItemsCollectionPage

        Returns: 
            :class:`ItemsCollectionPage<msgraph.request.items_collection.ItemsCollectionPage>`:
                The ItemsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the ItemsCollectionPage in async

        Yields: 
            :class:`ItemsCollectionPage<msgraph.request.items_collection.ItemsCollectionPage>`:
                The ItemsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class ItemsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ItemsCollectionPage<msgraph.request.items_collection.ItemsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ItemsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ItemsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the DriveItem at the index specified
        
        Args:
            index (int): The index of the item to get from the ItemsCollectionPage

        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The DriveItem at the index
        """
        return DriveItem(self._prop_list[index])

    def items(self):
        """Get a generator of DriveItem within the ItemsCollectionPage
        
        Yields:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The next DriveItem in the collection
        """
        for item in self._prop_list:
            yield DriveItem(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ItemsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ItemsCollectionRequest(next_page_link, client, options)
