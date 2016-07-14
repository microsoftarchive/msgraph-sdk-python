# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .drive_item_request import DriveItemRequest
from ..request_builder_base import RequestBuilderBase
from ..request.drive_item_create_link import DriveItemCreateLinkRequestBuilder
from ..request.drive_item_copy import DriveItemCopyRequestBuilder
from ..request.drive_item_search import DriveItemSearchRequestBuilder
from ..request.drive_item_delta import DriveItemDeltaRequestBuilder
from ..request.drive_item_content_request import DriveItemContentRequestBuilder
import asyncio

from ..request import user_request_builder
from ..request import permission_collection
from ..request import drive_item_collection
from ..request import thumbnail_set_collection


class DriveItemRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DriveItemRequestBuilder

        Args:
            request_url (str): The url to perform the DriveItemRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DriveItemRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the DriveItemRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DriveItemRequest<msgraph.request.drive_item_request.DriveItemRequest>`:
                The DriveItemRequest
        """
        req = DriveItemRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified DriveItem."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DriveItem."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified DriveItem.
        
        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The DriveItem.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DriveItem in async.

        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The DriveItem.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, drive_item):
        """Updates the specified DriveItem.
        
        Args:
            drive_item (:class:`DriveItem<msgraph.model.drive_item.DriveItem>`):
                The DriveItem to update.

        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The updated DriveItem
        """
        return self.request().update(drive_item)

    @asyncio.coroutine
    def update_async(self, drive_item):
        """Updates the specified DriveItem in async
        
        Args:
            drive_item (:class:`DriveItem<msgraph.model.drive_item.DriveItem>`):
                The DriveItem to update.

        Returns:
            :class:`DriveItem<msgraph.model.drive_item.DriveItem>`:
                The updated DriveItem.
        """
        entity = yield from self.request().update_async(drive_item)
        return entity

    def upload(self, local_path):
        """Uploads the file using PUT
        
        Args:
            local_path (str): The path to the local file to upload.

        Returns: 
            The created entity.
        """
        return self.content.request().upload(local_path)

    @asyncio.coroutine
    def upload_async(self, local_path):
        """Uploads the file using PUT in async
        
        Args:
            local_path (str): The path to the local file to upload.

        Returns: The created entity.
        """
        entity = yield from self.content.request().upload_async(local_path)
        return entity

    def download(self, local_path):
        """Downloads the specified entity.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        return self.content.request().download(local_path)

    @asyncio.coroutine
    def download_async(self, local_path):
        """Downloads the specified entity in async.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        entity = yield from self.content.request().download_async(local_path)
        return entity

    @property
    def created_by_user(self):
        """The created_by_user for the DriveItemRequestBuilder

        Returns: 
            :class:`UserRequestBuilder<msgraph.request.user_request.UserRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return user_request_builder.UserRequestBuilder(self.append_to_request_url("createdByUser"), self._client)


    @property
    def last_modified_by_user(self):
        """The last_modified_by_user for the DriveItemRequestBuilder

        Returns: 
            :class:`UserRequestBuilder<msgraph.request.user_request.UserRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return user_request_builder.UserRequestBuilder(self.append_to_request_url("lastModifiedByUser"), self._client)


    @property
    def permissions(self):
        """The permissions for the DriveItemRequestBuilder

        Returns: 
            :class:`PermissionCollectionRequestBuilder<msgraph.request.permissions_collection.PermissionCollectionRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return permission_collection.PermissionCollectionRequestBuilder(self.append_to_request_url("permissions"), self._client)

    @property
    def children(self):
        """The children for the DriveItemRequestBuilder

        Returns: 
            :class:`DriveItemCollectionRequestBuilder<msgraph.request.children_collection.DriveItemCollectionRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return drive_item_collection.DriveItemCollectionRequestBuilder(self.append_to_request_url("children"), self._client)

    @property
    def thumbnails(self):
        """The thumbnails for the DriveItemRequestBuilder

        Returns: 
            :class:`ThumbnailSetCollectionRequestBuilder<msgraph.request.thumbnails_collection.ThumbnailSetCollectionRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return thumbnail_set_collection.ThumbnailSetCollectionRequestBuilder(self.append_to_request_url("thumbnails"), self._client)

    @property
    def content(self):
        """The content for the DriveItemRequestBuilder

        Returns: 
            :class:`DriveItemContentRequestBuilder<msgraph.request.drive_item_content.DriveItemContentRequestBuilder>`:
                A request builder created from the DriveItemRequestBuilder
        """
        return DriveItemContentRequestBuilder(self.append_to_request_url("content"), self._client)
    def create_link(self, type, scope=None):
        """Executes the createLink method

        Args:
            type (str):
                The type to use in the method request          
            scope (str):
                The scope to use in the method request          

        Returns:
            :class:`DriveItemCreateLinkRequestBuilder<msgraph.request.drive_item_create_link.DriveItemCreateLinkRequestBuilder>`:
                A DriveItemCreateLinkRequestBuilder for the method
        """
        return DriveItemCreateLinkRequestBuilder(self.append_to_request_url("createLink"), self._client, type, scope=scope)

    def copy(self, name=None, parent_reference=None):
        """Executes the copy method

        Args:
            name (str):
                The name to use in the method request          
            parent_reference (:class:`ItemReference<msgraph.model.item_reference.ItemReference>`):
                Defaults to None, The parent_reference to use in the method request

        Returns:
            :class:`DriveItemCopyRequestBuilder<msgraph.request.drive_item_copy.DriveItemCopyRequestBuilder>`:
                A DriveItemCopyRequestBuilder for the method
        """
        return DriveItemCopyRequestBuilder(self.append_to_request_url("copy"), self._client, name=name, parent_reference=parent_reference)

    def search(self, q=None):
        """Executes the search method

        Args:
            q (str):
                The q to use in the method request          

        Returns:
            :class:`DriveItemSearchRequestBuilder<msgraph.request.drive_item_search.DriveItemSearchRequestBuilder>`:
                A DriveItemSearchRequestBuilder for the method
        """
        return DriveItemSearchRequestBuilder(self.append_to_request_url("search"), self._client, q=q)

    def delta(self, token=None):
        """Executes the delta method

        Args:
            token (str):
                The token to use in the method request          

        Returns:
            :class:`DriveItemDeltaRequestBuilder<msgraph.request.drive_item_delta.DriveItemDeltaRequestBuilder>`:
                A DriveItemDeltaRequestBuilder for the method
        """
        return DriveItemDeltaRequestBuilder(self.append_to_request_url("delta"), self._client, token=token)


