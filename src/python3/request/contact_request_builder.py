# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .contact_request import ContactRequest
from ..request_builder_base import RequestBuilderBase
import asyncio

from ..request import extension_collection
from ..request import profile_photo_request_builder


class ContactRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ContactRequestBuilder

        Args:
            request_url (str): The url to perform the ContactRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(ContactRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ContactRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ContactRequest<msgraph.request.contact_request.ContactRequest>`:
                The ContactRequest
        """
        req = ContactRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, )
        return req

    def delete(self):
        """Deletes the specified Contact."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Contact."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Contact.
        
        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The Contact.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Contact in async.

        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The Contact.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, contact):
        """Updates the specified Contact.
        
        Args:
            contact (:class:`Contact<msgraph.model.contact.Contact>`):
                The Contact to update.

        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The updated Contact
        """
        return self.request().update(contact)

    @asyncio.coroutine
    def update_async(self, contact):
        """Updates the specified Contact in async
        
        Args:
            contact (:class:`Contact<msgraph.model.contact.Contact>`):
                The Contact to update.

        Returns:
            :class:`Contact<msgraph.model.contact.Contact>`:
                The updated Contact.
        """
        entity = yield from self.request().update_async(contact)
        return entity

    @property
    def extensions(self):
        """The extensions for the ContactRequestBuilder

        Returns: 
            :class:`ExtensionCollectionRequestBuilder<msgraph.request.extensions_collection.ExtensionCollectionRequestBuilder>`:
                A request builder created from the ContactRequestBuilder
        """
        return extension_collection.ExtensionCollectionRequestBuilder(self.append_to_request_url("extensions"), self._client)

    @property
    def photo(self):
        """The photo for the ContactRequestBuilder

        Returns: 
            :class:`ProfilePhotoRequestBuilder<msgraph.request.profile_photo_request.ProfilePhotoRequestBuilder>`:
                A request builder created from the ContactRequestBuilder
        """
        return profile_photo_request_builder.ProfilePhotoRequestBuilder(self.append_to_request_url("photo"), self._client)


