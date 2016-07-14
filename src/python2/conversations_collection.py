# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import conversation_request_builder # import ConversationRequestBuilder
#from .conversation_request_builder import ConversationRequestBuilder
from ..model.conversation import Conversation
import json

class ConversationsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ConversationsCollectionRequest
        
        Args:
            request_url (str): The url to perform the ConversationsCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ConversationsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ConversationsCollectionPage

        Returns: 
            :class:`ConversationsCollectionPage<microsoft.msgraph.request.conversations_collection.ConversationsCollectionPage>`:
                The ConversationsCollectionPage
        """
        self.method = "GET"
        collection_response = ConversationsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ConversationsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ConversationRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ConversationRequestBuilder for
        
        Returns: 
            :class:`ConversationRequestBuilder<microsoft.msgraph.request.conversation_request_builder.ConversationRequestBuilder>`:
                A ConversationRequestBuilder for that key
        """
        return conversation_request_builder.ConversationRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the ConversationsCollectionRequest
        
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
            :class:`ConversationsCollectionRequest<microsoft.msgraph.request.conversations_collection.ConversationsCollectionRequest>`:
                The ConversationsCollectionRequest
        """
        req = ConversationsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ConversationsCollectionPage

        Returns: 
            :class:`ConversationsCollectionPage<microsoft.msgraph.request.conversations_collection.ConversationsCollectionPage>`:
                The ConversationsCollectionPage
        """
        return self.request().get()



class ConversationsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ConversationsCollectionPage<microsoft.msgraph.request.conversations_collection.ConversationsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ConversationsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ConversationsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Conversation at the index specified
        
        Args:
            index (int): The index of the item to get from the ConversationsCollectionPage

        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The Conversation at the index
        """
        return Conversation(self._prop_list[index])

    def conversations(self):
        """Get a generator of Conversation within the ConversationsCollectionPage
        
        Yields:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The next Conversation in the collection
        """
        for item in self._prop_list:
            yield Conversation(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ConversationsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ConversationsCollectionRequest(next_page_link, client, options)
