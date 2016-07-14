# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.contact import Contact
import json
import asyncio

class ContactRequest(RequestBase):
    """The type ContactRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ContactRequest.

        Args:
            request_url (str): The url to perform the ContactRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ContactRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Contact."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Contact."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Contact.
        
        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The Contact.
        """
        self.method = "GET"
        entity = Contact(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Contact in async.

        Yields:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The Contact.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, contact):
        """Updates the specified Contact.
        
        Args:
            contact (:class:`Contact<msgraph.model.contact.Contact>`):
                The Contact to update.

        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The updated Contact.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Contact(json.loads(self.send(contact).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, contact):
        """Updates the specified Contact in async
        
        Args:
            contact (:class:`Contact<msgraph.model.contact.Contact>`):
                The Contact to update.

        Yields:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The updated Contact.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    contact)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.email_addresses and value.email_addresses._prop_dict:
                if "email_addresses@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["email_addresses@odata.nextLink"]
                    value.email_addresses._init_next_page_request(next_page_link, self._client, None)
            if value.extensions and value.extensions._prop_dict:
                if "extensions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["extensions@odata.nextLink"]
                    value.extensions._init_next_page_request(next_page_link, self._client, None)
