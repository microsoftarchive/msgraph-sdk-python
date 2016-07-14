# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json


class MessageForwardRequest(RequestBase):

    def __init__(self, request_url, client, options, comment=None, to_recipients=None):
        super(MessageForwardRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if comment:
            self.body_options["Comment"] = comment
        if to_recipients:
            self.body_options["ToRecipients"] = to_recipients

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`None<microsoft.msgraph.model.none.None>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = None(json.loads(self.send(self.body_options).content))
        return entity



class MessageForwardRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, comment=None, to_recipients=None):
        super(MessageForwardRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["Comment"] = comment
        self._method_options["ToRecipients"] = to_recipients._prop_dict

    def request(self, options=None):
        """Builds the request for the MessageForward
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`MessageForwardRequest<microsoft.msgraph.request.message_forward.MessageForwardRequest>`:
                The request
        """
        req = MessageForwardRequest(self._request_url, self._client, options, comment=self._method_options["Comment"], to_recipients=self._method_options["ToRecipients"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`None<microsoft.msgraph.model.none.None>`:
            The resulting None from the operation
        """
        return self.request().post()

