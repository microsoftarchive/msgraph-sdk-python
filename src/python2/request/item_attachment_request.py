# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.item_attachment import ItemAttachment
import json

class ItemAttachmentRequest(RequestBase):
    """The type ItemAttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ItemAttachmentRequest.

        Args:
            request_url (str): The url to perform the ItemAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ItemAttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ItemAttachment."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified ItemAttachment.
        
        Returns:
            :class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`:
                The ItemAttachment.
        """
        self.method = "GET"
        entity = ItemAttachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, item_attachment):
        """Updates the specified ItemAttachment.
        
        Args:
            item_attachment (:class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`):
                The ItemAttachment to update.

        Returns:
            :class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`:
                The updated ItemAttachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ItemAttachment(json.loads(self.send(item_attachment).content))
        self._initialize_collection_properties(entity)
        return entity

