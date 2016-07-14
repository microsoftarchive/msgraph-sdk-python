# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.post import Post
import json

class PostRequest(RequestBase):
    """The type PostRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new PostRequest.

        Args:
            request_url (str): The url to perform the PostRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(PostRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Post."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Post.
        
        Returns:
            :class:`Post<microsoft.msgraph.model.post.Post>`:
                The Post.
        """
        self.method = "GET"
        entity = Post(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, post):
        """Updates the specified Post.
        
        Args:
            post (:class:`Post<microsoft.msgraph.model.post.Post>`):
                The Post to update.

        Returns:
            :class:`Post<microsoft.msgraph.model.post.Post>`:
                The updated Post.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Post(json.loads(self.send(post).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.new_participants and value.new_participants._prop_dict:
                if "new_participants@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["new_participants@odata.nextLink"]
                    value.new_participants._init_next_page_request(next_page_link, self._client, None)
            if value.attachments and value.attachments._prop_dict:
                if "attachments@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["attachments@odata.nextLink"]
                    value.attachments._init_next_page_request(next_page_link, self._client, None)
