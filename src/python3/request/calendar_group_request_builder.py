# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .calendar_group_request import CalendarGroupRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import calendar_collection


class CalendarGroupRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the CalendarGroupRequestBuilder

        Args:
            request_url (str): The url to perform the CalendarGroupRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(CalendarGroupRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the CalendarGroupRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`CalendarGroupRequest<msgraph.request.calendar_group_request.CalendarGroupRequest>`:
                The CalendarGroupRequest
        """
        req = CalendarGroupRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified CalendarGroup."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified CalendarGroup."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified CalendarGroup.
        
        Returns:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The CalendarGroup.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified CalendarGroup in async.

        Returns:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The CalendarGroup.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, calendar_group):
        """Updates the specified CalendarGroup.
        
        Args:
            calendar_group (:class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`):
                The CalendarGroup to update.

        Returns:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The updated CalendarGroup
        """
        return self.request().update(calendar_group)

    @asyncio.coroutine
    def update_async(self, calendar_group):
        """Updates the specified CalendarGroup in async
        
        Args:
            calendar_group (:class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`):
                The CalendarGroup to update.

        Returns:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The updated CalendarGroup.
        """
        entity = yield from self.request().update_async(calendar_group)
        return entity

    @property
    def calendars(self):
        """The calendars for the CalendarGroupRequestBuilder

        Returns: 
            :class:`CalendarCollectionRequestBuilder<msgraph.request.calendars_collection.CalendarCollectionRequestBuilder>`:
                A request builder created from the CalendarGroupRequestBuilder
        """
        return calendar_collection.CalendarCollectionRequestBuilder(self.append_to_request_url("calendars"), self._client)

