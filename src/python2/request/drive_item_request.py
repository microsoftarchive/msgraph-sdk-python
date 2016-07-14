# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.drive_item import DriveItem
import json

class DriveItemRequest(RequestBase):
    """The type DriveItemRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DriveItemRequest.

        Args:
            request_url (str): The url to perform the DriveItemRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DriveItemRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DriveItem."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified DriveItem.
        
        Returns:
            :class:`DriveItem<microsoft.msgraph.model.drive_item.DriveItem>`:
                The DriveItem.
        """
        self.method = "GET"
        entity = DriveItem(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, drive_item):
        """Updates the specified DriveItem.
        
        Args:
            drive_item (:class:`DriveItem<microsoft.msgraph.model.drive_item.DriveItem>`):
                The DriveItem to update.

        Returns:
            :class:`DriveItem<microsoft.msgraph.model.drive_item.DriveItem>`:
                The updated DriveItem.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DriveItem(json.loads(self.send(drive_item).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.permissions and value.permissions._prop_dict:
                if "permissions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["permissions@odata.nextLink"]
                    value.permissions._init_next_page_request(next_page_link, self._client, None)
            if value.children and value.children._prop_dict:
                if "children@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["children@odata.nextLink"]
                    value.children._init_next_page_request(next_page_link, self._client, None)
            if value.thumbnails and value.thumbnails._prop_dict:
                if "thumbnails@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["thumbnails@odata.nextLink"]
                    value.thumbnails._init_next_page_request(next_page_link, self._client, None)
