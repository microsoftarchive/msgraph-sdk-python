# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .conversation_thread_request import ConversationThreadRequest
from ..request_builder_base import RequestBuilderBase
from ..request.conversation_thread_reply import ConversationThreadReplyRequestBuilder
from ..request import post_collection


class ConversationThreadRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ConversationThreadRequestBuilder

        Args:
            request_url (str): The url to perform the ConversationThreadRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ConversationThreadRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ConversationThreadRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ConversationThreadRequest<microsoft.msgraph.request.conversation_thread_request.ConversationThreadRequest>`:
                The ConversationThreadRequest
        """
        req = ConversationThreadRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ConversationThread."""
        self.request().delete()

    def get(self):
        """Gets the specified ConversationThread.
        
        Returns:
            :class:`ConversationThread<microsoft.msgraph.model.conversation_thread.ConversationThread>`:
                The ConversationThread.
        """
        return self.request().get()

    def update(self, conversation_thread):
        """Updates the specified ConversationThread.
        
        Args:
            conversation_thread (:class:`ConversationThread<microsoft.msgraph.model.conversation_thread.ConversationThread>`):
                The ConversationThread to update.

        Returns:
            :class:`ConversationThread<microsoft.msgraph.model.conversation_thread.ConversationThread>`:
                The updated ConversationThread
        """
        return self.request().update(conversation_thread)


    @property
    def posts(self):
        """The posts for the ConversationThreadRequestBuilder

        Returns: 
            :class:`PostCollectionRequestBuilder<microsoft.msgraph.request.posts_collection.PostCollectionRequestBuilder>`:
                A request builder created from the ConversationThreadRequestBuilder
        """
        return post_collection.PostCollectionRequestBuilder(self.append_to_request_url("posts"), self._client)
    def reply(self, post):
        """Executes the reply method

        Args:
            post (:class:`Post<microsoft.msgraph.model.post.Post>`):
                The post to use in the method request

        Returns:
            :class:`ConversationThreadReplyRequestBuilder<microsoft.msgraph.request.conversation_thread_reply.ConversationThreadReplyRequestBuilder>`:
                A ConversationThreadReplyRequestBuilder for the method
        """
        return ConversationThreadReplyRequestBuilder(self.append_to_request_url("reply"), self._client, post)


