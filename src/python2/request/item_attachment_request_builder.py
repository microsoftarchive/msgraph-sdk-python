# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .item_attachment_request import ItemAttachmentRequest
from ..request_builder_base import RequestBuilderBase
from ..request import outlook_item_request_builder


class ItemAttachmentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ItemAttachmentRequestBuilder

        Args:
            request_url (str): The url to perform the ItemAttachmentRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ItemAttachmentRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ItemAttachmentRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ItemAttachmentRequest<microsoft.msgraph.request.item_attachment_request.ItemAttachmentRequest>`:
                The ItemAttachmentRequest
        """
        req = ItemAttachmentRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ItemAttachment."""
        self.request().delete()

    def get(self):
        """Gets the specified ItemAttachment.
        
        Returns:
            :class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`:
                The ItemAttachment.
        """
        return self.request().get()

    def update(self, item_attachment):
        """Updates the specified ItemAttachment.
        
        Args:
            item_attachment (:class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`):
                The ItemAttachment to update.

        Returns:
            :class:`ItemAttachment<microsoft.msgraph.model.item_attachment.ItemAttachment>`:
                The updated ItemAttachment
        """
        return self.request().update(item_attachment)


    @property
    def item(self):
        """The item for the ItemAttachmentRequestBuilder

        Returns: 
            :class:`OutlookItemRequestBuilder<microsoft.msgraph.request.outlook_item_request.OutlookItemRequestBuilder>`:
                A request builder created from the ItemAttachmentRequestBuilder
        """
        return outlook_item_request_builder.OutlookItemRequestBuilder(self.append_to_request_url("item"), self._client)


