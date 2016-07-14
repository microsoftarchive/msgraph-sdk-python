# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import contact_request_builder 
from ..model.contact import Contact
import json
import asyncio

class ContactCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ContactCollectionRequest
        
        Args:
            request_url (str): The url to perform the ContactCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ContactCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ContactCollectionPage

        Returns: 
            :class:`ContactCollectionPage<msgraph.request.contact_collection.ContactCollectionPage>`:
                The ContactCollectionPage
        """
        self.method = "GET"
        collection_response = ContactCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the ContactCollectionPage in async

        Yields: 
            :class:`ContactCollectionPage<msgraph.request.contact_collection.ContactCollectionPage>`:
                The ContactCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class ContactCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ContactRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ContactRequestBuilder for
        
        Returns: 
            :class:`ContactRequestBuilder<msgraph.request.contact_request_builder.ContactRequestBuilder>`:
                A ContactRequestBuilder for that key
        """
        return contact_request_builder.ContactRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the ContactCollectionRequest
        
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
            :class:`ContactCollectionRequest<msgraph.request.contact_collection.ContactCollectionRequest>`:
                The ContactCollectionRequest
        """
        req = ContactCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the ContactCollectionPage

        Returns: 
            :class:`ContactCollectionPage<msgraph.request.contact_collection.ContactCollectionPage>`:
                The ContactCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the ContactCollectionPage in async

        Yields: 
            :class:`ContactCollectionPage<msgraph.request.contact_collection.ContactCollectionPage>`:
                The ContactCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class ContactCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ContactCollectionPage<msgraph.request.contact_collection.ContactCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ContactCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ContactCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Contact at the index specified
        
        Args:
            index (int): The index of the item to get from the ContactCollectionPage

        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The Contact at the index
        """
        return Contact(self._prop_list[index])

    def contact(self):
        """Get a generator of Contact within the ContactCollectionPage
        
        Yields:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The next Contact in the collection
        """
        for item in self._prop_list:
            yield Contact(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ContactCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ContactCollectionRequest(next_page_link, client, options)
