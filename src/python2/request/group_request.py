# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.group import Group
import json

class GroupRequest(RequestBase):
    """The type GroupRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new GroupRequest.

        Args:
            request_url (str): The url to perform the GroupRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(GroupRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Group."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Group.
        
        Returns:
            :class:`Group<microsoft.msgraph.model.group.Group>`:
                The Group.
        """
        self.method = "GET"
        entity = Group(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, group):
        """Updates the specified Group.
        
        Args:
            group (:class:`Group<microsoft.msgraph.model.group.Group>`):
                The Group to update.

        Returns:
            :class:`Group<microsoft.msgraph.model.group.Group>`:
                The updated Group.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Group(json.loads(self.send(group).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.members and value.members._prop_dict:
                if "members@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["members@odata.nextLink"]
                    value.members._init_next_page_request(next_page_link, self._client, None)
            if value.member_of and value.member_of._prop_dict:
                if "member_of@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["member_of@odata.nextLink"]
                    value.member_of._init_next_page_request(next_page_link, self._client, None)
            if value.owners and value.owners._prop_dict:
                if "owners@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["owners@odata.nextLink"]
                    value.owners._init_next_page_request(next_page_link, self._client, None)
            if value.threads and value.threads._prop_dict:
                if "threads@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["threads@odata.nextLink"]
                    value.threads._init_next_page_request(next_page_link, self._client, None)
            if value.calendar_view and value.calendar_view._prop_dict:
                if "calendar_view@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendar_view@odata.nextLink"]
                    value.calendar_view._init_next_page_request(next_page_link, self._client, None)
            if value.events and value.events._prop_dict:
                if "events@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["events@odata.nextLink"]
                    value.events._init_next_page_request(next_page_link, self._client, None)
            if value.conversations and value.conversations._prop_dict:
                if "conversations@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["conversations@odata.nextLink"]
                    value.conversations._init_next_page_request(next_page_link, self._client, None)
            if value.accepted_senders and value.accepted_senders._prop_dict:
                if "accepted_senders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["accepted_senders@odata.nextLink"]
                    value.accepted_senders._init_next_page_request(next_page_link, self._client, None)
            if value.rejected_senders and value.rejected_senders._prop_dict:
                if "rejected_senders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["rejected_senders@odata.nextLink"]
                    value.rejected_senders._init_next_page_request(next_page_link, self._client, None)
