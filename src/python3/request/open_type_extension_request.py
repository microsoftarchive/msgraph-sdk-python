# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.open_type_extension import OpenTypeExtension
import json
import asyncio

class OpenTypeExtensionRequest(RequestBase):
    """The type OpenTypeExtensionRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new OpenTypeExtensionRequest.

        Args:
            request_url (str): The url to perform the OpenTypeExtensionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(OpenTypeExtensionRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified OpenTypeExtension."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified OpenTypeExtension."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified OpenTypeExtension.
        
        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The OpenTypeExtension.
        """
        self.method = "GET"
        entity = OpenTypeExtension(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified OpenTypeExtension in async.

        Yields:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The OpenTypeExtension.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, open_type_extension):
        """Updates the specified OpenTypeExtension.
        
        Args:
            open_type_extension (:class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`):
                The OpenTypeExtension to update.

        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The updated OpenTypeExtension.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = OpenTypeExtension(json.loads(self.send(open_type_extension).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, open_type_extension):
        """Updates the specified OpenTypeExtension in async
        
        Args:
            open_type_extension (:class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`):
                The OpenTypeExtension to update.

        Yields:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The updated OpenTypeExtension.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    open_type_extension)
        entity = yield from future
        return entity

