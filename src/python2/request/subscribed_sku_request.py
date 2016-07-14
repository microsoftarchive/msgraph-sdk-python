# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.subscribed_sku import SubscribedSku
import json

class SubscribedSkuRequest(RequestBase):
    """The type SubscribedSkuRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new SubscribedSkuRequest.

        Args:
            request_url (str): The url to perform the SubscribedSkuRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscribedSkuRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified SubscribedSku."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified SubscribedSku.
        
        Returns:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The SubscribedSku.
        """
        self.method = "GET"
        entity = SubscribedSku(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, subscribed_sku):
        """Updates the specified SubscribedSku.
        
        Args:
            subscribed_sku (:class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`):
                The SubscribedSku to update.

        Returns:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The updated SubscribedSku.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = SubscribedSku(json.loads(self.send(subscribed_sku).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.service_plans and value.service_plans._prop_dict:
                if "service_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["service_plans@odata.nextLink"]
                    value.service_plans._init_next_page_request(next_page_link, self._client, None)
