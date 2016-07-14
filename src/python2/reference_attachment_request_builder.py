# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .reference_attachment_request import ReferenceAttachmentRequest
from ..request_builder_base import RequestBuilderBase


class ReferenceAttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ReferenceAttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the ReferenceAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ReferenceAttachmentRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ReferenceAttachmentRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ReferenceAttachmentRequest<microsoft.msgraph.request.reference_attachment_request.ReferenceAttachmentRequest>`:
                The ReferenceAttachmentRequest
        """
        req = ReferenceAttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ReferenceAttachment."""
        self.request().delete()

    def get(self):
        """Gets the specified ReferenceAttachment.
        
        Returns:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        return self.request().get()

    def update(self, reference_attachment):
        """Updates the specified ReferenceAttachment.
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Returns:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment
        """
        return self.request().update(reference_attachment)


