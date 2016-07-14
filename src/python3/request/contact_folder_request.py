# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.contact_folder import ContactFolder
import json
import asyncio

class ContactFolderRequest(RequestBase):
    """The type ContactFolderRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ContactFolderRequest.

        Args:
            request_url (str): The url to perform the ContactFolderRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ContactFolderRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ContactFolder."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ContactFolder."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified ContactFolder.
        
        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder.
        """
        self.method = "GET"
        entity = ContactFolder(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ContactFolder in async.

        Yields:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The ContactFolder.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, contact_folder):
        """Updates the specified ContactFolder.
        
        Args:
            contact_folder (:class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`):
                The ContactFolder to update.

        Returns:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The updated ContactFolder.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ContactFolder(json.loads(self.send(contact_folder).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, contact_folder):
        """Updates the specified ContactFolder in async
        
        Args:
            contact_folder (:class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`):
                The ContactFolder to update.

        Yields:
            :class:`ContactFolder<msgraph.model.contact_folder.ContactFolder>`:
                The updated ContactFolder.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    contact_folder)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.contacts and value.contacts._prop_dict:
                if "contacts@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["contacts@odata.nextLink"]
                    value.contacts._init_next_page_request(next_page_link, self._client, None)
            if value.child_folders and value.child_folders._prop_dict:
                if "child_folders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["child_folders@odata.nextLink"]
                    value.child_folders._init_next_page_request(next_page_link, self._client, None)
