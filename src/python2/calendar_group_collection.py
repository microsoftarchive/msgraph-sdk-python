# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import calendar_group_request_builder # import CalendarGroupRequestBuilder
#from .calendar_group_request_builder import CalendarGroupRequestBuilder
from ..model.calendar_group import CalendarGroup
import json

class CalendarGroupCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the CalendarGroupCollectionRequest
        
        Args:
            request_url (str): The url to perform the CalendarGroupCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(CalendarGroupCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the CalendarGroupCollectionPage

        Returns: 
            :class:`CalendarGroupCollectionPage<microsoft.msgraph.request.calendar_group_collection.CalendarGroupCollectionPage>`:
                The CalendarGroupCollectionPage
        """
        self.method = "GET"
        collection_response = CalendarGroupCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class CalendarGroupCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the CalendarGroupRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a CalendarGroupRequestBuilder for
        
        Returns: 
            :class:`CalendarGroupRequestBuilder<microsoft.msgraph.request.calendar_group_request_builder.CalendarGroupRequestBuilder>`:
                A CalendarGroupRequestBuilder for that key
        """
        return calendar_group_request_builder.CalendarGroupRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the CalendarGroupCollectionRequest
        
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
            :class:`CalendarGroupCollectionRequest<microsoft.msgraph.request.calendar_group_collection.CalendarGroupCollectionRequest>`:
                The CalendarGroupCollectionRequest
        """
        req = CalendarGroupCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the CalendarGroupCollectionPage

        Returns: 
            :class:`CalendarGroupCollectionPage<microsoft.msgraph.request.calendar_group_collection.CalendarGroupCollectionPage>`:
                The CalendarGroupCollectionPage
        """
        return self.request().get()



class CalendarGroupCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`CalendarGroupCollectionPage<microsoft.msgraph.request.calendar_group_collection.CalendarGroupCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = CalendarGroupCollectionPage(self._prop_dict["value"])

        return self._collection_page


class CalendarGroupCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the CalendarGroup at the index specified
        
        Args:
            index (int): The index of the item to get from the CalendarGroupCollectionPage

        Returns:
            :class:`CalendarGroup<microsoft.msgraph.model.calendar_group.CalendarGroup>`:
                The CalendarGroup at the index
        """
        return CalendarGroup(self._prop_list[index])

    def calendar_group(self):
        """Get a generator of CalendarGroup within the CalendarGroupCollectionPage
        
        Yields:
            :class:`CalendarGroup<microsoft.msgraph.model.calendar_group.CalendarGroup>`:
                The next CalendarGroup in the collection
        """
        for item in self._prop_list:
            yield CalendarGroup(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the CalendarGroupCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = CalendarGroupCollectionRequest(next_page_link, client, options)
