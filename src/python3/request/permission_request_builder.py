# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .permission_request import PermissionRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class PermissionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the PermissionRequestBuilder

        Args:
            request_url (str): The url to perform the PermissionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(PermissionRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the PermissionRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`PermissionRequest<msgraph.request.permission_request.PermissionRequest>`:
                The PermissionRequest
        """
        req = PermissionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Permission."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Permission."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Permission.
        
        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The Permission.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Permission in async.

        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The Permission.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, permission):
        """Updates the specified Permission.
        
        Args:
            permission (:class:`Permission<msgraph.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The updated Permission
        """
        return self.request().update(permission)

    @asyncio.coroutine
    def update_async(self, permission):
        """Updates the specified Permission in async
        
        Args:
            permission (:class:`Permission<msgraph.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The updated Permission.
        """
        entity = yield from self.request().update_async(permission)
        return entity

