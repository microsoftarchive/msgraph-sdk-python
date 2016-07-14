# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import device_request_builder # import DeviceRequestBuilder
#from .device_request_builder import DeviceRequestBuilder
from ..model.device import Device
import json

class DevicesCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DevicesCollectionRequest
        
        Args:
            request_url (str): The url to perform the DevicesCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DevicesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DevicesCollectionPage

        Returns: 
            :class:`DevicesCollectionPage<microsoft.msgraph.request.devices_collection.DevicesCollectionPage>`:
                The DevicesCollectionPage
        """
        self.method = "GET"
        collection_response = DevicesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class DevicesCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DeviceRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DeviceRequestBuilder for
        
        Returns: 
            :class:`DeviceRequestBuilder<microsoft.msgraph.request.device_request_builder.DeviceRequestBuilder>`:
                A DeviceRequestBuilder for that key
        """
        return device_request_builder.DeviceRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the DevicesCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DevicesCollectionRequest<microsoft.msgraph.request.devices_collection.DevicesCollectionRequest>`:
                The DevicesCollectionRequest
        """
        req = DevicesCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the DevicesCollectionPage

        Returns: 
            :class:`DevicesCollectionPage<microsoft.msgraph.request.devices_collection.DevicesCollectionPage>`:
                The DevicesCollectionPage
        """
        return self.request().get()



class DevicesCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DevicesCollectionPage<microsoft.msgraph.request.devices_collection.DevicesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DevicesCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DevicesCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Device at the index specified
        
        Args:
            index (int): The index of the item to get from the DevicesCollectionPage

        Returns:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The Device at the index
        """
        return Device(self._prop_list[index])

    def devices(self):
        """Get a generator of Device within the DevicesCollectionPage
        
        Yields:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The next Device in the collection
        """
        for item in self._prop_list:
            yield Device(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DevicesCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DevicesCollectionRequest(next_page_link, client, options)
