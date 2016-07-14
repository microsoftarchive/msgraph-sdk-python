# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .directory_role_request import DirectoryRoleRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import directory_object_collection


class DirectoryRoleRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DirectoryRoleRequestBuilder

        Args:
            request_url (str): The url to perform the DirectoryRoleRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DirectoryRoleRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the DirectoryRoleRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DirectoryRoleRequest<msgraph.request.directory_role_request.DirectoryRoleRequest>`:
                The DirectoryRoleRequest
        """
        req = DirectoryRoleRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified DirectoryRole."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryRole."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified DirectoryRole.
        
        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryRole in async.

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, directory_role):
        """Updates the specified DirectoryRole.
        
        Args:
            directory_role (:class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`):
                The DirectoryRole to update.

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The updated DirectoryRole
        """
        return self.request().update(directory_role)

    @asyncio.coroutine
    def update_async(self, directory_role):
        """Updates the specified DirectoryRole in async
        
        Args:
            directory_role (:class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`):
                The DirectoryRole to update.

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The updated DirectoryRole.
        """
        entity = yield from self.request().update_async(directory_role)
        return entity

    @property
    def members(self):
        """The members for the DirectoryRoleRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.members_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the DirectoryRoleRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("members"), self._client)

