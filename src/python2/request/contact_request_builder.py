# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .contact_request import ContactRequest
from ..request_builder_base import RequestBuilderBase
from ..request import profile_photo_request_builder


class ContactRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ContactRequestBuilder

        Args:
            request_url (str): The url to perform the ContactRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
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
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ContactRequest<microsoft.msgraph.request.contact_request.ContactRequest>`:
                The ContactRequest
        """
        req = ContactRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Contact."""
        self.request().delete()

    def get(self):
        """Gets the specified Contact.
        
        Returns:
            :class:`Contact<microsoft.msgraph.model.contact.Contact>`:
                The Contact.
        """
        return self.request().get()

    def update(self, contact):
        """Updates the specified Contact.
        
        Args:
            contact (:class:`Contact<microsoft.msgraph.model.contact.Contact>`):
                The Contact to update.

        Returns:
            :class:`Contact<microsoft.msgraph.model.contact.Contact>`:
                The updated Contact
        """
        return self.request().update(contact)


    @property
    def photo(self):
        """The photo for the ContactRequestBuilder

        Returns: 
            :class:`ProfilePhotoRequestBuilder<microsoft.msgraph.request.profile_photo_request.ProfilePhotoRequestBuilder>`:
                A request builder created from the ContactRequestBuilder
        """
        return profile_photo_request_builder.ProfilePhotoRequestBuilder(self.append_to_request_url("photo"), self._client)


