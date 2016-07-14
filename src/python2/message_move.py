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


class MessageMoveRequest(RequestBase):

    def __init__(self, request_url, client, options, destination_id=None):
        super(MessageMoveRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if destination_id:
            self.body_options["DestinationId"] = destination_id

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`Message<microsoft.msgraph.model.message.Message>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = Message(json.loads(self.send(self.body_options).content))
        return entity



class MessageMoveRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, destination_id=None):
        super(MessageMoveRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["DestinationId"] = destination_id

    def request(self, options=None):
        """Builds the request for the MessageMove
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`MessageMoveRequest<microsoft.msgraph.request.message_move.MessageMoveRequest>`:
                The request
        """
        req = MessageMoveRequest(self._request_url, self._client, options, destination_id=self._method_options["DestinationId"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Message<microsoft.msgraph.model.message.Message>`:
            The resulting Message from the operation
        """
        return self.request().post()

