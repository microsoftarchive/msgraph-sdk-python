# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.event_message import EventMessage
import json

class EventMessageRequest(RequestBase):
    """The type EventMessageRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new EventMessageRequest.

        Args:
            request_url (str): The url to perform the EventMessageRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EventMessageRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified EventMessage."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified EventMessage.
        
        Returns:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The EventMessage.
        """
        self.method = "GET"
        entity = EventMessage(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, event_message):
        """Updates the specified EventMessage.
        
        Args:
            event_message (:class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`):
                The EventMessage to update.

        Returns:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The updated EventMessage.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = EventMessage(json.loads(self.send(event_message).content))
        self._initialize_collection_properties(entity)
        return entity

