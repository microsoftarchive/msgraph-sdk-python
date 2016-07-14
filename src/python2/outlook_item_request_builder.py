# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .outlook_item_request import OutlookItemRequest
from ..request_builder_base import RequestBuilderBase


class OutlookItemRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the OutlookItemRequestBuilder

        Args:
            request_url (str): The url to perform the OutlookItemRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(OutlookItemRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the OutlookItemRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`OutlookItemRequest<microsoft.msgraph.request.outlook_item_request.OutlookItemRequest>`:
                The OutlookItemRequest
        """
        req = OutlookItemRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified OutlookItem."""
        self.request().delete()

    def get(self):
        """Gets the specified OutlookItem.
        
        Returns:
            :class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`:
                The OutlookItem.
        """
        return self.request().get()

    def update(self, outlook_item):
        """Updates the specified OutlookItem.
        
        Args:
            outlook_item (:class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`):
                The OutlookItem to update.

        Returns:
            :class:`OutlookItem<microsoft.msgraph.model.outlook_item.OutlookItem>`:
                The updated OutlookItem
        """
        return self.request().update(outlook_item)

    @property
    def event(self):
        """The event for the OutlookItemRequestBuilder

        Returns:
            :class:`EventRequestBuilder<microsoft.msgraph.request.event_request.EventRequestBuilder>`:
                A request builder created from the OutlookItemRequestBuilder
        """
        return EventRequestBuilder(self.append_to_request_url("event"), self._client)

    @property
    def message(self):
        """The message for the OutlookItemRequestBuilder

        Returns:
            :class:`MessageRequestBuilder<microsoft.msgraph.request.message_request.MessageRequestBuilder>`:
                A request builder created from the OutlookItemRequestBuilder
        """
        return MessageRequestBuilder(self.append_to_request_url("message"), self._client)

    @property
    def contact(self):
        """The contact for the OutlookItemRequestBuilder

        Returns:
            :class:`ContactRequestBuilder<microsoft.msgraph.request.contact_request.ContactRequestBuilder>`:
                A request builder created from the OutlookItemRequestBuilder
        """
        return ContactRequestBuilder(self.append_to_request_url("contact"), self._client)

    @property
    def post(self):
        """The post for the OutlookItemRequestBuilder

        Returns:
            :class:`PostRequestBuilder<microsoft.msgraph.request.post_request.PostRequestBuilder>`:
                A request builder created from the OutlookItemRequestBuilder
        """
        return PostRequestBuilder(self.append_to_request_url("post"), self._client)


