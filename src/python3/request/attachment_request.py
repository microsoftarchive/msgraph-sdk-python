# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.attachment import Attachment
import json
import asyncio

class AttachmentRequest(RequestBase):
    """The type AttachmentRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new AttachmentRequest.

        Args:
            request_url (str): The url to perform the AttachmentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(AttachmentRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Attachment."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Attachment."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Attachment.
        
        Returns:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The Attachment.
        """
        self.method = "GET"
        entity = Attachment(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Attachment in async.

        Yields:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The Attachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, attachment):
        """Updates the specified Attachment.
        
        Args:
            attachment (:class:`Attachment<msgraph.model.attachment.Attachment>`):
                The Attachment to update.

        Returns:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The updated Attachment.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Attachment(json.loads(self.send(attachment).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, attachment):
        """Updates the specified Attachment in async
        
        Args:
            attachment (:class:`Attachment<msgraph.model.attachment.Attachment>`):
                The Attachment to update.

        Yields:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The updated Attachment.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    attachment)
        entity = yield from future
        return entity

