# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .event_message_request import EventMessageRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import event_request_builder


class EventMessageRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the EventMessageRequestBuilder

        Args:
            request_url (str): The url to perform the EventMessageRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(EventMessageRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the EventMessageRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EventMessageRequest<msgraph.request.event_message_request.EventMessageRequest>`:
                The EventMessageRequest
        """
        req = EventMessageRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified EventMessage."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified EventMessage."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified EventMessage.
        
        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified EventMessage in async.

        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, event_message):
        """Updates the specified EventMessage.
        
        Args:
            event_message (:class:`EventMessage<msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The updated EventMessage
        """
        return self.request().update(event_message)

    @asyncio.coroutine
    def update_async(self, event_message):
        """Updates the specified EventMessage in async
        
        Args:
            event_message (:class:`EventMessage<msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Returns:
            :class:`EventMessage<msgraph.model.event_message.EventMessage>`:
                The updated EventMessage.
        """
        entity = yield from self.request().update_async(event_message)
        return entity

    @property
    def event(self):
        """The event for the EventMessageRequestBuilder

        Returns: 
            :class:`EventRequestBuilder<msgraph.request.event_request.EventRequestBuilder>`:
                A request builder created from the EventMessageRequestBuilder
        """
        return event_request_builder.EventRequestBuilder(self.append_to_request_url("event"), self._client)


