# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.profile_photo import ProfilePhoto
import json

class ProfilePhotoRequest(RequestBase):
    """The type ProfilePhotoRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ProfilePhotoRequest.

        Args:
            request_url (str): The url to perform the ProfilePhotoRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ProfilePhotoRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ProfilePhoto."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified ProfilePhoto.
        
        Returns:
            :class:`ProfilePhoto<microsoft.msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto.
        """
        self.method = "GET"
        entity = ProfilePhoto(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, profile_photo):
        """Updates the specified ProfilePhoto.
        
        Args:
            profile_photo (:class:`ProfilePhoto<microsoft.msgraph.model.profile_photo.ProfilePhoto>`):
                The ProfilePhoto to update.

        Returns:
            :class:`ProfilePhoto<microsoft.msgraph.model.profile_photo.ProfilePhoto>`:
                The updated ProfilePhoto.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ProfilePhoto(json.loads(self.send(profile_photo).content))
        self._initialize_collection_properties(entity)
        return entity

