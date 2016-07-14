# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import organization_request_builder # import OrganizationRequestBuilder
#from .organization_request_builder import OrganizationRequestBuilder
from ..model.organization import Organization
import json

class OrganizationCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the OrganizationCollectionRequest
        
        Args:
            request_url (str): The url to perform the OrganizationCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(OrganizationCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the OrganizationCollectionPage

        Returns: 
            :class:`OrganizationCollectionPage<microsoft.msgraph.request.organization_collection.OrganizationCollectionPage>`:
                The OrganizationCollectionPage
        """
        self.method = "GET"
        collection_response = OrganizationCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class OrganizationCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the OrganizationRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a OrganizationRequestBuilder for
        
        Returns: 
            :class:`OrganizationRequestBuilder<microsoft.msgraph.request.organization_request_builder.OrganizationRequestBuilder>`:
                A OrganizationRequestBuilder for that key
        """
        return organization_request_builder.OrganizationRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the OrganizationCollectionRequest
        
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
            :class:`OrganizationCollectionRequest<microsoft.msgraph.request.organization_collection.OrganizationCollectionRequest>`:
                The OrganizationCollectionRequest
        """
        req = OrganizationCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the OrganizationCollectionPage

        Returns: 
            :class:`OrganizationCollectionPage<microsoft.msgraph.request.organization_collection.OrganizationCollectionPage>`:
                The OrganizationCollectionPage
        """
        return self.request().get()



class OrganizationCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`OrganizationCollectionPage<microsoft.msgraph.request.organization_collection.OrganizationCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = OrganizationCollectionPage(self._prop_dict["value"])

        return self._collection_page


class OrganizationCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Organization at the index specified
        
        Args:
            index (int): The index of the item to get from the OrganizationCollectionPage

        Returns:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The Organization at the index
        """
        return Organization(self._prop_list[index])

    def organization(self):
        """Get a generator of Organization within the OrganizationCollectionPage
        
        Yields:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The next Organization in the collection
        """
        for item in self._prop_list:
            yield Organization(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the OrganizationCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = OrganizationCollectionRequest(next_page_link, client, options)
