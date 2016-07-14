# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.reference_attachment import ReferenceAttachment
import json

class ReferenceAttachmentRequest(RequestBase):
    """The type ReferenceAttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ReferenceAttachmentRequest.

        Args:
            request_url (str): The url to perform the ReferenceAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ReferenceAttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ReferenceAttachment."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified ReferenceAttachment.
        
        Returns:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        self.method = "GET"
        entity = ReferenceAttachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, reference_attachment):
        """Updates the specified ReferenceAttachment.
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Returns:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ReferenceAttachment(json.loads(self.send(reference_attachment).content))
        self._initialize_collection_properties(entity)
        return entity

