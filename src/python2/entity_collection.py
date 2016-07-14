# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import entity_request_builder # import EntityRequestBuilder
#from .entity_request_builder import EntityRequestBuilder
from ..model.entity import Entity
import json

class EntityCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the EntityCollectionRequest
        
        Args:
            request_url (str): The url to perform the EntityCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EntityCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EntityCollectionPage

        Returns: 
            :class:`EntityCollectionPage<microsoft.msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        self.method = "GET"
        collection_response = EntityCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class EntityCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the EntityRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a EntityRequestBuilder for
        
        Returns: 
            :class:`EntityRequestBuilder<microsoft.msgraph.request.entity_request_builder.EntityRequestBuilder>`:
                A EntityRequestBuilder for that key
        """
        return entity_request_builder.EntityRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the EntityCollectionRequest
        
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
            :class:`EntityCollectionRequest<microsoft.msgraph.request.entity_collection.EntityCollectionRequest>`:
                The EntityCollectionRequest
        """
        req = EntityCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the EntityCollectionPage

        Returns: 
            :class:`EntityCollectionPage<microsoft.msgraph.request.entity_collection.EntityCollectionPage>`:
                The EntityCollectionPage
        """
        return self.request().get()



class EntityCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`EntityCollectionPage<microsoft.msgraph.request.entity_collection.EntityCollectionPage>`:
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
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The Entity at the index
        """
        return Entity(self._prop_list[index])

    def entity(self):
        """Get a generator of Entity within the EntityCollectionPage
        
        Yields:
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The next Entity in the collection
        """
        for item in self._prop_list:
            yield Entity(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EntityCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = EntityCollectionRequest(next_page_link, client, options)
