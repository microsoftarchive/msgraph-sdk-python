# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

#from ..model.permission import Permission
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class DriveItemCreateLinkRequest(RequestBase):

    def __init__(self, request_url, client, options, type, scope=None):
        super(DriveItemCreateLinkRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if type:
            self.body_options["type"] = type
        if scope:
            self.body_options["scope"] = scope

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`Permission<msgraph.model.permission.Permission>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = Permission(json.loads(self.send(self.body_options).content))
        return entity

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The resulting entity from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        entity = yield from future
        return entity


class DriveItemCreateLinkRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, type, scope=None):
        super(DriveItemCreateLinkRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["type"] = type
        self._method_options["scope"] = scope

    def request(self, options=None):
        """Builds the request for the DriveItemCreateLink
        
        Args:
            options (list of :class:`Option<msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`DriveItemCreateLinkRequest<msgraph.request.drive_item_create_link.DriveItemCreateLinkRequest>`:
                The request
        """
        req = DriveItemCreateLinkRequest(self._request_url, self._client, options, self._method_options["type"], scope=self._method_options["scope"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
            The resulting Permission from the operation
        """
        return self.request().post()

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The resulting Permission from the operation
        """
        entity = yield from self.request().post_async()
        return entity

