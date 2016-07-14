# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..model.drive_item import DriveItem
import json
import asyncio


class DriveItemContentRequest(RequestBase):
    def __init__(self, request_url, client, options):
        """Initialize the DriveItemContentRequest

        Args:
            request_url (str): The url to perform the DriveItemContentRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DriveItemContentRequest, self).__init__(request_url, client, options)

    def upload(self, content_local_path):
        """Uploads the file using PUT
        
        Args:
            content_local_path (str):
                The path to the local file to upload.

        Returns: 
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The created DriveItem.
        """
        self.method = "PUT"
        entity_response = self.send(path=content_local_path)
        entity = DriveItem(json.loads(entity_response.content))
        return entity

    @asyncio.coroutine
    def upload_async(self, content_local_path):
        """Uploads the file using PUT in async
        
        Args:
            content_local_path (str): 
                The path to the local file to upload.

        Yields: 
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The created DriveItem.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.put,
                                                    content_local_path)
        entity = yield from future
        return entity

    def download(self, content_local_path):
        """Downloads the specified DriveItem.
        
        Args:
            content_local_path (str):
                The path where the DriveItem should be downloaded to
        """
        self.download_item(content_local_path)

    @asyncio.coroutine
    def download_async(self, content_local_path):
        """
        Downloads the specified DriveItem in async.
        
        Args:
            content_local_path (str):
                The path where the DriveItem should be downloaded to
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.download,
                                                    content_local_path)
        yield from future

class DriveItemContentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DriveItemContentRequestBuilder
        
        Args:
            request_url (str): The request URL to initialize
                the DriveItemContentRequestBuilder at
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client to use for requests made by the
                DriveItemContentRequestBuilder
        """
        super(DriveItemContentRequestBuilder, self).__init__(request_url, client)

    def request(self):
        """Builds the DriveItemContentRequest

        Returns:
            :class:`DriveItemContentRequest<msgraph.request.drive_item_content.DriveItemContentRequest>`:
                The DriveItemContentRequest
        """
        return DriveItemContentRequest(self._request_url, self._client, None)
