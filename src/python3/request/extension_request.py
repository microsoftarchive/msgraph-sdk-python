# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.extension import Extension
import json
import asyncio

class ExtensionRequest(RequestBase):
    """The type ExtensionRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ExtensionRequest.

        Args:
            request_url (str): The url to perform the ExtensionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ExtensionRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Extension."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Extension."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Extension.
        
        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The Extension.
        """
        self.method = "GET"
        entity = Extension(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Extension in async.

        Yields:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The Extension.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, extension):
        """Updates the specified Extension.
        
        Args:
            extension (:class:`Extension<msgraph.model.extension.Extension>`):
                The Extension to update.

        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The updated Extension.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Extension(json.loads(self.send(extension).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, extension):
        """Updates the specified Extension in async
        
        Args:
            extension (:class:`Extension<msgraph.model.extension.Extension>`):
                The Extension to update.

        Yields:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The updated Extension.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    extension)
        entity = yield from future
        return entity

