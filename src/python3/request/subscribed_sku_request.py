# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.subscribed_sku import SubscribedSku
import json
import asyncio

class SubscribedSkuRequest(RequestBase):
    """The type SubscribedSkuRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new SubscribedSkuRequest.

        Args:
            request_url (str): The url to perform the SubscribedSkuRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscribedSkuRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified SubscribedSku."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified SubscribedSku."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified SubscribedSku.
        
        Returns:
            :class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`:
                The SubscribedSku.
        """
        self.method = "GET"
        entity = SubscribedSku(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified SubscribedSku in async.

        Yields:
            :class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`:
                The SubscribedSku.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, subscribed_sku):
        """Updates the specified SubscribedSku.
        
        Args:
            subscribed_sku (:class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`):
                The SubscribedSku to update.

        Returns:
            :class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`:
                The updated SubscribedSku.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = SubscribedSku(json.loads(self.send(subscribed_sku).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, subscribed_sku):
        """Updates the specified SubscribedSku in async
        
        Args:
            subscribed_sku (:class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`):
                The SubscribedSku to update.

        Yields:
            :class:`SubscribedSku<msgraph.model.subscribed_sku.SubscribedSku>`:
                The updated SubscribedSku.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    subscribed_sku)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.service_plans and value.service_plans._prop_dict:
                if "service_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["service_plans@odata.nextLink"]
                    value.service_plans._init_next_page_request(next_page_link, self._client, None)
