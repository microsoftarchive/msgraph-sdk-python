# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import conversation_thread_request_builder # import ConversationThreadRequestBuilder
#from .conversation_thread_request_builder import ConversationThreadRequestBuilder
from ..model.conversation_thread import ConversationThread
import json

class ThreadsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ThreadsCollectionRequest
        
        Args:
            request_url (str): The url to perform the ThreadsCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ThreadsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ThreadsCollectionPage

        Returns: 
            :class:`ThreadsCollectionPage<microsoft.msgraph.request.threads_collection.ThreadsCollectionPage>`:
                The ThreadsCollectionPage
        """
        self.method = "GET"
        collection_response = ThreadsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ThreadsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ConversationThreadRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ConversationThreadRequestBuilder for
        
        Returns: 
            :class:`ConversationThreadRequestBuilder<microsoft.msgraph.request.conversation_thread_request_builder.ConversationThreadRequestBuilder>`:
                A ConversationThreadRequestBuilder for that key
        """
        return conversation_thread_request_builder.ConversationThreadRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the ThreadsCollectionRequest
        
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
            :class:`ThreadsCollectionRequest<microsoft.msgraph.request.threads_collection.ThreadsCollectionRequest>`:
                The ThreadsCollectionRequest
        """
        req = ThreadsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ThreadsCollectionPage

        Returns: 
            :class:`ThreadsCollectionPage<microsoft.msgraph.request.threads_collection.ThreadsCollectionPage>`:
                The ThreadsCollectionPage
        """
        return self.request().get()



class ThreadsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ThreadsCollectionPage<microsoft.msgraph.request.threads_collection.ThreadsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ThreadsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ThreadsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ConversationThread at the index specified
        
        Args:
            index (int): The index of the item to get from the ThreadsCollectionPage

        Returns:
            :class:`ConversationThread<microsoft.msgraph.model.conversation_thread.ConversationThread>`:
                The ConversationThread at the index
        """
        return ConversationThread(self._prop_list[index])

    def threads(self):
        """Get a generator of ConversationThread within the ThreadsCollectionPage
        
        Yields:
            :class:`ConversationThread<microsoft.msgraph.model.conversation_thread.ConversationThread>`:
                The next ConversationThread in the collection
        """
        for item in self._prop_list:
            yield ConversationThread(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ThreadsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ThreadsCollectionRequest(next_page_link, client, options)
