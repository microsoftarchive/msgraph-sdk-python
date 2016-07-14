# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.profile_photo import ProfilePhoto
import json
import asyncio

class ProfilePhotoRequest(RequestBase):
    """The type ProfilePhotoRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ProfilePhotoRequest.

        Args:
            request_url (str): The url to perform the ProfilePhotoRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ProfilePhotoRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ProfilePhoto."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ProfilePhoto."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified ProfilePhoto.
        
        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto.
        """
        self.method = "GET"
        entity = ProfilePhoto(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ProfilePhoto in async.

        Yields:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, profile_photo):
        """Updates the specified ProfilePhoto.
        
        Args:
            profile_photo (:class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`):
                The ProfilePhoto to update.

        Returns:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The updated ProfilePhoto.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ProfilePhoto(json.loads(self.send(profile_photo).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, profile_photo):
        """Updates the specified ProfilePhoto in async
        
        Args:
            profile_photo (:class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`):
                The ProfilePhoto to update.

        Yields:
            :class:`ProfilePhoto<msgraph.model.profile_photo.ProfilePhoto>`:
                The updated ProfilePhoto.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    profile_photo)
        entity = yield from future
        return entity

