# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.user import User
import json
import asyncio

class UserRequest(RequestBase):
    """The type UserRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new UserRequest.

        Args:
            request_url (str): The url to perform the UserRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(UserRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified User."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified User."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified User.
        
        Returns:
            :class:`User<msgraph.model.user.User>`:
                The User.
        """
        self.method = "GET"
        entity = User(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified User in async.

        Yields:
            :class:`User<msgraph.model.user.User>`:
                The User.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, user):
        """Updates the specified User.
        
        Args:
            user (:class:`User<msgraph.model.user.User>`):
                The User to update.

        Returns:
            :class:`User<msgraph.model.user.User>`:
                The updated User.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = User(json.loads(self.send(user).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, user):
        """Updates the specified User in async
        
        Args:
            user (:class:`User<msgraph.model.user.User>`):
                The User to update.

        Yields:
            :class:`User<msgraph.model.user.User>`:
                The updated User.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    user)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.assigned_licenses and value.assigned_licenses._prop_dict:
                if "assigned_licenses@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["assigned_licenses@odata.nextLink"]
                    value.assigned_licenses._init_next_page_request(next_page_link, self._client, None)
            if value.assigned_plans and value.assigned_plans._prop_dict:
                if "assigned_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["assigned_plans@odata.nextLink"]
                    value.assigned_plans._init_next_page_request(next_page_link, self._client, None)
            if value.provisioned_plans and value.provisioned_plans._prop_dict:
                if "provisioned_plans@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["provisioned_plans@odata.nextLink"]
                    value.provisioned_plans._init_next_page_request(next_page_link, self._client, None)
            if value.owned_devices and value.owned_devices._prop_dict:
                if "owned_devices@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["owned_devices@odata.nextLink"]
                    value.owned_devices._init_next_page_request(next_page_link, self._client, None)
            if value.registered_devices and value.registered_devices._prop_dict:
                if "registered_devices@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["registered_devices@odata.nextLink"]
                    value.registered_devices._init_next_page_request(next_page_link, self._client, None)
            if value.direct_reports and value.direct_reports._prop_dict:
                if "direct_reports@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["direct_reports@odata.nextLink"]
                    value.direct_reports._init_next_page_request(next_page_link, self._client, None)
            if value.member_of and value.member_of._prop_dict:
                if "member_of@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["member_of@odata.nextLink"]
                    value.member_of._init_next_page_request(next_page_link, self._client, None)
            if value.created_objects and value.created_objects._prop_dict:
                if "created_objects@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["created_objects@odata.nextLink"]
                    value.created_objects._init_next_page_request(next_page_link, self._client, None)
            if value.owned_objects and value.owned_objects._prop_dict:
                if "owned_objects@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["owned_objects@odata.nextLink"]
                    value.owned_objects._init_next_page_request(next_page_link, self._client, None)
            if value.messages and value.messages._prop_dict:
                if "messages@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["messages@odata.nextLink"]
                    value.messages._init_next_page_request(next_page_link, self._client, None)
            if value.mail_folders and value.mail_folders._prop_dict:
                if "mail_folders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["mail_folders@odata.nextLink"]
                    value.mail_folders._init_next_page_request(next_page_link, self._client, None)
            if value.calendars and value.calendars._prop_dict:
                if "calendars@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendars@odata.nextLink"]
                    value.calendars._init_next_page_request(next_page_link, self._client, None)
            if value.calendar_groups and value.calendar_groups._prop_dict:
                if "calendar_groups@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendar_groups@odata.nextLink"]
                    value.calendar_groups._init_next_page_request(next_page_link, self._client, None)
            if value.calendar_view and value.calendar_view._prop_dict:
                if "calendar_view@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["calendar_view@odata.nextLink"]
                    value.calendar_view._init_next_page_request(next_page_link, self._client, None)
            if value.events and value.events._prop_dict:
                if "events@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["events@odata.nextLink"]
                    value.events._init_next_page_request(next_page_link, self._client, None)
            if value.contacts and value.contacts._prop_dict:
                if "contacts@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["contacts@odata.nextLink"]
                    value.contacts._init_next_page_request(next_page_link, self._client, None)
            if value.contact_folders and value.contact_folders._prop_dict:
                if "contact_folders@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["contact_folders@odata.nextLink"]
                    value.contact_folders._init_next_page_request(next_page_link, self._client, None)
