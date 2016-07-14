# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .inference_classification_override_request import InferenceClassificationOverrideRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class InferenceClassificationOverrideRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the InferenceClassificationOverrideRequestBuilder

        Args:
            request_url (str): The url to perform the InferenceClassificationOverrideRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(InferenceClassificationOverrideRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the InferenceClassificationOverrideRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`InferenceClassificationOverrideRequest<msgraph.request.inference_classification_override_request.InferenceClassificationOverrideRequest>`:
                The InferenceClassificationOverrideRequest
        """
        req = InferenceClassificationOverrideRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified InferenceClassificationOverride."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified InferenceClassificationOverride."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified InferenceClassificationOverride.
        
        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The InferenceClassificationOverride.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified InferenceClassificationOverride in async.

        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The InferenceClassificationOverride.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, inference_classification_override):
        """Updates the specified InferenceClassificationOverride.
        
        Args:
            inference_classification_override (:class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`):
                The InferenceClassificationOverride to update.

        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The updated InferenceClassificationOverride
        """
        return self.request().update(inference_classification_override)

    @asyncio.coroutine
    def update_async(self, inference_classification_override):
        """Updates the specified InferenceClassificationOverride in async
        
        Args:
            inference_classification_override (:class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`):
                The InferenceClassificationOverride to update.

        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The updated InferenceClassificationOverride.
        """
        entity = yield from self.request().update_async(inference_classification_override)
        return entity

