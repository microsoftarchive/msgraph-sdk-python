# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.inference_classification_override import InferenceClassificationOverride
import json
import asyncio

class InferenceClassificationOverrideRequest(RequestBase):
    """The type InferenceClassificationOverrideRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new InferenceClassificationOverrideRequest.

        Args:
            request_url (str): The url to perform the InferenceClassificationOverrideRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(InferenceClassificationOverrideRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified InferenceClassificationOverride."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified InferenceClassificationOverride."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified InferenceClassificationOverride.
        
        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The InferenceClassificationOverride.
        """
        self.method = "GET"
        entity = InferenceClassificationOverride(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified InferenceClassificationOverride in async.

        Yields:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The InferenceClassificationOverride.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, inference_classification_override):
        """Updates the specified InferenceClassificationOverride.
        
        Args:
            inference_classification_override (:class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`):
                The InferenceClassificationOverride to update.

        Returns:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The updated InferenceClassificationOverride.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = InferenceClassificationOverride(json.loads(self.send(inference_classification_override).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, inference_classification_override):
        """Updates the specified InferenceClassificationOverride in async
        
        Args:
            inference_classification_override (:class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`):
                The InferenceClassificationOverride to update.

        Yields:
            :class:`InferenceClassificationOverride<msgraph.model.inference_classification_override.InferenceClassificationOverride>`:
                The updated InferenceClassificationOverride.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    inference_classification_override)
        entity = yield from future
        return entity

