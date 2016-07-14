# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.file_attachment import FileAttachment
import json
import asyncio

class FileAttachmentRequest(RequestBase):
    """The type FileAttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new FileAttachmentRequest.

        Args:
            request_url (str): The url to perform the FileAttachmentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(FileAttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified FileAttachment."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified FileAttachment."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified FileAttachment.
        
        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        self.method = "GET"
        entity = FileAttachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified FileAttachment in async.

        Yields:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, file_attachment):
        """Updates the specified FileAttachment.
        
        Args:
            file_attachment (:class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = FileAttachment(json.loads(self.send(file_attachment).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, file_attachment):
        """Updates the specified FileAttachment in async
        
        Args:
            file_attachment (:class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Yields:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    file_attachment)
        entity = yield from future
        return entity

