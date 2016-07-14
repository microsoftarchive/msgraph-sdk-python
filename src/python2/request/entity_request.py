# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.entity import Entity
import json

class EntityRequest(RequestBase):
    """The type EntityRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new EntityRequest.

        Args:
            request_url (str): The url to perform the EntityRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EntityRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Entity."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Entity.
        
        Returns:
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The Entity.
        """
        self.method = "GET"
        entity = Entity(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, entity):
        """Updates the specified Entity.
        
        Args:
            entity (:class:`Entity<microsoft.msgraph.model.entity.Entity>`):
                The Entity to update.

        Returns:
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The updated Entity.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Entity(json.loads(self.send(entity).content))
        self._initialize_collection_properties(entity)
        return entity

