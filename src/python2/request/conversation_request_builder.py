# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .conversation_request import ConversationRequest
from ..request_builder_base import RequestBuilderBase
from ..request import conversation_thread_collection


class ConversationRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ConversationRequestBuilder

        Args:
            request_url (str): The url to perform the ConversationRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ConversationRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ConversationRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ConversationRequest<microsoft.msgraph.request.conversation_request.ConversationRequest>`:
                The ConversationRequest
        """
        req = ConversationRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Conversation."""
        self.request().delete()

    def get(self):
        """Gets the specified Conversation.
        
        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The Conversation.
        """
        return self.request().get()

    def update(self, conversation):
        """Updates the specified Conversation.
        
        Args:
            conversation (:class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`):
                The Conversation to update.

        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The updated Conversation
        """
        return self.request().update(conversation)


    @property
    def threads(self):
        """The threads for the ConversationRequestBuilder

        Returns: 
            :class:`ConversationThreadCollectionRequestBuilder<microsoft.msgraph.request.threads_collection.ConversationThreadCollectionRequestBuilder>`:
                A request builder created from the ConversationRequestBuilder
        """
        return conversation_thread_collection.ConversationThreadCollectionRequestBuilder(self.append_to_request_url("threads"), self._client)

