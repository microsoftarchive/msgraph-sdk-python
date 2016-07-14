# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .file_attachment_request import FileAttachmentRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class FileAttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the FileAttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the FileAttachmentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(FileAttachmentRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the FileAttachmentRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`FileAttachmentRequest<msgraph.request.file_attachment_request.FileAttachmentRequest>`:
                The FileAttachmentRequest
        """
        req = FileAttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified FileAttachment."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified FileAttachment."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified FileAttachment.
        
        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified FileAttachment in async.

        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, file_attachment):
        """Updates the specified FileAttachment.
        
        Args:
            file_attachment (:class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment
        """
        return self.request().update(file_attachment)

    @asyncio.coroutine
    def update_async(self, file_attachment):
        """Updates the specified FileAttachment in async
        
        Args:
            file_attachment (:class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Returns:
            :class:`FileAttachment<msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment.
        """
        entity = yield from self.request().update_async(file_attachment)
        return entity

