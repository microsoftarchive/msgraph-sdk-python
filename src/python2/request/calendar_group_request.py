# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.calendar_group import CalendarGroup
import json

class CalendarGroupRequest(RequestBase):
    """The type CalendarGroupRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new CalendarGroupRequest.

        Args:
            request_url (str): The url to perform the CalendarGroupRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(CalendarGroupRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified CalendarGroup."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified CalendarGroup.
        
        Returns:
            :class:`CalendarGroup<microsoft.msgraph.model.calendar_group.CalendarGroup>`:
                The CalendarGroup.
        """
        self.method = "GET"
        entity = CalendarGroup(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, calendar_group):
        """Updates the specified CalendarGroup.
        
        Args:
            calendar_group (:class:`CalendarGroup<microsoft.msgraph.model.calendar_group.CalendarGroup>`):
                The CalendarGroup to update.

        Returns:
            :class:`CalendarGroup<microsoft.msgraph.model.calendar_group.CalendarGroup>`:
                The updated CalendarGroup.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = CalendarGroup(json.loads(self.send(calendar_group).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.calendars and value.calendars._prop_dict:
                if "calendars@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendars@odata.nextLink"]
                    value.calendars._init_next_page_request(next_page_link, self._client, None)
