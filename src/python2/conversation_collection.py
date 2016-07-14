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

class ConversationCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ConversationCollectionRequest
        
        Args:
            request_url (str): The url to perform the ConversationCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ConversationCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ConversationCollectionPage

        Returns: 
            :class:`ConversationCollectionPage<microsoft.msgraph.request.conversation_collection.ConversationCollectionPage>`:
                The ConversationCollectionPage
        """
        self.method = "GET"
        collection_response = ConversationCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ConversationCollectionRequestBuilder(RequestBuilderBase):

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
        """Builds the ConversationCollectionRequest
        
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
            :class:`ConversationCollectionRequest<microsoft.msgraph.request.conversation_collection.ConversationCollectionRequest>`:
                The ConversationCollectionRequest
        """
        req = ConversationCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ConversationCollectionPage

        Returns: 
            :class:`ConversationCollectionPage<microsoft.msgraph.request.conversation_collection.ConversationCollectionPage>`:
                The ConversationCollectionPage
        """
        return self.request().get()



class ConversationCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ConversationCollectionPage<microsoft.msgraph.request.conversation_collection.ConversationCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ConversationCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ConversationCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Conversation at the index specified
        
        Args:
            index (int): The index of the item to get from the ConversationCollectionPage

        Returns:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The Conversation at the index
        """
        return Conversation(self._prop_list[index])

    def conversation(self):
        """Get a generator of Conversation within the ConversationCollectionPage
        
        Yields:
            :class:`Conversation<microsoft.msgraph.model.conversation.Conversation>`:
                The next Conversation in the collection
        """
        for item in self._prop_list:
            yield Conversation(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ConversationCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ConversationCollectionRequest(next_page_link, client, options)
