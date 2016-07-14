# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import calendar_request_builder # import CalendarRequestBuilder
#from .calendar_request_builder import CalendarRequestBuilder
from ..model.calendar import Calendar
import json

class CalendarsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the CalendarsCollectionRequest
        
        Args:
            request_url (str): The url to perform the CalendarsCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(CalendarsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the CalendarsCollectionPage

        Returns: 
            :class:`CalendarsCollectionPage<microsoft.msgraph.request.calendars_collection.CalendarsCollectionPage>`:
                The CalendarsCollectionPage
        """
        self.method = "GET"
        collection_response = CalendarsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class CalendarsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the CalendarRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a CalendarRequestBuilder for
        
        Returns: 
            :class:`CalendarRequestBuilder<microsoft.msgraph.request.calendar_request_builder.CalendarRequestBuilder>`:
                A CalendarRequestBuilder for that key
        """
        return calendar_request_builder.CalendarRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the CalendarsCollectionRequest
        
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
            :class:`CalendarsCollectionRequest<microsoft.msgraph.request.calendars_collection.CalendarsCollectionRequest>`:
                The CalendarsCollectionRequest
        """
        req = CalendarsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the CalendarsCollectionPage

        Returns: 
            :class:`CalendarsCollectionPage<microsoft.msgraph.request.calendars_collection.CalendarsCollectionPage>`:
                The CalendarsCollectionPage
        """
        return self.request().get()



class CalendarsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`CalendarsCollectionPage<microsoft.msgraph.request.calendars_collection.CalendarsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = CalendarsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class CalendarsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Calendar at the index specified
        
        Args:
            index (int): The index of the item to get from the CalendarsCollectionPage

        Returns:
            :class:`Calendar<microsoft.msgraph.model.calendar.Calendar>`:
                The Calendar at the index
        """
        return Calendar(self._prop_list[index])

    def calendars(self):
        """Get a generator of Calendar within the CalendarsCollectionPage
        
        Yields:
            :class:`Calendar<microsoft.msgraph.model.calendar.Calendar>`:
                The next Calendar in the collection
        """
        for item in self._prop_list:
            yield Calendar(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the CalendarsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = CalendarsCollectionRequest(next_page_link, client, options)
