# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .event_message_request import EventMessageRequest
from ..request_builder_base import RequestBuilderBase
from ..request import event_request_builder


class EventMessageRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the EventMessageRequestBuilder

        Args:
            request_url (str): The url to perform the EventMessageRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EventMessageRequest<microsoft.msgraph.request.event_message_request.EventMessageRequest>`:
                The EventMessageRequest
        """
        req = EventMessageRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified EventMessage."""
        self.request().delete()

    def get(self):
        """Gets the specified EventMessage.
        
        Returns:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        return self.request().get()

    def update(self, event_message):
        """Updates the specified EventMessage.
        
        Args:
            event_message (:class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Returns:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The updated EventMessage
        """
        return self.request().update(event_message)


    @property
    def event(self):
        """The event for the EventMessageRequestBuilder

        Returns: 
            :class:`EventRequestBuilder<microsoft.msgraph.request.event_request.EventRequestBuilder>`:
                A request builder created from the EventMessageRequestBuilder
        """
        return event_request_builder.EventRequestBuilder(self.append_to_request_url("event"), self._client)


