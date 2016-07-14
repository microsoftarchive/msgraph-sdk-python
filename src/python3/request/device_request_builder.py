# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .device_request import DeviceRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import directory_object_collection


class DeviceRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DeviceRequestBuilder

        Args:
            request_url (str): The url to perform the DeviceRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DeviceRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the DeviceRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DeviceRequest<msgraph.request.device_request.DeviceRequest>`:
                The DeviceRequest
        """
        req = DeviceRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified Device."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Device."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Device.
        
        Returns:
            :class:`Device<msgraph.model.device.Device>`:
                The Device.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Device in async.

        Returns:
            :class:`Device<msgraph.model.device.Device>`:
                The Device.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, device):
        """Updates the specified Device.
        
        Args:
            device (:class:`Device<msgraph.model.device.Device>`):
                The Device to update.

        Returns:
            :class:`Device<msgraph.model.device.Device>`:
                The updated Device
        """
        return self.request().update(device)

    @asyncio.coroutine
    def update_async(self, device):
        """Updates the specified Device in async
        
        Args:
            device (:class:`Device<msgraph.model.device.Device>`):
                The Device to update.

        Returns:
            :class:`Device<msgraph.model.device.Device>`:
                The updated Device.
        """
        entity = yield from self.request().update_async(device)
        return entity

    @property
    def registered_owners(self):
        """The registered_owners for the DeviceRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.registered_owners_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the DeviceRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("registeredOwners"), self._client)

    @property
    def registered_users(self):
        """The registered_users for the DeviceRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.registered_users_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the DeviceRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("registeredUsers"), self._client)

