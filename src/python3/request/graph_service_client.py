# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..request.directory_objects_collection import DirectoryObjectsCollectionRequestBuilder
from ..request.devices_collection import DevicesCollectionRequestBuilder
from ..request.groups_collection import GroupsCollectionRequestBuilder
from ..request.directory_roles_collection import DirectoryRolesCollectionRequestBuilder
from ..request.directory_role_templates_collection import DirectoryRoleTemplatesCollectionRequestBuilder
from ..request.organization_collection import OrganizationCollectionRequestBuilder
from ..request.subscribed_skus_collection import SubscribedSkusCollectionRequestBuilder
from ..request.users_collection import UsersCollectionRequestBuilder
from ..request.drives_collection import DrivesCollectionRequestBuilder
from ..request.subscriptions_collection import SubscriptionsCollectionRequestBuilder
from ..request.user_request_builder import UserRequestBuilder
from ..request.drive_request_builder import DriveRequestBuilder
import sys


class GraphServiceClient(object):

    def __init__(self, base_url, auth_provider, http_provider, loop=None):
        """Initialize the :class:`GraphClient` to be
            used for all Graph API interactions
        
        Args:
            base_url (str): The Graph base url to use for API interactions
            auth_provider(:class:`AuthProviderBase<msgraph.auth_provider_base.AuthProviderBase>`):
                The authentication provider used by the client to auth
                with Graph services
            http_provider(:class:`HttpProviderBase<msgraph.http_provider_base.HttpProviderBase>`):
                The HTTP provider used by the client to send all 
                requests to Graph
            loop (BaseEventLoop): Default to None, the AsyncIO loop 
                to use for all async requests
        """
        self.base_url = base_url
        self.auth_provider = auth_provider
        self.http_provider = http_provider

        if sys.version_info >= (3, 5, 0):
            import asyncio
            self._loop = loop if loop else asyncio.new_event_loop()

    @property
    def auth_provider(self):
        """Gets and sets the client auth provider
        
        Returns:
            :class:`AuthProviderBase<msgraph.auth_provider_base.AuthProviderBase>`: 
            The authentication provider
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, value):
        self._auth_provider = value

    @property
    def http_provider(self):
        """Gets and sets the client HTTP provider

        Returns: 
            :class:`HttpProviderBase<msgraph.http_provider_base.HttpProviderBase>`: 
                The HTTP provider
        """
        return self._http_provider

    @http_provider.setter
    def http_provider(self, value):
        self._http_provider = value

    @property
    def base_url(self):
        """Gets and sets the base URL used by the client to make requests

        Returns:
            str: The base URL
        """
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def directory_objects(self):
        """Get the DirectoryObjectsCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DirectoryObjectsCollectionRequestBuilder<msgraph.request.directory_objects_collection.DirectoryObjectsCollectionRequestBuilder>`:
                The DirectoryObjectsCollectionRequestBuilder to return
        """
        return DirectoryObjectsCollectionRequestBuilder(self.base_url + "directoryObjects", self)

    @property
    def devices(self):
        """Get the DevicesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DevicesCollectionRequestBuilder<msgraph.request.devices_collection.DevicesCollectionRequestBuilder>`:
                The DevicesCollectionRequestBuilder to return
        """
        return DevicesCollectionRequestBuilder(self.base_url + "devices", self)

    @property
    def groups(self):
        """Get the GroupsCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`GroupsCollectionRequestBuilder<msgraph.request.groups_collection.GroupsCollectionRequestBuilder>`:
                The GroupsCollectionRequestBuilder to return
        """
        return GroupsCollectionRequestBuilder(self.base_url + "groups", self)

    @property
    def directory_roles(self):
        """Get the DirectoryRolesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DirectoryRolesCollectionRequestBuilder<msgraph.request.directory_roles_collection.DirectoryRolesCollectionRequestBuilder>`:
                The DirectoryRolesCollectionRequestBuilder to return
        """
        return DirectoryRolesCollectionRequestBuilder(self.base_url + "directoryRoles", self)

    @property
    def directory_role_templates(self):
        """Get the DirectoryRoleTemplatesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DirectoryRoleTemplatesCollectionRequestBuilder<msgraph.request.directory_role_templates_collection.DirectoryRoleTemplatesCollectionRequestBuilder>`:
                The DirectoryRoleTemplatesCollectionRequestBuilder to return
        """
        return DirectoryRoleTemplatesCollectionRequestBuilder(self.base_url + "directoryRoleTemplates", self)

    @property
    def organization(self):
        """Get the OrganizationCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`OrganizationCollectionRequestBuilder<msgraph.request.organization_collection.OrganizationCollectionRequestBuilder>`:
                The OrganizationCollectionRequestBuilder to return
        """
        return OrganizationCollectionRequestBuilder(self.base_url + "organization", self)

    @property
    def subscribed_skus(self):
        """Get the SubscribedSkusCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`SubscribedSkusCollectionRequestBuilder<msgraph.request.subscribed_skus_collection.SubscribedSkusCollectionRequestBuilder>`:
                The SubscribedSkusCollectionRequestBuilder to return
        """
        return SubscribedSkusCollectionRequestBuilder(self.base_url + "subscribedSkus", self)

    @property
    def users(self):
        """Get the UsersCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`UsersCollectionRequestBuilder<msgraph.request.users_collection.UsersCollectionRequestBuilder>`:
                The UsersCollectionRequestBuilder to return
        """
        return UsersCollectionRequestBuilder(self.base_url + "users", self)

    @property
    def drives(self):
        """Get the DrivesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DrivesCollectionRequestBuilder<msgraph.request.drives_collection.DrivesCollectionRequestBuilder>`:
                The DrivesCollectionRequestBuilder to return
        """
        return DrivesCollectionRequestBuilder(self.base_url + "drives", self)

    @property
    def subscriptions(self):
        """Get the SubscriptionsCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`SubscriptionsCollectionRequestBuilder<msgraph.request.subscriptions_collection.SubscriptionsCollectionRequestBuilder>`:
                The SubscriptionsCollectionRequestBuilder to return
        """
        return SubscriptionsCollectionRequestBuilder(self.base_url + "subscriptions", self)
    
    @property
    def me(self):
        """Get the UserRequestBuilder for constructing requests

        Returns: 
            :class:`UserRequestBuilder<msgraph.request.user_request_builder.UserRequestBuilder>`:
                The UserRequestBuilder to return    
        """
        return UserRequestBuilder(self.base_url + "me", self)
    
    @property
    def drive(self):
        """Get the DriveRequestBuilder for constructing requests

        Returns: 
            :class:`DriveRequestBuilder<msgraph.request.drive_request_builder.DriveRequestBuilder>`:
                The DriveRequestBuilder to return    
        """
        return DriveRequestBuilder(self.base_url + "drive", self)
