# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import entity_request_builder 
from ..model.entity import Entity
import json
import asyncio

class EntityCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the EntityCollectionRequest
        
        Args:
            request_url (str): The url to perform the EntityCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EntityCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EntityCollectionPage

        Returns: 
            :class:`EntityCollectionPage<msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        self.method = "GET"
        collection_response = EntityCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the EntityCollectionPage in async

        Yields: 
            :class:`EntityCollectionPage<msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class EntityCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the EntityRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a EntityRequestBuilder for
        
        Returns: 
            :class:`EntityRequestBuilder<msgraph.request.entity_request_builder.EntityRequestBuilder>`:
                A EntityRequestBuilder for that key
        """
        return entity_request_builder.EntityRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the EntityCollectionRequest
        
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
            :class:`EntityCollectionRequest<msgraph.request.entity_collection.EntityCollectionRequest>`:
                The EntityCollectionRequest
        """
        req = EntityCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the EntityCollectionPage

        Returns: 
            :class:`EntityCollectionPage<msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the EntityCollectionPage in async

        Yields: 
            :class:`EntityCollectionPage<msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class EntityCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`EntityCollectionPage<msgraph.request.entity_collection.EntityCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = EntityCollectionPage(self._prop_dict["value"])

        return self._collection_page


class EntityCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Entity at the index specified
        
        Args:
            index (int): The index of the item to get from the EntityCollectionPage

        Returns:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The Entity at the index
        """
        return Entity(self._prop_list[index])

    def entity(self):
        """Get a generator of Entity within the EntityCollectionPage
        
        Yields:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The next Entity in the collection
        """
        for item in self._prop_list:
            yield Entity(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EntityCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = EntityCollectionRequest(next_page_link, client, options)
