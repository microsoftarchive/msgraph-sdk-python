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


class EventSnoozeReminderRequest(RequestBase):

    def __init__(self, request_url, client, options, new_reminder_time):
        super(EventSnoozeReminderRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if new_reminder_time:
            self.body_options["NewReminderTime"] = new_reminder_time

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



class EventSnoozeReminderRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, new_reminder_time):
        super(EventSnoozeReminderRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["NewReminderTime"] = new_reminder_time._prop_dict

    def request(self, options=None):
        """Builds the request for the EventSnoozeReminder
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`EventSnoozeReminderRequest<microsoft.msgraph.request.event_snooze_reminder.EventSnoozeReminderRequest>`:
                The request
        """
        req = EventSnoozeReminderRequest(self._request_url, self._client, options, self._method_options["NewReminderTime"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`None<microsoft.msgraph.model.none.None>`:
            The resulting None from the operation
        """
        return self.request().post()

