# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.file_attachment import FileAttachment
import json

class FileAttachmentRequest(RequestBase):
    """The type FileAttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new FileAttachmentRequest.

        Args:
            request_url (str): The url to perform the FileAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(FileAttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified FileAttachment."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified FileAttachment.
        
        Returns:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        self.method = "GET"
        entity = FileAttachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, file_attachment):
        """Updates the specified FileAttachment.
        
        Args:
            file_attachment (:class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Returns:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = FileAttachment(json.loads(self.send(file_attachment).content))
        self._initialize_collection_properties(entity)
        return entity

