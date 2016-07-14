# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .calendar_request import CalendarRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import event_collection


class CalendarRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the CalendarRequestBuilder

        Args:
            request_url (str): The url to perform the CalendarRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(CalendarRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the CalendarRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`CalendarRequest<msgraph.request.calendar_request.CalendarRequest>`:
                The CalendarRequest
        """
        req = CalendarRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Calendar."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Calendar."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Calendar.
        
        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The Calendar.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Calendar in async.

        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The Calendar.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, calendar):
        """Updates the specified Calendar.
        
        Args:
            calendar (:class:`Calendar<msgraph.model.calendar.Calendar>`):
                The Calendar to update.

        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The updated Calendar
        """
        return self.request().update(calendar)

    @asyncio.coroutine
    def update_async(self, calendar):
        """Updates the specified Calendar in async
        
        Args:
            calendar (:class:`Calendar<msgraph.model.calendar.Calendar>`):
                The Calendar to update.

        Returns:
            :class:`Calendar<msgraph.model.calendar.Calendar>`:
                The updated Calendar.
        """
        entity = yield from self.request().update_async(calendar)
        return entity

    @property
    def events(self):
        """The events for the CalendarRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.events_collection.EventCollectionRequestBuilder>`:
                A request builder created from the CalendarRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("events"), self._client)

    @property
    def calendar_view(self):
        """The calendar_view for the CalendarRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.calendar_view_collection.EventCollectionRequestBuilder>`:
                A request builder created from the CalendarRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("calendarView"), self._client)

