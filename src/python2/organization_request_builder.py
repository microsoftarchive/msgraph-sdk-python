# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .organization_request import OrganizationRequest
from ..request_builder_base import RequestBuilderBase


class OrganizationRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the OrganizationRequestBuilder

        Args:
            request_url (str): The url to perform the OrganizationRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(OrganizationRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the OrganizationRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`OrganizationRequest<microsoft.msgraph.request.organization_request.OrganizationRequest>`:
                The OrganizationRequest
        """
        req = OrganizationRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Organization."""
        self.request().delete()

    def get(self):
        """Gets the specified Organization.
        
        Returns:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The Organization.
        """
        return self.request().get()

    def update(self, organization):
        """Updates the specified Organization.
        
        Args:
            organization (:class:`Organization<microsoft.msgraph.model.organization.Organization>`):
                The Organization to update.

        Returns:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The updated Organization
        """
        return self.request().update(organization)


