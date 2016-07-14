# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import group_request_builder # import GroupRequestBuilder
#from .group_request_builder import GroupRequestBuilder
from ..model.group import Group
import json

class GroupsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the GroupsCollectionRequest
        
        Args:
            request_url (str): The url to perform the GroupsCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(GroupsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the GroupsCollectionPage

        Returns: 
            :class:`GroupsCollectionPage<microsoft.msgraph.request.groups_collection.GroupsCollectionPage>`:
                The GroupsCollectionPage
        """
        self.method = "GET"
        collection_response = GroupsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class GroupsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the GroupRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a GroupRequestBuilder for
        
        Returns: 
            :class:`GroupRequestBuilder<microsoft.msgraph.request.group_request_builder.GroupRequestBuilder>`:
                A GroupRequestBuilder for that key
        """
        return group_request_builder.GroupRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the GroupsCollectionRequest
        
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
            :class:`GroupsCollectionRequest<microsoft.msgraph.request.groups_collection.GroupsCollectionRequest>`:
                The GroupsCollectionRequest
        """
        req = GroupsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the GroupsCollectionPage

        Returns: 
            :class:`GroupsCollectionPage<microsoft.msgraph.request.groups_collection.GroupsCollectionPage>`:
                The GroupsCollectionPage
        """
        return self.request().get()



class GroupsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`GroupsCollectionPage<microsoft.msgraph.request.groups_collection.GroupsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = GroupsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class GroupsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Group at the index specified
        
        Args:
            index (int): The index of the item to get from the GroupsCollectionPage

        Returns:
            :class:`Group<microsoft.msgraph.model.group.Group>`:
                The Group at the index
        """
        return Group(self._prop_list[index])

    def groups(self):
        """Get a generator of Group within the GroupsCollectionPage
        
        Yields:
            :class:`Group<microsoft.msgraph.model.group.Group>`:
                The next Group in the collection
        """
        for item in self._prop_list:
            yield Group(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the GroupsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = GroupsCollectionRequest(next_page_link, client, options)
