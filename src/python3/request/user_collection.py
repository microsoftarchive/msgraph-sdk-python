# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import user_request_builder 
from ..model.user import User
import json
import asyncio

class UserCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the UserCollectionRequest
        
        Args:
            request_url (str): The url to perform the UserCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(UserCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the UserCollectionPage

        Returns: 
            :class:`UserCollectionPage<msgraph.request.user_collection.UserCollectionPage>`:
                The UserCollectionPage
        """
        self.method = "GET"
        collection_response = UserCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the UserCollectionPage in async

        Yields: 
            :class:`UserCollectionPage<msgraph.request.user_collection.UserCollectionPage>`:
                The UserCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class UserCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the UserRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a UserRequestBuilder for
        
        Returns: 
            :class:`UserRequestBuilder<msgraph.request.user_request_builder.UserRequestBuilder>`:
                A UserRequestBuilder for that key
        """
        return user_request_builder.UserRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,top=None, order_by=None, options=None):
        """Builds the UserCollectionRequest
        
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
            :class:`UserCollectionRequest<msgraph.request.user_collection.UserCollectionRequest>`:
                The UserCollectionRequest
        """
        req = UserCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(top=top, order_by=order_by, )
        return req

    def get(self):
        """Gets the UserCollectionPage

        Returns: 
            :class:`UserCollectionPage<msgraph.request.user_collection.UserCollectionPage>`:
                The UserCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the UserCollectionPage in async

        Yields: 
            :class:`UserCollectionPage<msgraph.request.user_collection.UserCollectionPage>`:
                The UserCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class UserCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`UserCollectionPage<msgraph.request.user_collection.UserCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = UserCollectionPage(self._prop_dict["value"])

        return self._collection_page


class UserCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the User at the index specified
        
        Args:
            index (int): The index of the item to get from the UserCollectionPage

        Returns:
            :class:`User<msgraph.model.user.User>`:
                The User at the index
        """
        return User(self._prop_list[index])

    def user(self):
        """Get a generator of User within the UserCollectionPage
        
        Yields:
            :class:`User<msgraph.model.user.User>`:
                The next User in the collection
        """
        for item in self._prop_list:
            yield User(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the UserCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = UserCollectionRequest(next_page_link, client, options)
