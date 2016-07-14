# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .extension_request import ExtensionRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class ExtensionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ExtensionRequestBuilder

        Args:
            request_url (str): The url to perform the ExtensionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ExtensionRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ExtensionRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ExtensionRequest<msgraph.request.extension_request.ExtensionRequest>`:
                The ExtensionRequest
        """
        req = ExtensionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Extension."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Extension."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Extension.
        
        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The Extension.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Extension in async.

        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The Extension.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, extension):
        """Updates the specified Extension.
        
        Args:
            extension (:class:`Extension<msgraph.model.extension.Extension>`):
                The Extension to update.

        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The updated Extension
        """
        return self.request().update(extension)

    @asyncio.coroutine
    def update_async(self, extension):
        """Updates the specified Extension in async
        
        Args:
            extension (:class:`Extension<msgraph.model.extension.Extension>`):
                The Extension to update.

        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The updated Extension.
        """
        entity = yield from self.request().update_async(extension)
        return entity
    @property
    def open_type_extension(self):
        """The open_type_extension for the ExtensionRequestBuilder

        Returns:
            :class:`OpenTypeExtensionRequestBuilder<msgraph.request.open_type_extension_request.OpenTypeExtensionRequestBuilder>`:
                A request builder created from the ExtensionRequestBuilder
        """
        return OpenTypeExtensionRequestBuilder(self.append_to_request_url("openTypeExtension"), self._client)


