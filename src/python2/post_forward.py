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


class PostForwardRequest(RequestBase):

    def __init__(self, request_url, client, options, to_recipients, comment=None):
        super(PostForwardRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if to_recipients:
            self.body_options["ToRecipients"] = to_recipients
        if comment:
            self.body_options["Comment"] = comment

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



class PostForwardRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, to_recipients, comment=None):
        super(PostForwardRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["ToRecipients"] = to_recipients._prop_dict
        self._method_options["Comment"] = comment

    def request(self, options=None):
        """Builds the request for the PostForward
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`PostForwardRequest<microsoft.msgraph.request.post_forward.PostForwardRequest>`:
                The request
        """
        req = PostForwardRequest(self._request_url, self._client, options, self._method_options["ToRecipients"], comment=self._method_options["Comment"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`None<microsoft.msgraph.model.none.None>`:
            The resulting None from the operation
        """
        return self.request().post()

