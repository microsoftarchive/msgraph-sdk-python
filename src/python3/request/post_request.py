# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.post import Post
import json
import asyncio

class PostRequest(RequestBase):
    """The type PostRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new PostRequest.

        Args:
            request_url (str): The url to perform the PostRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(PostRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Post."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Post."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Post.
        
        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The Post.
        """
        self.method = "GET"
        entity = Post(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Post in async.

        Yields:
            :class:`Post<msgraph.model.post.Post>`:
                The Post.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, post):
        """Updates the specified Post.
        
        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The Post to update.

        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The updated Post.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Post(json.loads(self.send(post).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, post):
        """Updates the specified Post in async
        
        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The Post to update.

        Yields:
            :class:`Post<msgraph.model.post.Post>`:
                The updated Post.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    post)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.new_participants and value.new_participants._prop_dict:
                if "new_participants@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["new_participants@odata.nextLink"]
                    value.new_participants._init_next_page_request(next_page_link, self._client, None)
            if value.extensions and value.extensions._prop_dict:
                if "extensions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["extensions@odata.nextLink"]
                    value.extensions._init_next_page_request(next_page_link, self._client, None)
            if value.attachments and value.attachments._prop_dict:
                if "attachments@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["attachments@odata.nextLink"]
                    value.attachments._init_next_page_request(next_page_link, self._client, None)
