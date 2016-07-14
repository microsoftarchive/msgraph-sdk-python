# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

#from ..model.drive_item import DriveItem
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class DriveItemCopyRequest(RequestBase):

    def __init__(self, request_url, client, options, name=None, parent_reference=None):
        super(DriveItemCopyRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if name:
            self.body_options["name"] = name
        if parent_reference:
            self.body_options["parentReference"] = parent_reference

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = DriveItem(json.loads(self.send(self.body_options).content))
        return entity

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The resulting entity from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        entity = yield from future
        return entity


class DriveItemCopyRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, name=None, parent_reference=None):
        super(DriveItemCopyRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["name"] = name
        self._method_options["parentReference"] = parent_reference._prop_dict

    def request(self, options=None):
        """Builds the request for the DriveItemCopy
        
        Args:
            options (list of :class:`Option<msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`DriveItemCopyRequest<msgraph.request.drive_item_copy.DriveItemCopyRequest>`:
                The request
        """
        req = DriveItemCopyRequest(self._request_url, self._client, options, name=self._method_options["name"], parent_reference=self._method_options["parentReference"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
            The resulting DriveItem from the operation
        """
        return self.request().post()

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The resulting DriveItem from the operation
        """
        entity = yield from self.request().post_async()
        return entity

