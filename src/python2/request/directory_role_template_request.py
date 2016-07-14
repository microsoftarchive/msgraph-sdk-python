# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_role_template import DirectoryRoleTemplate
import json

class DirectoryRoleTemplateRequest(RequestBase):
    """The type DirectoryRoleTemplateRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryRoleTemplateRequest.

        Args:
            request_url (str): The url to perform the DirectoryRoleTemplateRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryRoleTemplateRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryRoleTemplate."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified DirectoryRoleTemplate.
        
        Returns:
            :class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The DirectoryRoleTemplate.
        """
        self.method = "GET"
        entity = DirectoryRoleTemplate(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, directory_role_template):
        """Updates the specified DirectoryRoleTemplate.
        
        Args:
            directory_role_template (:class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`):
                The DirectoryRoleTemplate to update.

        Returns:
            :class:`DirectoryRoleTemplate<microsoft.msgraph.model.directory_role_template.DirectoryRoleTemplate>`:
                The updated DirectoryRoleTemplate.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryRoleTemplate(json.loads(self.send(directory_role_template).content))
        self._initialize_collection_properties(entity)
        return entity

