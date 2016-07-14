# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import drive_request_builder # import DriveRequestBuilder
#from .drive_request_builder import DriveRequestBuilder
from ..model.drive import Drive
import json

class DriveCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DriveCollectionRequest
        
        Args:
            request_url (str): The url to perform the DriveCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DriveCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DriveCollectionPage

        Returns: 
            :class:`DriveCollectionPage<microsoft.msgraph.request.drive_collection.DriveCollectionPage>`:
                The DriveCollectionPage
        """
        self.method = "GET"
        collection_response = DriveCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class DriveCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DriveRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DriveRequestBuilder for
        
        Returns: 
            :class:`DriveRequestBuilder<microsoft.msgraph.request.drive_request_builder.DriveRequestBuilder>`:
                A DriveRequestBuilder for that key
        """
        return drive_request_builder.DriveRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the DriveCollectionRequest
        
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
            :class:`DriveCollectionRequest<microsoft.msgraph.request.drive_collection.DriveCollectionRequest>`:
                The DriveCollectionRequest
        """
        req = DriveCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the DriveCollectionPage

        Returns: 
            :class:`DriveCollectionPage<microsoft.msgraph.request.drive_collection.DriveCollectionPage>`:
                The DriveCollectionPage
        """
        return self.request().get()



class DriveCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DriveCollectionPage<microsoft.msgraph.request.drive_collection.DriveCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DriveCollectionPage(self._prop_dict["value"])

        return self._collection_page


class DriveCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Drive at the index specified
        
        Args:
            index (int): The index of the item to get from the DriveCollectionPage

        Returns:
            :class:`Drive<microsoft.msgraph.model.drive.Drive>`:
                The Drive at the index
        """
        return Drive(self._prop_list[index])

    def drive(self):
        """Get a generator of Drive within the DriveCollectionPage
        
        Yields:
            :class:`Drive<microsoft.msgraph.model.drive.Drive>`:
                The next Drive in the collection
        """
        for item in self._prop_list:
            yield Drive(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the DriveCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = DriveCollectionRequest(next_page_link, client, options)
