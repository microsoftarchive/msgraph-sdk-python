# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_role_template import DirectoryRoleTemplate
import json
import asyncio

class DirectoryRoleTemplateRequest(RequestBase):
    """The type DirectoryRoleTemplateRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryRoleTemplateRequest.

        Args:
            request_url (str): The url to perform the DirectoryRoleTemplateRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleTemplateRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryRoleTemplate."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryRoleTemplate."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified DirectoryRoleTemplate.
        
        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        self.method = "GET"
        entity = DirectoryRoleTemplate(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryRoleTemplate in async.

        Yields:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate.
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Returns:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryRoleTemplate(json.loads(self.send(directory_role_template).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate in async
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Yields:
            :class:`DirectoryRoleTemplate<msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    directory_role_template)
        entity = yield from future
        return entity

