# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .directory_object_request import DirectoryObjectRequest
from ..request_builder_base import RequestBuilderBase
from ..request.directory_object_check_member_groups import DirectoryObjectCheckMemberGroupsRequestBuilder
from ..request.directory_object_get_member_groups import DirectoryObjectGetMemberGroupsRequestBuilder
from ..request.directory_object_get_member_objects import DirectoryObjectGetMemberObjectsRequestBuilder
import asyncio



class DirectoryObjectRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DirectoryObjectRequestBuilder

        Args:
            request_url (str): The url to perform the DirectoryObjectRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(DirectoryObjectRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the DirectoryObjectRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DirectoryObjectRequest<msgraph.request.directory_object_request.DirectoryObjectRequest>`:
                The DirectoryObjectRequest
        """
        req = DirectoryObjectRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified DirectoryObject."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified DirectoryObject."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified DirectoryObject.
        
        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified DirectoryObject in async.

        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The DirectoryObject.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, directory_object):
        """Updates the specified DirectoryObject.
        
        Args:
            directory_object (:class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`):
                The DirectoryObject to update.

        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The updated DirectoryObject
        """
        return self.request().update(directory_object)

    @asyncio.coroutine
    def update_async(self, directory_object):
        """Updates the specified DirectoryObject in async
        
        Args:
            directory_object (:class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`):
                The DirectoryObject to update.

        Returns:
            :class:`DirectoryObject<msgraph.model.directory_object.DirectoryObject>`:
                The updated DirectoryObject.
        """
        entity = yield from self.request().update_async(directory_object)
        return entity
    @property
    def device(self):
        """The device for the DirectoryObjectRequestBuilder

        Returns:
            :class:`DeviceRequestBuilder<msgraph.request.device_request.DeviceRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return DeviceRequestBuilder(self.append_to_request_url("device"), self._client)

    @property
    def directory_role(self):
        """The directory_role for the DirectoryObjectRequestBuilder

        Returns:
            :class:`DirectoryRoleRequestBuilder<msgraph.request.directory_role_request.DirectoryRoleRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return DirectoryRoleRequestBuilder(self.append_to_request_url("directoryRole"), self._client)

    @property
    def directory_role_template(self):
        """The directory_role_template for the DirectoryObjectRequestBuilder

        Returns:
            :class:`DirectoryRoleTemplateRequestBuilder<msgraph.request.directory_role_template_request.DirectoryRoleTemplateRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return DirectoryRoleTemplateRequestBuilder(self.append_to_request_url("directoryRoleTemplate"), self._client)

    @property
    def group(self):
        """The group for the DirectoryObjectRequestBuilder

        Returns:
            :class:`GroupRequestBuilder<msgraph.request.group_request.GroupRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return GroupRequestBuilder(self.append_to_request_url("group"), self._client)

    @property
    def organization(self):
        """The organization for the DirectoryObjectRequestBuilder

        Returns:
            :class:`OrganizationRequestBuilder<msgraph.request.organization_request.OrganizationRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return OrganizationRequestBuilder(self.append_to_request_url("organization"), self._client)

    @property
    def user(self):
        """The user for the DirectoryObjectRequestBuilder

        Returns:
            :class:`UserRequestBuilder<msgraph.request.user_request.UserRequestBuilder>`:
                A request builder created from the DirectoryObjectRequestBuilder
        """
        return UserRequestBuilder(self.append_to_request_url("user"), self._client)

    def check_member_groups(self, group_ids):
        """Executes the checkMemberGroups method

        Args:
            group_ids (str):
                The group_ids to use in the method request          

        Returns:
            :class:`DirectoryObjectCheckMemberGroupsRequestBuilder<msgraph.request.directory_object_check_member_groups.DirectoryObjectCheckMemberGroupsRequestBuilder>`:
                A DirectoryObjectCheckMemberGroupsRequestBuilder for the method
        """
        return DirectoryObjectCheckMemberGroupsRequestBuilder(self.append_to_request_url("checkMemberGroups"), self._client, group_ids)

    def get_member_groups(self, security_enabled_only=None):
        """Executes the getMemberGroups method

        Args:
            security_enabled_only (bool):
                The security_enabled_only to use in the method request          

        Returns:
            :class:`DirectoryObjectGetMemberGroupsRequestBuilder<msgraph.request.directory_object_get_member_groups.DirectoryObjectGetMemberGroupsRequestBuilder>`:
                A DirectoryObjectGetMemberGroupsRequestBuilder for the method
        """
        return DirectoryObjectGetMemberGroupsRequestBuilder(self.append_to_request_url("getMemberGroups"), self._client, security_enabled_only=security_enabled_only)

    def get_member_objects(self, security_enabled_only=None):
        """Executes the getMemberObjects method

        Args:
            security_enabled_only (bool):
                The security_enabled_only to use in the method request          

        Returns:
            :class:`DirectoryObjectGetMemberObjectsRequestBuilder<msgraph.request.directory_object_get_member_objects.DirectoryObjectGetMemberObjectsRequestBuilder>`:
                A DirectoryObjectGetMemberObjectsRequestBuilder for the method
        """
        return DirectoryObjectGetMemberObjectsRequestBuilder(self.append_to_request_url("getMemberObjects"), self._client, security_enabled_only=security_enabled_only)


