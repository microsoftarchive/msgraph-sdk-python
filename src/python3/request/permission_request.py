# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.permission import Permission
import json
import asyncio

class PermissionRequest(RequestBase):
    """The type PermissionRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new PermissionRequest.

        Args:
            request_url (str): The url to perform the PermissionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(PermissionRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Permission."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Permission."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Permission.
        
        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The Permission.
        """
        self.method = "GET"
        entity = Permission(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Permission in async.

        Yields:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The Permission.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, permission):
        """Updates the specified Permission.
        
        Args:
            permission (:class:`Permission<msgraph.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The updated Permission.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Permission(json.loads(self.send(permission).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, permission):
        """Updates the specified Permission in async
        
        Args:
            permission (:class:`Permission<msgraph.model.permission.Permission>`):
                The Permission to update.

        Yields:
            :class:`Permission<msgraph.model.permission.Permission>`:
                The updated Permission.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    permission)
        entity = yield from future
        return entity

