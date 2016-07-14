# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.entity import Entity
import json
import asyncio

class EntityRequest(RequestBase):
    """The type EntityRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new EntityRequest.

        Args:
            request_url (str): The url to perform the EntityRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(EntityRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Entity."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Entity."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Entity.
        
        Returns:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The Entity.
        """
        self.method = "GET"
        entity = Entity(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Entity in async.

        Yields:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The Entity.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, entity):
        """Updates the specified Entity.
        
        Args:
            entity (:class:`Entity<msgraph.model.entity.Entity>`):
                The Entity to update.

        Returns:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The updated Entity.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Entity(json.loads(self.send(entity).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, entity):
        """Updates the specified Entity in async
        
        Args:
            entity (:class:`Entity<msgraph.model.entity.Entity>`):
                The Entity to update.

        Yields:
            :class:`Entity<msgraph.model.entity.Entity>`:
                The updated Entity.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    entity)
        entity = yield from future
        return entity

