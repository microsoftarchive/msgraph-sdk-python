# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.calendar import Calendar
import json
import asyncio

class CalendarRequest(RequestBase):
    """The type CalendarRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new CalendarRequest.

        Args:
            request_url (str): The url to perform the CalendarRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(CalendarRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Calendar."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Calendar."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Calendar.
        
        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The Calendar.
        """
        self.method = "GET"
        entity = Calendar(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Calendar in async.

        Yields:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The Calendar.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, calendar):
        """Updates the specified Calendar.
        
        Args:
            calendar (:class:`Calendar<msgraph.model.calendar.Calendar>`):
                The Calendar to update.

        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The updated Calendar.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Calendar(json.loads(self.send(calendar).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, calendar):
        """Updates the specified Calendar in async
        
        Args:
            calendar (:class:`Calendar<msgraph.model.calendar.Calendar>`):
                The Calendar to update.

        Yields:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The updated Calendar.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    calendar)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.events and value.events._prop_dict:
                if "events@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["events@odata.nextLink"]
                    value.events._init_next_page_request(next_page_link, self._client, None)
            if value.calendar_view and value.calendar_view._prop_dict:
                if "calendar_view@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendar_view@odata.nextLink"]
                    value.calendar_view._init_next_page_request(next_page_link, self._client, None)
