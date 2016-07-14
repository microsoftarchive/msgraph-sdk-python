# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .profile_photo_request import ProfilePhotoRequest
from ..request_builder_base import RequestBuilderBase
import asyncio



class ProfilePhotoRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ProfilePhotoRequestBuilder

        Args:
            request_url (str): The url to perform the ProfilePhotoRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ProfilePhotoRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ProfilePhotoRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ProfilePhotoRequest<msgraph.request.profile_photo_request.ProfilePhotoRequest>`:
                The ProfilePhotoRequest
        """
        req = ProfilePhotoRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified ProfilePhoto."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ProfilePhoto."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified ProfilePhoto.
        
        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ProfilePhoto in async.

        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, profile_photo):
        """Updates the specified ProfilePhoto.
        
        Args:
            profile_photo (:class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`):
                The ProfilePhoto to update.

        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The updated ProfilePhoto
        """
        return self.request().update(profile_photo)

    @asyncio.coroutine
    def update_async(self, profile_photo):
        """Updates the specified ProfilePhoto in async
        
        Args:
            profile_photo (:class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`):
                The ProfilePhoto to update.

        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The updated ProfilePhoto.
        """
        entity = yield from self.request().update_async(profile_photo)
        return entity

