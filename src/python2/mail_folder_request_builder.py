# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .mail_folder_request import MailFolderRequest
from ..request_builder_base import RequestBuilderBase
from ..request.mail_folder_copy import MailFolderCopyRequestBuilder
from ..request.mail_folder_move import MailFolderMoveRequestBuilder
from ..request import message_collection
from ..request import mail_folder_collection


class MailFolderRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the MailFolderRequestBuilder

        Args:
            request_url (str): The url to perform the MailFolderRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(MailFolderRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the MailFolderRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`MailFolderRequest<microsoft.msgraph.request.mail_folder_request.MailFolderRequest>`:
                The MailFolderRequest
        """
        req = MailFolderRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified MailFolder."""
        self.request().delete()

    def get(self):
        """Gets the specified MailFolder.
        
        Returns:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The MailFolder.
        """
        return self.request().get()

    def update(self, mail_folder):
        """Updates the specified MailFolder.
        
        Args:
            mail_folder (:class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`):
                The MailFolder to update.

        Returns:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The updated MailFolder
        """
        return self.request().update(mail_folder)


    @property
    def messages(self):
        """The messages for the MailFolderRequestBuilder

        Returns: 
            :class:`MessageCollectionRequestBuilder<microsoft.msgraph.request.messages_collection.MessageCollectionRequestBuilder>`:
                A request builder created from the MailFolderRequestBuilder
        """
        return message_collection.MessageCollectionRequestBuilder(self.append_to_request_url("messages"), self._client)

    @property
    def child_folders(self):
        """The child_folders for the MailFolderRequestBuilder

        Returns: 
            :class:`MailFolderCollectionRequestBuilder<microsoft.msgraph.request.child_folders_collection.MailFolderCollectionRequestBuilder>`:
                A request builder created from the MailFolderRequestBuilder
        """
        return mail_folder_collection.MailFolderCollectionRequestBuilder(self.append_to_request_url("childFolders"), self._client)
    def copy(self, destination_id=None):
        """Executes the copy method

        Args:
            destination_id (str):
                The destination_id to use in the method request          

        Returns:
            :class:`MailFolderCopyRequestBuilder<microsoft.msgraph.request.mail_folder_copy.MailFolderCopyRequestBuilder>`:
                A MailFolderCopyRequestBuilder for the method
        """
        return MailFolderCopyRequestBuilder(self.append_to_request_url("copy"), self._client, destination_id=destination_id)

    def move(self, destination_id=None):
        """Executes the move method

        Args:
            destination_id (str):
                The destination_id to use in the method request          

        Returns:
            :class:`MailFolderMoveRequestBuilder<microsoft.msgraph.request.mail_folder_move.MailFolderMoveRequestBuilder>`:
                A MailFolderMoveRequestBuilder for the method
        """
        return MailFolderMoveRequestBuilder(self.append_to_request_url("move"), self._client, destination_id=destination_id)


