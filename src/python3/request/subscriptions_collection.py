# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import subscription_request_builder 
from ..model.subscription import Subscription
import json
import asyncio

class SubscriptionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the SubscriptionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the SubscriptionsCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscriptionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the SubscriptionsCollectionPage

        Returns: 
            :class:`SubscriptionsCollectionPage<msgraph.request.subscriptions_collection.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        self.method = "GET"
        collection_response = SubscriptionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the SubscriptionsCollectionPage in async

        Yields: 
            :class:`SubscriptionsCollectionPage<msgraph.request.subscriptions_collection.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class SubscriptionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the SubscriptionRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a SubscriptionRequestBuilder for
        
        Returns: 
            :class:`SubscriptionRequestBuilder<msgraph.request.subscription_request_builder.SubscriptionRequestBuilder>`:
                A SubscriptionRequestBuilder for that key
        """
        return subscription_request_builder.SubscriptionRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,options=None):
        """Builds the SubscriptionsCollectionRequest
        
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
            :class:`SubscriptionsCollectionRequest<msgraph.request.subscriptions_collection.SubscriptionsCollectionRequest>`:
                The SubscriptionsCollectionRequest
        """
        req = SubscriptionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def get(self):
        """Gets the SubscriptionsCollectionPage

        Returns: 
            :class:`SubscriptionsCollectionPage<msgraph.request.subscriptions_collection.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the SubscriptionsCollectionPage in async

        Yields: 
            :class:`SubscriptionsCollectionPage<msgraph.request.subscriptions_collection.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class SubscriptionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`SubscriptionsCollectionPage<msgraph.request.subscriptions_collection.SubscriptionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = SubscriptionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class SubscriptionsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Subscription at the index specified
        
        Args:
            index (int): The index of the item to get from the SubscriptionsCollectionPage

        Returns:
            :class:`Subscription<msgraph.model.subscription.Subscription>`:
                The Subscription at the index
        """
        return Subscription(self._prop_list[index])

    def subscriptions(self):
        """Get a generator of Subscription within the SubscriptionsCollectionPage
        
        Yields:
            :class:`Subscription<msgraph.model.subscription.Subscription>`:
                The next Subscription in the collection
        """
        for item in self._prop_list:
            yield Subscription(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the SubscriptionsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = SubscriptionsCollectionRequest(next_page_link, client, options)
