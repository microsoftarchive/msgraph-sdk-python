# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.conversation import Conversation
import json
import asyncio

class ConversationRequest(RequestBase):
    """The type ConversationRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ConversationRequest.

        Args:
            request_url (str): The url to perform the ConversationRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ConversationRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Conversation."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Conversation."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Conversation.
        
        Returns:
            :class:`Conversation<msgraph.model.conversation.Conversation>`:
                The Conversation.
        """
        self.method = "GET"
        entity = Conversation(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Conversation in async.

        Yields:
            :class:`Conversation<msgraph.model.conversation.Conversation>`:
                The Conversation.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, conversation):
        """Updates the specified Conversation.
        
        Args:
            conversation (:class:`Conversation<msgraph.model.conversation.Conversation>`):
                The Conversation to update.

        Returns:
            :class:`Conversation<msgraph.model.conversation.Conversation>`:
                The updated Conversation.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Conversation(json.loads(self.send(conversation).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, conversation):
        """Updates the specified Conversation in async
        
        Args:
            conversation (:class:`Conversation<msgraph.model.conversation.Conversation>`):
                The Conversation to update.

        Yields:
            :class:`Conversation<msgraph.model.conversation.Conversation>`:
                The updated Conversation.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    conversation)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.threads and value.threads._prop_dict:
                if "threads@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["threads@odata.nextLink"]
                    value.threads._init_next_page_request(next_page_link, self._client, None)
