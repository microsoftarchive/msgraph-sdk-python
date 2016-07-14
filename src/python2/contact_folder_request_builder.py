# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .contact_folder_request import ContactFolderRequest
from ..request_builder_base import RequestBuilderBase
from ..request import contact_collection
from ..request import contact_folder_collection


class ContactFolderRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ContactFolderRequestBuilder

        Args:
            request_url (str): The url to perform the ContactFolderRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ContactFolderRequest<microsoft.msgraph.request.contact_folder_request.ContactFolderRequest>`:
                The ContactFolderRequest
        """
        req = ContactFolderRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ContactFolder."""
        self.request().delete()

    def get(self):
        """Gets the specified ContactFolder.
        
        Returns:
            :class:`ContactFolder<microsoft.msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder.
        """
        return self.request().get()

    def update(self, contact_folder):
        """Updates the specified ContactFolder.
        
        Args:
            contact_folder (:class:`ContactFolder<microsoft.msgraph.model.contact_folder.ContactFolder>`):
                The ContactFolder to update.

        Returns:
            :class:`ContactFolder<microsoft.msgraph.model.contact_folder.ContactFolder>`:
                The updated ContactFolder
        """
        return self.request().update(contact_folder)


    @property
    def contacts(self):
        """The contacts for the ContactFolderRequestBuilder

        Returns: 
            :class:`ContactCollectionRequestBuilder<microsoft.msgraph.request.contacts_collection.ContactCollectionRequestBuilder>`:
                A request builder created from the ContactFolderRequestBuilder
        """
        return contact_collection.ContactCollectionRequestBuilder(self.append_to_request_url("contacts"), self._client)

    @property
    def child_folders(self):
        """The child_folders for the ContactFolderRequestBuilder

        Returns: 
            :class:`ContactFolderCollectionRequestBuilder<microsoft.msgraph.request.child_folders_collection.ContactFolderCollectionRequestBuilder>`:
                A request builder created from the ContactFolderRequestBuilder
        """
        return contact_folder_collection.ContactFolderCollectionRequestBuilder(self.append_to_request_url("childFolders"), self._client)

