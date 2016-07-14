# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .contact_folder_request import ContactFolderRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import contact_collection
from ..request import contact_folder_collection


class ContactFolderRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ContactFolderRequestBuilder

        Args:
            request_url (str): The url to perform the ContactFolderRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ContactFolderRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ContactFolderRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ContactFolderRequest<msgraph.request.contact_folder_request.ContactFolderRequest>`:
                The ContactFolderRequest
        """
        req = ContactFolderRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified ContactFolder."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ContactFolder."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified ContactFolder.
        
        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ContactFolder in async.

        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, contact_folder):
        """Updates the specified ContactFolder.
        
        Args:
            contact_folder (:class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`):
                The ContactFolder to update.

        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The updated ContactFolder
        """
        return self.request().update(contact_folder)

    @asyncio.coroutine
    def update_async(self, contact_folder):
        """Updates the specified ContactFolder in async
        
        Args:
            contact_folder (:class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`):
                The ContactFolder to update.

        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The updated ContactFolder.
        """
        entity = yield from self.request().update_async(contact_folder)
        return entity

    @property
    def contacts(self):
        """The contacts for the ContactFolderRequestBuilder

        Returns: 
            :class:`ContactCollectionRequestBuilder<msgraph.request.contacts_collection.ContactCollectionRequestBuilder>`:
                A request builder created from the ContactFolderRequestBuilder
        """
        return contact_collection.ContactCollectionRequestBuilder(self.append_to_request_url("contacts"), self._client)

    @property
    def child_folders(self):
        """The child_folders for the ContactFolderRequestBuilder

        Returns: 
            :class:`ContactFolderCollectionRequestBuilder<msgraph.request.child_folders_collection.ContactFolderCollectionRequestBuilder>`:
                A request builder created from the ContactFolderRequestBuilder
        """
        return contact_folder_collection.ContactFolderCollectionRequestBuilder(self.append_to_request_url("childFolders"), self._client)

