# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.reference_attachment import ReferenceAttachment
import json
import asyncio

class ReferenceAttachmentRequest(RequestBase):
    """The type ReferenceAttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ReferenceAttachmentRequest.

        Args:
            request_url (str): The url to perform the ReferenceAttachmentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ReferenceAttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ReferenceAttachment."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ReferenceAttachment."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified ReferenceAttachment.
        
        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        self.method = "GET"
        entity = ReferenceAttachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ReferenceAttachment in async.

        Yields:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, reference_attachment):
        """Updates the specified ReferenceAttachment.
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ReferenceAttachment(json.loads(self.send(reference_attachment).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, reference_attachment):
        """Updates the specified ReferenceAttachment in async
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Yields:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    reference_attachment)
        entity = yield from future
        return entity

