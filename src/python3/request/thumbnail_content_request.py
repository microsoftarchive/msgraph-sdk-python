# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..model.thumbnail import Thumbnail
import json
import asyncio


class ThumbnailContentRequest(RequestBase):
    def __init__(self, request_url, client, options):
        """Initialize the ThumbnailContentRequest

        Args:
            request_url (str): The url to perform the ThumbnailContentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailContentRequest, self).__init__(request_url, client, options)

    def download(self, content_local_path):
        """Downloads the specified Thumbnail.
        
        Args:
            content_local_path (str):
                The path where the Thumbnail should be downloaded to
        """
        self.download_item(content_local_path)

    @asyncio.coroutine
    def download_async(self, content_local_path):
        """
        Downloads the specified Thumbnail in async.
        
        Args:
            content_local_path (str):
                The path where the Thumbnail should be downloaded to
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.download,
                                                    content_local_path)
        yield from future

class ThumbnailContentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailContentRequestBuilder
        
        Args:
            request_url (str): The request URL to initialize
                the ThumbnailContentRequestBuilder at
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client to use for requests made by the
                ThumbnailContentRequestBuilder
        """
        super(ThumbnailContentRequestBuilder, self).__init__(request_url, client)

    def request(self):
        """Builds the ThumbnailContentRequest

        Returns:
            :class:`ThumbnailContentRequest<msgraph.request.thumbnail_content.ThumbnailContentRequest>`:
                The ThumbnailContentRequest
        """
        return ThumbnailContentRequest(self._request_url, self._client, None)
