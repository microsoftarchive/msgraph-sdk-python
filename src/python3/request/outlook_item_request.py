# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.outlook_item import OutlookItem
import json
import asyncio

class OutlookItemRequest(RequestBase):
    """The type OutlookItemRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new OutlookItemRequest.

        Args:
            request_url (str): The url to perform the OutlookItemRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(OutlookItemRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified OutlookItem."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified OutlookItem."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified OutlookItem.
        
        Returns:
            :class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`:
                The OutlookItem.
        """
        self.method = "GET"
        entity = OutlookItem(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified OutlookItem in async.

        Yields:
            :class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`:
                The OutlookItem.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, outlook_item):
        """Updates the specified OutlookItem.
        
        Args:
            outlook_item (:class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`):
                The OutlookItem to update.

        Returns:
            :class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`:
                The updated OutlookItem.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = OutlookItem(json.loads(self.send(outlook_item).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, outlook_item):
        """Updates the specified OutlookItem in async
        
        Args:
            outlook_item (:class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`):
                The OutlookItem to update.

        Yields:
            :class:`OutlookItem<msgraph.model.outlook_item.OutlookItem>`:
                The updated OutlookItem.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    outlook_item)
        entity = yield from future
        return entity

