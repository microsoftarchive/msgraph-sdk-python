# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.mail_folder import MailFolder
import json

class MailFolderRequest(RequestBase):
    """The type MailFolderRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new MailFolderRequest.

        Args:
            request_url (str): The url to perform the MailFolderRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(MailFolderRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified MailFolder."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified MailFolder.
        
        Returns:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The MailFolder.
        """
        self.method = "GET"
        entity = MailFolder(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, mail_folder):
        """Updates the specified MailFolder.
        
        Args:
            mail_folder (:class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`):
                The MailFolder to update.

        Returns:
            :class:`MailFolder<microsoft.msgraph.model.mail_folder.MailFolder>`:
                The updated MailFolder.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = MailFolder(json.loads(self.send(mail_folder).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.messages and value.messages._prop_dict:
                if "messages@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["messages@odata.nextLink"]
                    value.messages._init_next_page_request(next_page_link, self._client, None)
            if value.child_folders and value.child_folders._prop_dict:
                if "child_folders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["child_folders@odata.nextLink"]
                    value.child_folders._init_next_page_request(next_page_link, self._client, None)
