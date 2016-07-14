# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .open_type_extension_request import OpenTypeExtensionRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class OpenTypeExtensionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the OpenTypeExtensionRequestBuilder

        Args:
            request_url (str): The url to perform the OpenTypeExtensionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(OpenTypeExtensionRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the OpenTypeExtensionRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`OpenTypeExtensionRequest<msgraph.request.open_type_extension_request.OpenTypeExtensionRequest>`:
                The OpenTypeExtensionRequest
        """
        req = OpenTypeExtensionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified OpenTypeExtension."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified OpenTypeExtension."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified OpenTypeExtension.
        
        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The OpenTypeExtension.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified OpenTypeExtension in async.

        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The OpenTypeExtension.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, open_type_extension):
        """Updates the specified OpenTypeExtension.
        
        Args:
            open_type_extension (:class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`):
                The OpenTypeExtension to update.

        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The updated OpenTypeExtension
        """
        return self.request().update(open_type_extension)

    @asyncio.coroutine
    def update_async(self, open_type_extension):
        """Updates the specified OpenTypeExtension in async
        
        Args:
            open_type_extension (:class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`):
                The OpenTypeExtension to update.

        Returns:
            :class:`OpenTypeExtension<msgraph.model.open_type_extension.OpenTypeExtension>`:
                The updated OpenTypeExtension.
        """
        entity = yield from self.request().update_async(open_type_extension)
        return entity

