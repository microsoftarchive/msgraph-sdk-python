# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.directory_object import DirectoryObject
import json
import asyncio

class DirectoryObjectRequest(RequestBase):
    """The type DirectoryObjectRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DirectoryObjectRequest.

        Args:
            request_url (str): The url to perform the DirectoryObjectRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DirectoryObjectRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified DirectoryObject."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryObject."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified DirectoryObject.
        
        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject.
        """
        self.method = "GET"
        entity = DirectoryObject(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryObject in async.

        Yields:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, directory_object):
        """Updates the specified DirectoryObject.
        
        Args:
            directory_object (:class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`):
                The DirectoryObject to update.

        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The updated DirectoryObject.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = DirectoryObject(json.loads(self.send(directory_object).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, directory_object):
        """Updates the specified DirectoryObject in async
        
        Args:
            directory_object (:class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`):
                The DirectoryObject to update.

        Yields:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The updated DirectoryObject.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    directory_object)
        entity = yield from future
        return entity

