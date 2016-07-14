# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.attachment import Attachment
import json

class AttachmentRequest(RequestBase):
    """The type AttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new AttachmentRequest.

        Args:
            request_url (str): The url to perform the AttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(AttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Attachment."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Attachment.
        
        Returns:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The Attachment.
        """
        self.method = "GET"
        entity = Attachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, attachment):
        """Updates the specified Attachment.
        
        Args:
            attachment (:class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`):
                The Attachment to update.

        Returns:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The updated Attachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Attachment(json.loads(self.send(attachment).content))
        self._initialize_collection_properties(entity)
        return entity

