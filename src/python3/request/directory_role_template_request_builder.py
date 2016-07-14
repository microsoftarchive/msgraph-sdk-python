# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .directory_role_template_request import DirectoryRoleTemplateRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class DirectoryRoleTemplateRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DirectoryRoleTemplateRequestBuilder

        Args:
            request_url (str): The url to perform the DirectoryRoleTemplateRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DirectoryRoleTemplateRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the DirectoryRoleTemplateRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DirectoryRoleTemplateRequest<msgraph.request.directory_role_template_request.DirectoryRoleTemplateRequest>`:
                The DirectoryRoleTemplateRequest
        """
        req = DirectoryRoleTemplateRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified DirectoryRoleTemplate."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryRoleTemplate."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified DirectoryRoleTemplate.
        
        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryRoleTemplate in async.

        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate.
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate
        """
        return self.request().update(directory_role_template)

    @asyncio.coroutine
    def update_async(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate in async
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate.
        """
        entity = yield from self.request().update_async(directory_role_template)
        return entity

