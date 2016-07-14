# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import thumbnail_set_request_builder # import ThumbnailSetRequestBuilder
#from .thumbnail_set_request_builder import ThumbnailSetRequestBuilder
from ..model.thumbnail_set import ThumbnailSet
import json

class ThumbnailSetCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ThumbnailSetCollectionRequest
        
        Args:
            request_url (str): The url to perform the ThumbnailSetCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailSetCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ThumbnailSetCollectionPage

        Returns: 
            :class:`ThumbnailSetCollectionPage<microsoft.msgraph.request.thumbnail_set_collection.ThumbnailSetCollectionPage>`:
                The ThumbnailSetCollectionPage
        """
        self.method = "GET"
        collection_response = ThumbnailSetCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ThumbnailSetCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ThumbnailSetRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ThumbnailSetRequestBuilder for
        
        Returns: 
            :class:`ThumbnailSetRequestBuilder<microsoft.msgraph.request.thumbnail_set_request_builder.ThumbnailSetRequestBuilder>`:
                A ThumbnailSetRequestBuilder for that key
        """
        return thumbnail_set_request_builder.ThumbnailSetRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the ThumbnailSetCollectionRequest
        
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
            :class:`ThumbnailSetCollectionRequest<microsoft.msgraph.request.thumbnail_set_collection.ThumbnailSetCollectionRequest>`:
                The ThumbnailSetCollectionRequest
        """
        req = ThumbnailSetCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ThumbnailSetCollectionPage

        Returns: 
            :class:`ThumbnailSetCollectionPage<microsoft.msgraph.request.thumbnail_set_collection.ThumbnailSetCollectionPage>`:
                The ThumbnailSetCollectionPage
        """
        return self.request().get()



class ThumbnailSetCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ThumbnailSetCollectionPage<microsoft.msgraph.request.thumbnail_set_collection.ThumbnailSetCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ThumbnailSetCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ThumbnailSetCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ThumbnailSet at the index specified
        
        Args:
            index (int): The index of the item to get from the ThumbnailSetCollectionPage

        Returns:
            :class:`ThumbnailSet<microsoft.msgraph.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet at the index
        """
        return ThumbnailSet(self._prop_list[index])

    def thumbnail_set(self):
        """Get a generator of ThumbnailSet within the ThumbnailSetCollectionPage
        
        Yields:
            :class:`ThumbnailSet<microsoft.msgraph.model.thumbnail_set.ThumbnailSet>`:
                The next ThumbnailSet in the collection
        """
        for item in self._prop_list:
            yield ThumbnailSet(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ThumbnailSetCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ThumbnailSetCollectionRequest(next_page_link, client, options)
