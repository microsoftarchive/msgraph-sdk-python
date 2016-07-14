# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .organization_request import OrganizationRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class OrganizationRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the OrganizationRequestBuilder

        Args:
            request_url (str): The url to perform the OrganizationRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(OrganizationRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the OrganizationRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`OrganizationRequest<msgraph.request.organization_request.OrganizationRequest>`:
                The OrganizationRequest
        """
        req = OrganizationRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified Organization."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Organization."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Organization.
        
        Returns:
            :class:`Organization<msgraph.model.organization.Organization>`:
                The Organization.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Organization in async.

        Returns:
            :class:`Organization<msgraph.model.organization.Organization>`:
                The Organization.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, organization):
        """Updates the specified Organization.
        
        Args:
            organization (:class:`Organization<msgraph.model.organization.Organization>`):
                The Organization to update.

        Returns:
            :class:`Organization<msgraph.model.organization.Organization>`:
                The updated Organization
        """
        return self.request().update(organization)

    @asyncio.coroutine
    def update_async(self, organization):
        """Updates the specified Organization in async
        
        Args:
            organization (:class:`Organization<msgraph.model.organization.Organization>`):
                The Organization to update.

        Returns:
            :class:`Organization<msgraph.model.organization.Organization>`:
                The updated Organization.
        """
        entity = yield from self.request().update_async(organization)
        return entity

