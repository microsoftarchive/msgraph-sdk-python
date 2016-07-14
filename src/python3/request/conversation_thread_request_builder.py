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
import asyncio

from ..request import post_collection


class ConversationThreadRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ConversationThreadRequestBuilder

        Args:
            request_url (str): The url to perform the ConversationThreadRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ConversationThreadRequest<msgraph.request.conversation_thread_request.ConversationThreadRequest>`:
                The ConversationThreadRequest
        """
        req = ConversationThreadRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified ConversationThread."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ConversationThread."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified ConversationThread.
        
        Returns:
            :class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`:
                The ConversationThread.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ConversationThread in async.

        Returns:
            :class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`:
                The ConversationThread.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, conversation_thread):
        """Updates the specified ConversationThread.
        
        Args:
            conversation_thread (:class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`):
                The ConversationThread to update.

        Returns:
            :class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`:
                The updated ConversationThread
        """
        return self.request().update(conversation_thread)

    @asyncio.coroutine
    def update_async(self, conversation_thread):
        """Updates the specified ConversationThread in async
        
        Args:
            conversation_thread (:class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`):
                The ConversationThread to update.

        Returns:
            :class:`ConversationThread<msgraph.model.conversation_thread.ConversationThread>`:
                The updated ConversationThread.
        """
        entity = yield from self.request().update_async(conversation_thread)
        return entity

    @property
    def posts(self):
        """The posts for the ConversationThreadRequestBuilder

        Returns: 
            :class:`PostCollectionRequestBuilder<msgraph.request.posts_collection.PostCollectionRequestBuilder>`:
                A request builder created from the ConversationThreadRequestBuilder
        """
        return post_collection.PostCollectionRequestBuilder(self.append_to_request_url("posts"), self._client)
    def reply(self, post):
        """Executes the reply method

        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The post to use in the method request

        Returns:
            :class:`ConversationThreadReplyRequestBuilder<msgraph.request.conversation_thread_reply.ConversationThreadReplyRequestBuilder>`:
                A ConversationThreadReplyRequestBuilder for the method
        """
        return ConversationThreadReplyRequestBuilder(self.append_to_request_url("reply"), self._client, post)


