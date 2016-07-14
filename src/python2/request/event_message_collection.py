# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import event_message_request_builder # import EventMessageRequestBuilder
#from .event_message_request_builder import EventMessageRequestBuilder
from ..model.event_message import EventMessage
import json

class EventMessageCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the EventMessageCollectionRequest
        
        Args:
            request_url (str): The url to perform the EventMessageCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EventMessageCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EventMessageCollectionPage

        Returns: 
            :class:`EventMessageCollectionPage<microsoft.msgraph.request.event_message_collection.EventMessageCollectionPage>`:
                The EventMessageCollectionPage
        """
        self.method = "GET"
        collection_response = EventMessageCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class EventMessageCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the EventMessageRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a EventMessageRequestBuilder for
        
        Returns: 
            :class:`EventMessageRequestBuilder<microsoft.msgraph.request.event_message_request_builder.EventMessageRequestBuilder>`:
                A EventMessageRequestBuilder for that key
        """
        return event_message_request_builder.EventMessageRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the EventMessageCollectionRequest
        
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
            :class:`EventMessageCollectionRequest<microsoft.msgraph.request.event_message_collection.EventMessageCollectionRequest>`:
                The EventMessageCollectionRequest
        """
        req = EventMessageCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the EventMessageCollectionPage

        Returns: 
            :class:`EventMessageCollectionPage<microsoft.msgraph.request.event_message_collection.EventMessageCollectionPage>`:
                The EventMessageCollectionPage
        """
        return self.request().get()



class EventMessageCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`EventMessageCollectionPage<microsoft.msgraph.request.event_message_collection.EventMessageCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = EventMessageCollectionPage(self._prop_dict["value"])

        return self._collection_page


class EventMessageCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the EventMessage at the index specified
        
        Args:
            index (int): The index of the item to get from the EventMessageCollectionPage

        Returns:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The EventMessage at the index
        """
        return EventMessage(self._prop_list[index])

    def event_message(self):
        """Get a generator of EventMessage within the EventMessageCollectionPage
        
        Yields:
            :class:`EventMessage<microsoft.msgraph.model.event_message.EventMessage>`:
                The next EventMessage in the collection
        """
        for item in self._prop_list:
            yield EventMessage(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EventMessageCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = EventMessageCollectionRequest(next_page_link, client, options)
