# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.conversation import Conversation
import json

class ConversationRequest(RequestBase):
    """The type ConversationRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ConversationRequest.

        Args:
            request_url (str): The url to perform the ConversationRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ConversationRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Conversation."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Conversation.
        
        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The Conversation.
        """
        self.method = "GET"
        entity = Conversation(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, conversation):
        """Updates the specified Conversation.
        
        Args:
            conversation (:class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`):
                The Conversation to update.

        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The updated Conversation.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Conversation(json.loads(self.send(conversation).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.threads and value.threads._prop_dict:
                if "threads@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["threads@odata.nextLink"]
                    value.threads._init_next_page_request(next_page_link, self._client, None)
