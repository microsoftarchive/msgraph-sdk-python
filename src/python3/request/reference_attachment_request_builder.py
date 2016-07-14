# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .reference_attachment_request import ReferenceAttachmentRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class ReferenceAttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ReferenceAttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the ReferenceAttachmentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ReferenceAttachmentRequest<msgraph.request.reference_attachment_request.ReferenceAttachmentRequest>`:
                The ReferenceAttachmentRequest
        """
        req = ReferenceAttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified ReferenceAttachment."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ReferenceAttachment."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified ReferenceAttachment.
        
        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ReferenceAttachment in async.

        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, reference_attachment):
        """Updates the specified ReferenceAttachment.
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment
        """
        return self.request().update(reference_attachment)

    @asyncio.coroutine
    def update_async(self, reference_attachment):
        """Updates the specified ReferenceAttachment in async
        
        Args:
            reference_attachment (:class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`):
                The ReferenceAttachment to update.

        Returns:
            :class:`ReferenceAttachment<msgraph.model.reference_attachment.ReferenceAttachment>`:
                The updated ReferenceAttachment.
        """
        entity = yield from self.request().update_async(reference_attachment)
        return entity

