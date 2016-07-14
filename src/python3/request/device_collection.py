# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import device_request_builder 
from ..model.device import Device
import json
import asyncio

class DeviceCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DeviceCollectionRequest
        
        Args:
            request_url (str): The url to perform the DeviceCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DeviceCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DeviceCollectionPage

        Returns: 
            :class:`DeviceCollectionPage<msgraph.request.device_collection.DeviceCollectionPage>`:
                The DeviceCollectionPage
        """
        self.method = "GET"
        collection_response = DeviceCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the DeviceCollectionPage in async

        Yields: 
            :class:`DeviceCollectionPage<msgraph.request.device_collection.DeviceCollectionPage>`:
                The DeviceCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class DeviceCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DeviceRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DeviceRequestBuilder for
        
        Returns: 
            :class:`DeviceRequestBuilder<msgraph.request.device_request_builder.DeviceRequestBuilder>`:
                A DeviceRequestBuilder for that key
        """
        return device_request_builder.DeviceRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,top=None, order_by=None, options=None):
        """Builds the DeviceCollectionRequest
        
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
            :class:`DeviceCollectionRequest<msgraph.request.device_collection.DeviceCollectionRequest>`:
                The DeviceCollectionRequest
        """
        req = DeviceCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(top=top, order_by=order_by, )
        return req

    def get(self):
        """Gets the DeviceCollectionPage

        Returns: 
            :class:`DeviceCollectionPage<msgraph.request.device_collection.DeviceCollectionPage>`:
                The DeviceCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the DeviceCollectionPage in async

        Yields: 
            :class:`DeviceCollectionPage<msgraph.request.device_collection.DeviceCollectionPage>`:
                The DeviceCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class DeviceCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DeviceCollectionPage<msgraph.request.device_collection.DeviceCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DeviceCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DeviceCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Device at the index specified
        
        Args:
            index (int): The index of the item to get from the DeviceCollectionPage

        Returns:
            :class:`Device<msgraph.model.device.Device>`:
                The Device at the index
        """
        return Device(self._prop_list[index])

    def device(self):
        """Get a generator of Device within the DeviceCollectionPage
        
        Yields:
            :class:`Device<msgraph.model.device.Device>`:
                The next Device in the collection
        """
        for item in self._prop_list:
            yield Device(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DeviceCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DeviceCollectionRequest(next_page_link, client, options)
