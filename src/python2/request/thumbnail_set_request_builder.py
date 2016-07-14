# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .thumbnail_set_request import ThumbnailSetRequest
from ..request_builder_base import RequestBuilderBase


class ThumbnailSetRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailSetRequestBuilder

        Args:
            request_url (str): The url to perform the ThumbnailSetRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ThumbnailSetRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ThumbnailSetRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ThumbnailSetRequest<microsoft.msgraph.request.thumbnail_set_request.ThumbnailSetRequest>`:
                The ThumbnailSetRequest
        """
        req = ThumbnailSetRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ThumbnailSet."""
        self.request().delete()

    def get(self):
        """Gets the specified ThumbnailSet.
        
        Returns:
            :class:`ThumbnailSet<microsoft.msgraph.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet.
        """
        return self.request().get()

    def update(self, thumbnail_set):
        """Updates the specified ThumbnailSet.
        
        Args:
            thumbnail_set (:class:`ThumbnailSet<microsoft.msgraph.model.thumbnail_set.ThumbnailSet>`):
                The ThumbnailSet to update.

        Returns:
            :class:`ThumbnailSet<microsoft.msgraph.model.thumbnail_set.ThumbnailSet>`:
                The updated ThumbnailSet
        """
        return self.request().update(thumbnail_set)


    @property
    def large(self):
        """The large for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<microsoft.msgraph.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("large"), self._client)

    @property
    def medium(self):
        """The medium for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<microsoft.msgraph.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("medium"), self._client)

    @property
    def small(self):
        """The small for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<microsoft.msgraph.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("small"), self._client)

    @property
    def source(self):
        """The source for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<microsoft.msgraph.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("source"), self._client)

