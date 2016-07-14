# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .inference_classification_request import InferenceClassificationRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import inference_classification_override_collection


class InferenceClassificationRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the InferenceClassificationRequestBuilder

        Args:
            request_url (str): The url to perform the InferenceClassificationRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(InferenceClassificationRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the InferenceClassificationRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`InferenceClassificationRequest<msgraph.request.inference_classification_request.InferenceClassificationRequest>`:
                The InferenceClassificationRequest
        """
        req = InferenceClassificationRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified InferenceClassification."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified InferenceClassification."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified InferenceClassification.
        
        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The InferenceClassification.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified InferenceClassification in async.

        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The InferenceClassification.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, inference_classification):
        """Updates the specified InferenceClassification.
        
        Args:
            inference_classification (:class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`):
                The InferenceClassification to update.

        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The updated InferenceClassification
        """
        return self.request().update(inference_classification)

    @asyncio.coroutine
    def update_async(self, inference_classification):
        """Updates the specified InferenceClassification in async
        
        Args:
            inference_classification (:class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`):
                The InferenceClassification to update.

        Returns:
            :class:`InferenceClassification<msgraph.model.inference_classification.InferenceClassification>`:
                The updated InferenceClassification.
        """
        entity = yield from self.request().update_async(inference_classification)
        return entity

    @property
    def overrides(self):
        """The overrides for the InferenceClassificationRequestBuilder

        Returns: 
            :class:`InferenceClassificationOverrideCollectionRequestBuilder<msgraph.request.overrides_collection.InferenceClassificationOverrideCollectionRequestBuilder>`:
                A request builder created from the InferenceClassificationRequestBuilder
        """
        return inference_classification_override_collection.InferenceClassificationOverrideCollectionRequestBuilder(self.append_to_request_url("overrides"), self._client)

