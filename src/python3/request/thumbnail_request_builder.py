# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .thumbnail_request import ThumbnailRequest
from ..request_builder_base import RequestBuilderBase
from ..request.thumbnail_content_request import ThumbnailContentRequestBuilder
import asyncio



class ThumbnailRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailRequestBuilder

        Args:
            request_url (str): The url to perform the ThumbnailRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ThumbnailRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ThumbnailRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ThumbnailRequest<msgraph.request.thumbnail_request.ThumbnailRequest>`:
                The ThumbnailRequest
        """
        req = ThumbnailRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Thumbnail."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Thumbnail."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Thumbnail.
        
        Returns:
            :class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Thumbnail in async.

        Returns:
            :class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, thumbnail):
        """Updates the specified Thumbnail.
        
        Args:
            thumbnail (:class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`:
                The updated Thumbnail
        """
        return self.request().update(thumbnail)

    @asyncio.coroutine
    def update_async(self, thumbnail):
        """Updates the specified Thumbnail in async
        
        Args:
            thumbnail (:class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<msgraph.model.thumbnail.Thumbnail>`:
                The updated Thumbnail.
        """
        entity = yield from self.request().update_async(thumbnail)
        return entity

    def download(self, local_path):
        """Downloads the specified entity.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        return self.content.request().download(local_path)

    @asyncio.coroutine
    def download_async(self, local_path):
        """Downloads the specified entity in async.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        entity = yield from self.content.request().download_async(local_path)
        return entity

    @property
    def content(self):
        """The content for the ThumbnailRequestBuilder

        Returns: 
            :class:`ThumbnailContentRequestBuilder<msgraph.request.thumbnail_content.ThumbnailContentRequestBuilder>`:
                A request builder created from the ThumbnailRequestBuilder
        """
        return ThumbnailContentRequestBuilder(self.append_to_request_url("content"), self._client)

