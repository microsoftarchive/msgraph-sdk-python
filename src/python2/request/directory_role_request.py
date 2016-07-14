# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_role import DirectoryRole
import json

class DirectoryRoleRequest(RequestBase):
    """The type DirectoryRoleRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryRoleRequest.

        Args:
            request_url (str): The url to perform the DirectoryRoleRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryRole."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified DirectoryRole.
        
        Returns:
            :class:`DirectoryRole<microsoft.msgraph.model.directory_role.DirectoryRole>`:
                The DirectoryRole.
        """
        self.method = "GET"
        entity = DirectoryRole(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, directory_role):
        """Updates the specified DirectoryRole.
        
        Args:
            directory_role (:class:`DirectoryRole<microsoft.msgraph.model.directory_role.DirectoryRole>`):
                The DirectoryRole to update.

        Returns:
            :class:`DirectoryRole<microsoft.msgraph.model.directory_role.DirectoryRole>`:
                The updated DirectoryRole.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryRole(json.loads(self.send(directory_role).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.members and value.members._prop_dict:
                if "members@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["members@odata.nextLink"]
                    value.members._init_next_page_request(next_page_link, self._client, None)
