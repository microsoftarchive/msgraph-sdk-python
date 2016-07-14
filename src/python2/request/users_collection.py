# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import user_request_builder # import UserRequestBuilder
#from .user_request_builder import UserRequestBuilder
from ..model.user import User
import json

class UsersCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the UsersCollectionRequest
        
        Args:
            request_url (str): The url to perform the UsersCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(UsersCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the UsersCollectionPage

        Returns: 
            :class:`UsersCollectionPage<microsoft.msgraph.request.users_collection.UsersCollectionPage>`:
                The UsersCollectionPage
        """
        self.method = "GET"
        collection_response = UsersCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class UsersCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the UserRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a UserRequestBuilder for
        
        Returns: 
            :class:`UserRequestBuilder<microsoft.msgraph.request.user_request_builder.UserRequestBuilder>`:
                A UserRequestBuilder for that key
        """
        return user_request_builder.UserRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the UsersCollectionRequest
        
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
            :class:`UsersCollectionRequest<microsoft.msgraph.request.users_collection.UsersCollectionRequest>`:
                The UsersCollectionRequest
        """
        req = UsersCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the UsersCollectionPage

        Returns: 
            :class:`UsersCollectionPage<microsoft.msgraph.request.users_collection.UsersCollectionPage>`:
                The UsersCollectionPage
        """
        return self.request().get()



class UsersCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`UsersCollectionPage<microsoft.msgraph.request.users_collection.UsersCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = UsersCollectionPage(self._prop_dict["value"])

        return self._collection_page


class UsersCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the User at the index specified
        
        Args:
            index (int): The index of the item to get from the UsersCollectionPage

        Returns:
            :class:`User<microsoft.msgraph.model.user.User>`:
                The User at the index
        """
        return User(self._prop_list[index])

    def users(self):
        """Get a generator of User within the UsersCollectionPage
        
        Yields:
            :class:`User<microsoft.msgraph.model.user.User>`:
                The next User in the collection
        """
        for item in self._prop_list:
            yield User(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the UsersCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = UsersCollectionRequest(next_page_link, client, options)
