# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .permission_request import PermissionRequest
from ..request_builder_base import RequestBuilderBase


class PermissionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the PermissionRequestBuilder

        Args:
            request_url (str): The url to perform the PermissionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`PermissionRequest<microsoft.msgraph.request.permission_request.PermissionRequest>`:
                The PermissionRequest
        """
        req = PermissionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Permission."""
        self.request().delete()

    def get(self):
        """Gets the specified Permission.
        
        Returns:
            :class:`Permission<microsoft.msgraph.model.permission.Permission>`:
                The Permission.
        """
        return self.request().get()

    def update(self, permission):
        """Updates the specified Permission.
        
        Args:
            permission (:class:`Permission<microsoft.msgraph.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<microsoft.msgraph.model.permission.Permission>`:
                The updated Permission
        """
        return self.request().update(permission)


