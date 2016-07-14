# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .directory_role_template_request import DirectoryRoleTemplateRequest
from ..request_builder_base import RequestBuilderBase


class DirectoryRoleTemplateRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DirectoryRoleTemplateRequestBuilder

        Args:
            request_url (str): The url to perform the DirectoryRoleTemplateRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DirectoryRoleTemplateRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the DirectoryRoleTemplateRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DirectoryRoleTemplateRequest<microsoft.msgraph.request.directory_role_template_request.DirectoryRoleTemplateRequest>`:
                The DirectoryRoleTemplateRequest
        """
        req = DirectoryRoleTemplateRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified DirectoryRoleTemplate."""
        self.request().delete()

    def get(self):
        """Gets the specified DirectoryRoleTemplate.
        
        Returns:
            :class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        return self.request().get()

    def update(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate.
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Returns:
            :class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate
        """
        return self.request().update(directory_role_template)


