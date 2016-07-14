# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import subscribed_sku_request_builder # import SubscribedSkuRequestBuilder
#from .subscribed_sku_request_builder import SubscribedSkuRequestBuilder
from ..model.subscribed_sku import SubscribedSku
import json

class SubscribedSkusCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the SubscribedSkusCollectionRequest
        
        Args:
            request_url (str): The url to perform the SubscribedSkusCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscribedSkusCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the SubscribedSkusCollectionPage

        Returns: 
            :class:`SubscribedSkusCollectionPage<microsoft.msgraph.request.subscribed_skus_collection.SubscribedSkusCollectionPage>`:
                The SubscribedSkusCollectionPage
        """
        self.method = "GET"
        collection_response = SubscribedSkusCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class SubscribedSkusCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the SubscribedSkuRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a SubscribedSkuRequestBuilder for
        
        Returns: 
            :class:`SubscribedSkuRequestBuilder<microsoft.msgraph.request.subscribed_sku_request_builder.SubscribedSkuRequestBuilder>`:
                A SubscribedSkuRequestBuilder for that key
        """
        return subscribed_sku_request_builder.SubscribedSkuRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the SubscribedSkusCollectionRequest
        
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
            :class:`SubscribedSkusCollectionRequest<microsoft.msgraph.request.subscribed_skus_collection.SubscribedSkusCollectionRequest>`:
                The SubscribedSkusCollectionRequest
        """
        req = SubscribedSkusCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the SubscribedSkusCollectionPage

        Returns: 
            :class:`SubscribedSkusCollectionPage<microsoft.msgraph.request.subscribed_skus_collection.SubscribedSkusCollectionPage>`:
                The SubscribedSkusCollectionPage
        """
        return self.request().get()



class SubscribedSkusCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`SubscribedSkusCollectionPage<microsoft.msgraph.request.subscribed_skus_collection.SubscribedSkusCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = SubscribedSkusCollectionPage(self._prop_dict["value"])

        return self._collection_page


class SubscribedSkusCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the SubscribedSku at the index specified
        
        Args:
            index (int): The index of the item to get from the SubscribedSkusCollectionPage

        Returns:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The SubscribedSku at the index
        """
        return SubscribedSku(self._prop_list[index])

    def subscribed_skus(self):
        """Get a generator of SubscribedSku within the SubscribedSkusCollectionPage
        
        Yields:
            :class:`SubscribedSku<microsoft.msgraph.model.subscribed_sku.SubscribedSku>`:
                The next SubscribedSku in the collection
        """
        for item in self._prop_list:
            yield SubscribedSku(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the SubscribedSkusCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = SubscribedSkusCollectionRequest(next_page_link, client, options)
