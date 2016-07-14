# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_role import DirectoryRole
import json
import asyncio

class DirectoryRoleRequest(RequestBase):
    """The type DirectoryRoleRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryRoleRequest.

        Args:
            request_url (str): The url to perform the DirectoryRoleRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryRole."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryRole."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified DirectoryRole.
        
        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole.
        """
        self.method = "GET"
        entity = DirectoryRole(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryRole in async.

        Yields:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, directory_role):
        """Updates the specified DirectoryRole.
        
        Args:
            directory_role (:class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`):
                The DirectoryRole to update.

        Returns:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The updated DirectoryRole.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryRole(json.loads(self.send(directory_role).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, directory_role):
        """Updates the specified DirectoryRole in async
        
        Args:
            directory_role (:class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`):
                The DirectoryRole to update.

        Yields:
            :class:`DirectoryRole<msgraph.model.directory_role.DirectoryRole>`:
                The updated DirectoryRole.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    directory_role)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.members and value.members._prop_dict:
                if "members@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["members@odata.nextLink"]
                    value.members._init_next_page_request(next_page_link, self._client, None)
