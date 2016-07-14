# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .drive_request import DriveRequest
from ..request_builder_base import RequestBuilderBase
from ..request import drive_item_collection
from ..request import drive_item_request_builder


class DriveRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DriveRequestBuilder

        Args:
            request_url (str): The url to perform the DriveRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DriveRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the DriveRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DriveRequest<microsoft.msgraph.request.drive_request.DriveRequest>`:
                The DriveRequest
        """
        req = DriveRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Drive."""
        self.request().delete()

    def get(self):
        """Gets the specified Drive.
        
        Returns:
            :class:`Drive<microsoft.msgraph.model.drive.Drive>`:
                The Drive.
        """
        return self.request().get()

    def update(self, drive):
        """Updates the specified Drive.
        
        Args:
            drive (:class:`Drive<microsoft.msgraph.model.drive.Drive>`):
                The Drive to update.

        Returns:
            :class:`Drive<microsoft.msgraph.model.drive.Drive>`:
                The updated Drive
        """
        return self.request().update(drive)


    @property
    def items(self):
        """The items for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemCollectionRequestBuilder<microsoft.msgraph.request.items_collection.DriveItemCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_collection.DriveItemCollectionRequestBuilder(self.append_to_request_url("items"), self._client)

    @property
    def special(self):
        """The special for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemCollectionRequestBuilder<microsoft.msgraph.request.special_collection.DriveItemCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_collection.DriveItemCollectionRequestBuilder(self.append_to_request_url("special"), self._client)

    @property
    def root(self):
        """The root for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemRequestBuilder<microsoft.msgraph.request.drive_item_request.DriveItemRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.append_to_request_url("root"), self._client)


