# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .drive_request import DriveRequest
from ..request_builder_base import RequestBuilderBase
from ..request.drive_recent import DriveRecentRequestBuilder
from ..request.drive_shared_with_me import DriveSharedWithMeRequestBuilder
import asyncio

from ..request import drive_item_collection
from ..request import drive_item_request_builder


class DriveRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DriveRequestBuilder

        Args:
            request_url (str): The url to perform the DriveRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DriveRequest<msgraph.request.drive_request.DriveRequest>`:
                The DriveRequest
        """
        req = DriveRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Drive."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Drive."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Drive.
        
        Returns:
            :class:`Drive<msgraph.model.drive.Drive>`:
                The Drive.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Drive in async.

        Returns:
            :class:`Drive<msgraph.model.drive.Drive>`:
                The Drive.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, drive):
        """Updates the specified Drive.
        
        Args:
            drive (:class:`Drive<msgraph.model.drive.Drive>`):
                The Drive to update.

        Returns:
            :class:`Drive<msgraph.model.drive.Drive>`:
                The updated Drive
        """
        return self.request().update(drive)

    @asyncio.coroutine
    def update_async(self, drive):
        """Updates the specified Drive in async
        
        Args:
            drive (:class:`Drive<msgraph.model.drive.Drive>`):
                The Drive to update.

        Returns:
            :class:`Drive<msgraph.model.drive.Drive>`:
                The updated Drive.
        """
        entity = yield from self.request().update_async(drive)
        return entity

    @property
    def items(self):
        """The items for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemCollectionRequestBuilder<msgraph.request.items_collection.DriveItemCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_collection.DriveItemCollectionRequestBuilder(self.append_to_request_url("items"), self._client)

    @property
    def special(self):
        """The special for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemCollectionRequestBuilder<msgraph.request.special_collection.DriveItemCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_collection.DriveItemCollectionRequestBuilder(self.append_to_request_url("special"), self._client)

    @property
    def root(self):
        """The root for the DriveRequestBuilder

        Returns: 
            :class:`DriveItemRequestBuilder<msgraph.request.drive_item_request.DriveItemRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.append_to_request_url("root"), self._client)

    def recent(self):
        """Executes the recent method


        Returns:
            :class:`DriveRecentRequestBuilder<msgraph.request.drive_recent.DriveRecentRequestBuilder>`:
                A DriveRecentRequestBuilder for the method
        """
        return DriveRecentRequestBuilder(self.append_to_request_url("recent"), self._client)

    def shared_with_me(self):
        """Executes the sharedWithMe method


        Returns:
            :class:`DriveSharedWithMeRequestBuilder<msgraph.request.drive_shared_with_me.DriveSharedWithMeRequestBuilder>`:
                A DriveSharedWithMeRequestBuilder for the method
        """
        return DriveSharedWithMeRequestBuilder(self.append_to_request_url("sharedWithMe"), self._client)


