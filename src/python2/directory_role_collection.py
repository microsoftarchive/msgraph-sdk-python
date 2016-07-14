# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import directory_role_request_builder # import DirectoryRoleRequestBuilder
#from .directory_role_request_builder import DirectoryRoleRequestBuilder
from ..model.directory_role import DirectoryRole
import json

class DirectoryRoleCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DirectoryRoleCollectionRequest
        
        Args:
            request_url (str): The url to perform the DirectoryRoleCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DirectoryRoleCollectionPage

        Returns: 
            :class:`DirectoryRoleCollectionPage<microsoft.msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        self.method = "GET"
        collection_response = DirectoryRoleCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class DirectoryRoleCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DirectoryRoleRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DirectoryRoleRequestBuilder for
        
        Returns: 
            :class:`DirectoryRoleRequestBuilder<microsoft.msgraph.request.directory_role_request_builder.DirectoryRoleRequestBuilder>`:
                A DirectoryRoleRequestBuilder for that key
        """
        return directory_role_request_builder.DirectoryRoleRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the DirectoryRoleCollectionRequest
        
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
            :class:`DirectoryRoleCollectionRequest<microsoft.msgraph.request.directory_role_collection.DirectoryRoleCollectionRequest>`:
                The DirectoryRoleCollectionRequest
        """
        req = DirectoryRoleCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the DirectoryRoleCollectionPage

        Returns: 
            :class:`DirectoryRoleCollectionPage<microsoft.msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The DirectoryRoleCollectionPage
        """
        return self.request().get()



class DirectoryRoleCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DirectoryRoleCollectionPage<microsoft.msgraph.request.directory_role_collection.DirectoryRoleCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DirectoryRoleCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DirectoryRoleCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the DirectoryRole at the index specified
        
        Args:
            index (int): The index of the item to get from the DirectoryRoleCollectionPage

        Returns:
            :class:`DirectoryRole<microsoft.msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole at the index
        """
        return DirectoryRole(self._prop_list[index])

    def directory_role(self):
        """Get a generator of DirectoryRole within the DirectoryRoleCollectionPage
        
        Yields:
            :class:`DirectoryRole<microsoft.msgraph.model.directory_role.DirectoryRole>`:
                The next DirectoryRole in the collection
        """
        for item in self._prop_list:
            yield DirectoryRole(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DirectoryRoleCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DirectoryRoleCollectionRequest(next_page_link, client, options)
