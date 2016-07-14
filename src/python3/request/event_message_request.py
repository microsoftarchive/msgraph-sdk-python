# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.event_message import EventMessage
import json
import asyncio

class EventMessageRequest(RequestBase):
    """The type EventMessageRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new EventMessageRequest.

        Args:
            request_url (str): The url to perform the EventMessageRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EventMessageRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified EventMessage."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified EventMessage."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified EventMessage.
        
        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        self.method = "GET"
        entity = EventMessage(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified EventMessage in async.

        Yields:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, event_message):
        """Updates the specified EventMessage.
        
        Args:
            event_message (:class:`EventMessage<msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The updated EventMessage.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = EventMessage(json.loads(self.send(event_message).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, event_message):
        """Updates the specified EventMessage in async
        
        Args:
            event_message (:class:`EventMessage<msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Yields:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The updated EventMessage.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    event_message)
        entity = yield from future
        return entity

