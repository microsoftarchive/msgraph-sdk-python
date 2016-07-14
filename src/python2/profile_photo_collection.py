# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import profile_photo_request_builder # import ProfilePhotoRequestBuilder
#from .profile_photo_request_builder import ProfilePhotoRequestBuilder
from ..model.profile_photo import ProfilePhoto
import json

class ProfilePhotoCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ProfilePhotoCollectionRequest
        
        Args:
            request_url (str): The url to perform the ProfilePhotoCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ProfilePhotoCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ProfilePhotoCollectionPage

        Returns: 
            :class:`ProfilePhotoCollectionPage<microsoft.msgraph.request.profile_photo_collection.ProfilePhotoCollectionPage>`:
                The ProfilePhotoCollectionPage
        """
        self.method = "GET"
        collection_response = ProfilePhotoCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ProfilePhotoCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ProfilePhotoRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ProfilePhotoRequestBuilder for
        
        Returns: 
            :class:`ProfilePhotoRequestBuilder<microsoft.msgraph.request.profile_photo_request_builder.ProfilePhotoRequestBuilder>`:
                A ProfilePhotoRequestBuilder for that key
        """
        return profile_photo_request_builder.ProfilePhotoRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the ProfilePhotoCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ProfilePhotoCollectionRequest<microsoft.msgraph.request.profile_photo_collection.ProfilePhotoCollectionRequest>`:
                The ProfilePhotoCollectionRequest
        """
        req = ProfilePhotoCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ProfilePhotoCollectionPage

        Returns: 
            :class:`ProfilePhotoCollectionPage<microsoft.msgraph.request.profile_photo_collection.ProfilePhotoCollectionPage>`:
                The ProfilePhotoCollectionPage
        """
        return self.request().get()



class ProfilePhotoCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ProfilePhotoCollectionPage<microsoft.msgraph.request.profile_photo_collection.ProfilePhotoCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ProfilePhotoCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ProfilePhotoCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ProfilePhoto at the index specified
        
        Args:
            index (int): The index of the item to get from the ProfilePhotoCollectionPage

        Returns:
            :class:`ProfilePhoto<microsoft.msgraph.model.profile_photo.ProfilePhoto>`:
                The ProfilePhoto at the index
        """
        return ProfilePhoto(self._prop_list[index])

    def profile_photo(self):
        """Get a generator of ProfilePhoto within the ProfilePhotoCollectionPage
        
        Yields:
            :class:`ProfilePhoto<microsoft.msgraph.model.profile_photo.ProfilePhoto>`:
                The next ProfilePhoto in the collection
        """
        for item in self._prop_list:
            yield ProfilePhoto(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ProfilePhotoCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ProfilePhotoCollectionRequest(next_page_link, client, options)
