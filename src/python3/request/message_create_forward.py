# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

#from ..model.message import Message
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class MessageCreateForwardRequest(RequestBase):

    def __init__(self, request_url, client, options):
        super(MessageCreateForwardRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Message<msgraph.model.message.Message>`:
                The resulting entity from the operation
        """
        entity = Message(json.loads(self.send().content))
        return entity

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`Message<msgraph.model.message.Message>`:
                The resulting entity from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        entity = yield from future
        return entity


class MessageCreateForwardRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        super(MessageCreateForwardRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the request for the MessageCreateForward
        
        Args:
            options (list of :class:`Option<msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`MessageCreateForwardRequest<msgraph.request.message_create_forward.MessageCreateForwardRequest>`:
                The request
        """
        req = MessageCreateForwardRequest(self._request_url, self._client, options)
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Message<msgraph.model.message.Message>`:
            The resulting Message from the operation
        """
        return self.request().post()

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`Message<msgraph.model.message.Message>`:
                The resulting Message from the operation
        """
        entity = yield from self.request().post_async()
        return entity

