# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_object import DirectoryObject
import json

class DirectoryObjectRequest(RequestBase):
    """The type DirectoryObjectRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryObjectRequest.

        Args:
            request_url (str): The url to perform the DirectoryObjectRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryObjectRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryObject."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified DirectoryObject.
        
        Returns:
            :class:`DirectoryObject<microsoft.msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject.
        """
        self.method = "GET"
        entity = DirectoryObject(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, directory_object):
        """Updates the specified DirectoryObject.
        
        Args:
            directory_object (:class:`DirectoryObject<microsoft.msgraph.model.directory_object.DirectoryObject>`):
                The DirectoryObject to update.

        Returns:
            :class:`DirectoryObject<microsoft.msgraph.model.directory_object.DirectoryObject>`:
                The updated DirectoryObject.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryObject(json.loads(self.send(directory_object).content))
        self._initialize_collection_properties(entity)
        return entity

