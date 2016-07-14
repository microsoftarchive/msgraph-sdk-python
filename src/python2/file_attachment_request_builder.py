# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .file_attachment_request import FileAttachmentRequest
from ..request_builder_base import RequestBuilderBase


class FileAttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the FileAttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the FileAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`FileAttachmentRequest<microsoft.msgraph.request.file_attachment_request.FileAttachmentRequest>`:
                The FileAttachmentRequest
        """
        req = FileAttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified FileAttachment."""
        self.request().delete()

    def get(self):
        """Gets the specified FileAttachment.
        
        Returns:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment.
        """
        return self.request().get()

    def update(self, file_attachment):
        """Updates the specified FileAttachment.
        
        Args:
            file_attachment (:class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`):
                The FileAttachment to update.

        Returns:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The updated FileAttachment
        """
        return self.request().update(file_attachment)


