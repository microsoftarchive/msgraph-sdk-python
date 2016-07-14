# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .subscribed_sku_request import SubscribedSkuRequest
from ..request_builder_base import RequestBuilderBase


class SubscribedSkuRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the SubscribedSkuRequestBuilder

        Args:
            request_url (str): The url to perform the SubscribedSkuRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(SubscribedSkuRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the SubscribedSkuRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`SubscribedSkuRequest<microsoft.msgraph.request.subscribed_sku_request.SubscribedSkuRequest>`:
                The SubscribedSkuRequest
        """
        req = SubscribedSkuRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified SubscribedSku."""
        self.request().delete()

    def get(self):
        """Gets the specified SubscribedSku.
        
        Returns:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The SubscribedSku.
        """
        return self.request().get()

    def update(self, subscribed_sku):
        """Updates the specified SubscribedSku.
        
        Args:
            subscribed_sku (:class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`):
                The SubscribedSku to update.

        Returns:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The updated SubscribedSku
        """
        return self.request().update(subscribed_sku)


