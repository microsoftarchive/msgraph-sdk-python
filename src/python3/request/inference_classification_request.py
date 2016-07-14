# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.inference_classification import InferenceClassification
import json
import asyncio

class InferenceClassificationRequest(RequestBase):
    """The type InferenceClassificationRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new InferenceClassificationRequest.

        Args:
            request_url (str): The url to perform the InferenceClassificationRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(InferenceClassificationRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified InferenceClassification."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified InferenceClassification."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified InferenceClassification.
        
        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The InferenceClassification.
        """
        self.method = "GET"
        entity = InferenceClassification(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified InferenceClassification in async.

        Yields:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The InferenceClassification.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, inference_classification):
        """Updates the specified InferenceClassification.
        
        Args:
            inference_classification (:class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`):
                The InferenceClassification to update.

        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The updated InferenceClassification.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = InferenceClassification(json.loads(self.send(inference_classification).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, inference_classification):
        """Updates the specified InferenceClassification in async
        
        Args:
            inference_classification (:class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`):
                The InferenceClassification to update.

        Yields:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The updated InferenceClassification.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    inference_classification)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.overrides and value.overrides._prop_dict:
                if "overrides@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["overrides@odata.nextLink"]
                    value.overrides._init_next_page_request(next_page_link, self._client, None)
