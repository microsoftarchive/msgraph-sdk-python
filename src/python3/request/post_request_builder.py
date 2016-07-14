# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .post_request import PostRequest
from ..request_builder_base import RequestBuilderBase
from ..request.post_forward import PostForwardRequestBuilder
from ..request.post_reply import PostReplyRequestBuilder
import asyncio

from ..request import extension_collection
from ..request import post_request_builder
from ..request import attachment_collection


class PostRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the PostRequestBuilder

        Args:
            request_url (str): The url to perform the PostRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(PostRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the PostRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`PostRequest<msgraph.request.post_request.PostRequest>`:
                The PostRequest
        """
        req = PostRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Post."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Post."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Post.
        
        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The Post.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Post in async.

        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The Post.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, post):
        """Updates the specified Post.
        
        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The Post to update.

        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The updated Post
        """
        return self.request().update(post)

    @asyncio.coroutine
    def update_async(self, post):
        """Updates the specified Post in async
        
        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The Post to update.

        Returns:
            :class:`Post<msgraph.model.post.Post>`:
                The updated Post.
        """
        entity = yield from self.request().update_async(post)
        return entity

    @property
    def extensions(self):
        """The extensions for the PostRequestBuilder

        Returns: 
            :class:`ExtensionCollectionRequestBuilder<msgraph.request.extensions_collection.ExtensionCollectionRequestBuilder>`:
                A request builder created from the PostRequestBuilder
        """
        return extension_collection.ExtensionCollectionRequestBuilder(self.append_to_request_url("extensions"), self._client)

    @property
    def in_reply_to(self):
        """The in_reply_to for the PostRequestBuilder

        Returns: 
            :class:`PostRequestBuilder<msgraph.request.post_request.PostRequestBuilder>`:
                A request builder created from the PostRequestBuilder
        """
        return post_request_builder.PostRequestBuilder(self.append_to_request_url("inReplyTo"), self._client)


    @property
    def attachments(self):
        """The attachments for the PostRequestBuilder

        Returns: 
            :class:`AttachmentCollectionRequestBuilder<msgraph.request.attachments_collection.AttachmentCollectionRequestBuilder>`:
                A request builder created from the PostRequestBuilder
        """
        return attachment_collection.AttachmentCollectionRequestBuilder(self.append_to_request_url("attachments"), self._client)
    def forward(self, to_recipients, comment=None):
        """Executes the forward method

        Args:
            comment (str):
                The comment to use in the method request          
            to_recipients (:class:`Recipient<msgraph.model.recipient.Recipient>`):
                The to_recipients to use in the method request

        Returns:
            :class:`PostForwardRequestBuilder<msgraph.request.post_forward.PostForwardRequestBuilder>`:
                A PostForwardRequestBuilder for the method
        """
        return PostForwardRequestBuilder(self.append_to_request_url("forward"), self._client, to_recipients, comment=comment)

    def reply(self, post):
        """Executes the reply method

        Args:
            post (:class:`Post<msgraph.model.post.Post>`):
                The post to use in the method request

        Returns:
            :class:`PostReplyRequestBuilder<msgraph.request.post_reply.PostReplyRequestBuilder>`:
                A PostReplyRequestBuilder for the method
        """
        return PostReplyRequestBuilder(self.append_to_request_url("reply"), self._client, post)


