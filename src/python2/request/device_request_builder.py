# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .device_request import DeviceRequest
from ..request_builder_base import RequestBuilderBase
from ..request import directory_object_collection


class DeviceRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DeviceRequestBuilder

        Args:
            request_url (str): The url to perform the DeviceRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DeviceRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the DeviceRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DeviceRequest<microsoft.msgraph.request.device_request.DeviceRequest>`:
                The DeviceRequest
        """
        req = DeviceRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Device."""
        self.request().delete()

    def get(self):
        """Gets the specified Device.
        
        Returns:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The Device.
        """
        return self.request().get()

    def update(self, device):
        """Updates the specified Device.
        
        Args:
            device (:class:`Device<microsoft.msgraph.model.device.Device>`):
                The Device to update.

        Returns:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The updated Device
        """
        return self.request().update(device)


    @property
    def registered_owners(self):
        """The registered_owners for the DeviceRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<microsoft.msgraph.request.registered_owners_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the DeviceRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("registeredOwners"), self._client)

    @property
    def registered_users(self):
        """The registered_users for the DeviceRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<microsoft.msgraph.request.registered_users_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the DeviceRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("registeredUsers"), self._client)

