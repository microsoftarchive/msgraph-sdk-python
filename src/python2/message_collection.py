# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import message_request_builder # import MessageRequestBuilder
#from .message_request_builder import MessageRequestBuilder
from ..model.message import Message
import json

class MessageCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the MessageCollectionRequest
        
        Args:
            request_url (str): The url to perform the MessageCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(MessageCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the MessageCollectionPage

        Returns: 
            :class:`MessageCollectionPage<microsoft.msgraph.request.message_collection.MessageCollectionPage>`:
                The MessageCollectionPage
        """
        self.method = "GET"
        collection_response = MessageCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class MessageCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the MessageRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a MessageRequestBuilder for
        
        Returns: 
            :class:`MessageRequestBuilder<microsoft.msgraph.request.message_request_builder.MessageRequestBuilder>`:
                A MessageRequestBuilder for that key
        """
        return message_request_builder.MessageRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the MessageCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`MessageCollectionRequest<microsoft.msgraph.request.message_collection.MessageCollectionRequest>`:
                The MessageCollectionRequest
        """
        req = MessageCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the MessageCollectionPage

        Returns: 
            :class:`MessageCollectionPage<microsoft.msgraph.request.message_collection.MessageCollectionPage>`:
                The MessageCollectionPage
        """
        return self.request().get()



class MessageCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`MessageCollectionPage<microsoft.msgraph.request.message_collection.MessageCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = MessageCollectionPage(self._prop_dict["value"])

        return self._collection_page


class MessageCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Message at the index specified
        
        Args:
            index (int): The index of the item to get from the MessageCollectionPage

        Returns:
            :class:`Message<microsoft.msgraph.model.message.Message>`:
                The Message at the index
        """
        return Message(self._prop_list[index])

    def message(self):
        """Get a generator of Message within the MessageCollectionPage
        
        Yields:
            :class:`Message<microsoft.msgraph.model.message.Message>`:
                The next Message in the collection
        """
        for item in self._prop_list:
            yield Message(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the MessageCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = MessageCollectionRequest(next_page_link, client, options)
