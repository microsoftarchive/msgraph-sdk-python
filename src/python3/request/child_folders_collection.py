# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import contact_folder_request_builder 
from ..model.contact_folder import ContactFolder
import json
import asyncio

class ChildFoldersCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ChildFoldersCollectionRequest
        
        Args:
            request_url (str): The url to perform the ChildFoldersCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ChildFoldersCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ChildFoldersCollectionPage

        Returns: 
            :class:`ChildFoldersCollectionPage<msgraph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The ChildFoldersCollectionPage
        """
        self.method = "GET"
        collection_response = ChildFoldersCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the ChildFoldersCollectionPage in async

        Yields: 
            :class:`ChildFoldersCollectionPage<msgraph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The ChildFoldersCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class ChildFoldersCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ContactFolderRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ContactFolderRequestBuilder for
        
        Returns: 
            :class:`ContactFolderRequestBuilder<msgraph.request.contact_folder_request_builder.ContactFolderRequestBuilder>`:
                A ContactFolderRequestBuilder for that key
        """
        return contact_folder_request_builder.ContactFolderRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the ChildFoldersCollectionRequest
        
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
            :class:`ChildFoldersCollectionRequest<msgraph.request.child_folders_collection.ChildFoldersCollectionRequest>`:
                The ChildFoldersCollectionRequest
        """
        req = ChildFoldersCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the ChildFoldersCollectionPage

        Returns: 
            :class:`ChildFoldersCollectionPage<msgraph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The ChildFoldersCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the ChildFoldersCollectionPage in async

        Yields: 
            :class:`ChildFoldersCollectionPage<msgraph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The ChildFoldersCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class ChildFoldersCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ChildFoldersCollectionPage<msgraph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ChildFoldersCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ChildFoldersCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ContactFolder at the index specified
        
        Args:
            index (int): The index of the item to get from the ChildFoldersCollectionPage

        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder at the index
        """
        return ContactFolder(self._prop_list[index])

    def child_folders(self):
        """Get a generator of ContactFolder within the ChildFoldersCollectionPage
        
        Yields:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The next ContactFolder in the collection
        """
        for item in self._prop_list:
            yield ContactFolder(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ChildFoldersCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ChildFoldersCollectionRequest(next_page_link, client, options)
