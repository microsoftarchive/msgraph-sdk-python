# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import calendar_group_request_builder 
from ..model.calendar_group import CalendarGroup
import json
import asyncio

class CalendarGroupsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the CalendarGroupsCollectionRequest
        
        Args:
            request_url (str): The url to perform the CalendarGroupsCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(CalendarGroupsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the CalendarGroupsCollectionPage

        Returns: 
            :class:`CalendarGroupsCollectionPage<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The CalendarGroupsCollectionPage
        """
        self.method = "GET"
        collection_response = CalendarGroupsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the CalendarGroupsCollectionPage in async

        Yields: 
            :class:`CalendarGroupsCollectionPage<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The CalendarGroupsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class CalendarGroupsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the CalendarGroupRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a CalendarGroupRequestBuilder for
        
        Returns: 
            :class:`CalendarGroupRequestBuilder<msgraph.request.calendar_group_request_builder.CalendarGroupRequestBuilder>`:
                A CalendarGroupRequestBuilder for that key
        """
        return calendar_group_request_builder.CalendarGroupRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the CalendarGroupsCollectionRequest
        
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
            :class:`CalendarGroupsCollectionRequest<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionRequest>`:
                The CalendarGroupsCollectionRequest
        """
        req = CalendarGroupsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the CalendarGroupsCollectionPage

        Returns: 
            :class:`CalendarGroupsCollectionPage<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The CalendarGroupsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the CalendarGroupsCollectionPage in async

        Yields: 
            :class:`CalendarGroupsCollectionPage<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The CalendarGroupsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class CalendarGroupsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`CalendarGroupsCollectionPage<msgraph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = CalendarGroupsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class CalendarGroupsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the CalendarGroup at the index specified
        
        Args:
            index (int): The index of the item to get from the CalendarGroupsCollectionPage

        Returns:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The CalendarGroup at the index
        """
        return CalendarGroup(self._prop_list[index])

    def calendar_groups(self):
        """Get a generator of CalendarGroup within the CalendarGroupsCollectionPage
        
        Yields:
            :class:`CalendarGroup<msgraph.model.calendar_group.CalendarGroup>`:
                The next CalendarGroup in the collection
        """
        for item in self._prop_list:
            yield CalendarGroup(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the CalendarGroupsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = CalendarGroupsCollectionRequest(next_page_link, client, options)
