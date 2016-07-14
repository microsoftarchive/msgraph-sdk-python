# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

#from ..model.drive_item import DriveItem
from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio
from ..request import drive_item_collection 


class DriveItemDeltaRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, token=None):
        super(DriveItemDeltaRequest, self).__init__(request_url, client, options)
        self.method = "GET"

        if token:
            self._query_options["token"] = token

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting collection page from the operation
        """
        collection_response = drive_item_collection.DriveItemCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting collection page from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_response = yield from future
        return collection_response


class DriveItemDeltaRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, token=None):
        super(DriveItemDeltaRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["token"] = token

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the request for the DriveItemDelta
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`DriveItemDeltaRequest<msgraph.request.drive_item_delta.DriveItemDeltaRequest>`:
                The request
        """
        req = DriveItemDeltaRequest(self._request_url, self._client, options, token=self._method_options["token"])
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
            The resulting DriveItemCollectionResponse from the operation
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting DriveItemCollectionResponse from the operation
        """
        collection_page = yield from self.request().get_async()
        return collection_page

