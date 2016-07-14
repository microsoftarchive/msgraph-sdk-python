# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.organization import Organization
import json

class OrganizationRequest(RequestBase):
    """The type OrganizationRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new OrganizationRequest.

        Args:
            request_url (str): The url to perform the OrganizationRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(OrganizationRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Organization."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Organization.
        
        Returns:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The Organization.
        """
        self.method = "GET"
        entity = Organization(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, organization):
        """Updates the specified Organization.
        
        Args:
            organization (:class:`Organization<microsoft.msgraph.model.organization.Organization>`):
                The Organization to update.

        Returns:
            :class:`Organization<microsoft.msgraph.model.organization.Organization>`:
                The updated Organization.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Organization(json.loads(self.send(organization).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.assigned_plans and value.assigned_plans._prop_dict:
                if "assigned_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["assigned_plans@odata.nextLink"]
                    value.assigned_plans._init_next_page_request(next_page_link, self._client, None)
            if value.provisioned_plans and value.provisioned_plans._prop_dict:
                if "provisioned_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["provisioned_plans@odata.nextLink"]
                    value.provisioned_plans._init_next_page_request(next_page_link, self._client, None)
            if value.verified_domains and value.verified_domains._prop_dict:
                if "verified_domains@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["verified_domains@odata.nextLink"]
                    value.verified_domains._init_next_page_request(next_page_link, self._client, None)
