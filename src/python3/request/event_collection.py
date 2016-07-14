# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import event_request_builder 
from ..model.event import Event
import json
import asyncio

class EventCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the EventCollectionRequest
        
        Args:
            request_url (str): The url to perform the EventCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EventCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EventCollectionPage

        Returns: 
            :class:`EventCollectionPage<msgraph.request.event_collection.EventCollectionPage>`:
                The EventCollectionPage
        """
        self.method = "GET"
        collection_response = EventCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the EventCollectionPage in async

        Yields: 
            :class:`EventCollectionPage<msgraph.request.event_collection.EventCollectionPage>`:
                The EventCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class EventCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the EventRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a EventRequestBuilder for
        
        Returns: 
            :class:`EventRequestBuilder<msgraph.request.event_request_builder.EventRequestBuilder>`:
                A EventRequestBuilder for that key
        """
        return event_request_builder.EventRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the EventCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EventCollectionRequest<msgraph.request.event_collection.EventCollectionRequest>`:
                The EventCollectionRequest
        """
        req = EventCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the EventCollectionPage

        Returns: 
            :class:`EventCollectionPage<msgraph.request.event_collection.EventCollectionPage>`:
                The EventCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the EventCollectionPage in async

        Yields: 
            :class:`EventCollectionPage<msgraph.request.event_collection.EventCollectionPage>`:
                The EventCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class EventCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`EventCollectionPage<msgraph.request.event_collection.EventCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = EventCollectionPage(self._prop_dict["value"])

        return self._collection_page


class EventCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Event at the index specified
        
        Args:
            index (int): The index of the item to get from the EventCollectionPage

        Returns:
            :class:`Event<msgraph.model.event.Event>`:
                The Event at the index
        """
        return Event(self._prop_list[index])

    def event(self):
        """Get a generator of Event within the EventCollectionPage
        
        Yields:
            :class:`Event<msgraph.model.event.Event>`:
                The next Event in the collection
        """
        for item in self._prop_list:
            yield Event(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EventCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = EventCollectionRequest(next_page_link, client, options)
