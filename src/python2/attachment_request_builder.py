# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .attachment_request import AttachmentRequest
from ..request_builder_base import RequestBuilderBase


class AttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the AttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the AttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(AttachmentRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the AttachmentRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`AttachmentRequest<microsoft.msgraph.request.attachment_request.AttachmentRequest>`:
                The AttachmentRequest
        """
        req = AttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Attachment."""
        self.request().delete()

    def get(self):
        """Gets the specified Attachment.
        
        Returns:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The Attachment.
        """
        return self.request().get()

    def update(self, attachment):
        """Updates the specified Attachment.
        
        Args:
            attachment (:class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`):
                The Attachment to update.

        Returns:
            :class:`Attachment<microsoft.msgraph.model.attachment.Attachment>`:
                The updated Attachment
        """
        return self.request().update(attachment)

    @property
    def file_attachment(self):
        """The file_attachment for the AttachmentRequestBuilder

        Returns:
            :class:`FileAttachmentRequestBuilder<microsoft.msgraph.request.file_attachment_request.FileAttachmentRequestBuilder>`:
                A request builder created from the AttachmentRequestBuilder
        """
        return FileAttachmentRequestBuilder(self.append_to_request_url("fileAttachment"), self._client)

    @property
    def item_attachment(self):
        """The item_attachment for the AttachmentRequestBuilder

        Returns:
            :class:`ItemAttachmentRequestBuilder<microsoft.msgraph.request.item_attachment_request.ItemAttachmentRequestBuilder>`:
                A request builder created from the AttachmentRequestBuilder
        """
        return ItemAttachmentRequestBuilder(self.append_to_request_url("itemAttachment"), self._client)

    @property
    def reference_attachment(self):
        """The reference_attachment for the AttachmentRequestBuilder

        Returns:
            :class:`ReferenceAttachmentRequestBuilder<microsoft.msgraph.request.reference_attachment_request.ReferenceAttachmentRequestBuilder>`:
                A request builder created from the AttachmentRequestBuilder
        """
        return ReferenceAttachmentRequestBuilder(self.append_to_request_url("referenceAttachment"), self._client)


