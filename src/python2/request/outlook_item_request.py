# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.outlook_item import OutlookItem
import json

class OutlookItemRequest(RequestBase):
    """The type OutlookItemRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new OutlookItemRequest.

        Args:
            request_url (str): The url to perform the OutlookItemRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(OutlookItemRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified OutlookItem."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified OutlookItem.
        
        Returns:
            :class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`:
                The OutlookItem.
        """
        self.method = "GET"
        entity = OutlookItem(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, outlook_item):
        """Updates the specified OutlookItem.
        
        Args:
            outlook_item (:class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`):
                The OutlookItem to update.

        Returns:
            :class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`:
                The updated OutlookItem.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = OutlookItem(json.loads(self.send(outlook_item).content))
        self._initialize_collection_properties(entity)
        return entity

