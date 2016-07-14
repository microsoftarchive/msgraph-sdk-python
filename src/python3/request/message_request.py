# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.message import Message
import json
import asyncio

class MessageRequest(RequestBase):
    """The type MessageRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new MessageRequest.

        Args:
            request_url (str): The url to perform the MessageRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(MessageRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Message."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Message."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Message.
        
        Returns:
            :class:`Message<msgraph.model.message.Message>`:
                The Message.
        """
        self.method = "GET"
        entity = Message(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Message in async.

        Yields:
            :class:`Message<msgraph.model.message.Message>`:
                The Message.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, message):
        """Updates the specified Message.
        
        Args:
            message (:class:`Message<msgraph.model.message.Message>`):
                The Message to update.

        Returns:
            :class:`Message<msgraph.model.message.Message>`:
                The updated Message.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Message(json.loads(self.send(message).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, message):
        """Updates the specified Message in async
        
        Args:
            message (:class:`Message<msgraph.model.message.Message>`):
                The Message to update.

        Yields:
            :class:`Message<msgraph.model.message.Message>`:
                The updated Message.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    message)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.to_recipients and value.to_recipients._prop_dict:
                if "to_recipients@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["to_recipients@odata.nextLink"]
                    value.to_recipients._init_next_page_request(next_page_link, self._client, None)
            if value.cc_recipients and value.cc_recipients._prop_dict:
                if "cc_recipients@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["cc_recipients@odata.nextLink"]
                    value.cc_recipients._init_next_page_request(next_page_link, self._client, None)
            if value.bcc_recipients and value.bcc_recipients._prop_dict:
                if "bcc_recipients@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["bcc_recipients@odata.nextLink"]
                    value.bcc_recipients._init_next_page_request(next_page_link, self._client, None)
            if value.reply_to and value.reply_to._prop_dict:
                if "reply_to@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["reply_to@odata.nextLink"]
                    value.reply_to._init_next_page_request(next_page_link, self._client, None)
            if value.extensions and value.extensions._prop_dict:
                if "extensions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["extensions@odata.nextLink"]
                    value.extensions._init_next_page_request(next_page_link, self._client, None)
            if value.attachments and value.attachments._prop_dict:
                if "attachments@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["attachments@odata.nextLink"]
                    value.attachments._init_next_page_request(next_page_link, self._client, None)
