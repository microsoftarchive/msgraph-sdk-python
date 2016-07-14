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


class UserSendMailRequest(RequestBase):

    def __init__(self, request_url, client, options, message, save_to_sent_items=None):
        super(UserSendMailRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if message:
            self.body_options["Message"] = message
        if save_to_sent_items:
            self.body_options["SaveToSentItems"] = save_to_sent_items

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



class UserSendMailRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, message, save_to_sent_items=None):
        super(UserSendMailRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["Message"] = message._prop_dict
        self._method_options["SaveToSentItems"] = save_to_sent_items

    def request(self, options=None):
        """Builds the request for the UserSendMail
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`UserSendMailRequest<microsoft.msgraph.request.user_send_mail.UserSendMailRequest>`:
                The request
        """
        req = UserSendMailRequest(self._request_url, self._client, options, self._method_options["Message"], save_to_sent_items=self._method_options["SaveToSentItems"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`None<microsoft.msgraph.model.none.None>`:
            The resulting None from the operation
        """
        return self.request().post()

