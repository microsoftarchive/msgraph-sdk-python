# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.event import Event
import json
import asyncio

class EventRequest(RequestBase):
    """The type EventRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new EventRequest.

        Args:
            request_url (str): The url to perform the EventRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EventRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Event."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Event."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Event.
        
        Returns:
            :class:`Event<msgraph.model.event.Event>`:
                The Event.
        """
        self.method = "GET"
        entity = Event(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Event in async.

        Yields:
            :class:`Event<msgraph.model.event.Event>`:
                The Event.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, event):
        """Updates the specified Event.
        
        Args:
            event (:class:`Event<msgraph.model.event.Event>`):
                The Event to update.

        Returns:
            :class:`Event<msgraph.model.event.Event>`:
                The updated Event.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Event(json.loads(self.send(event).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, event):
        """Updates the specified Event in async
        
        Args:
            event (:class:`Event<msgraph.model.event.Event>`):
                The Event to update.

        Yields:
            :class:`Event<msgraph.model.event.Event>`:
                The updated Event.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    event)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.attendees and value.attendees._prop_dict:
                if "attendees@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["attendees@odata.nextLink"]
                    value.attendees._init_next_page_request(next_page_link, self._client, None)
            if value.instances and value.instances._prop_dict:
                if "instances@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["instances@odata.nextLink"]
                    value.instances._init_next_page_request(next_page_link, self._client, None)
            if value.extensions and value.extensions._prop_dict:
                if "extensions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["extensions@odata.nextLink"]
                    value.extensions._init_next_page_request(next_page_link, self._client, None)
            if value.attachments and value.attachments._prop_dict:
                if "attachments@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["attachments@odata.nextLink"]
                    value.attachments._init_next_page_request(next_page_link, self._client, None)
