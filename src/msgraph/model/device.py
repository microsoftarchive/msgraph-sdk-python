# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime

from .directory_object import DirectoryObject

class Device(DirectoryObject):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_enabled(self):
        """
        Gets and sets the accountEnabled
        
        Returns:
            bool:
                The accountEnabled
        """
        if "accountEnabled" in self._prop_dict:
            return self._prop_dict["accountEnabled"]
        else:
            return None

    @account_enabled.setter
    def account_enabled(self, val):
        self._prop_dict["accountEnabled"] = val

    @property
    def alternative_security_ids(self):
        """Gets and sets the alternativeSecurityIds
        
        Returns: 
            :class:`AlternativeSecurityIdsCollectionPage<microsoft.graph.request.alternative_security_ids_collection.AlternativeSecurityIdsCollectionPage>`:
                The alternativeSecurityIds
        """
        if "alternativeSecurityIds" in self._prop_dict:
            return AlternativeSecurityIdsCollectionPage(self._prop_dict["alternativeSecurityIds"])
        else:
            return None

    @property
    def approximate_last_sign_in_date_time(self):
        """
        Gets and sets the approximateLastSignInDateTime
        
        Returns:
            datetime:
                The approximateLastSignInDateTime
        """
        if "approximateLastSignInDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["approximateLastSignInDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @approximate_last_sign_in_date_time.setter
    def approximate_last_sign_in_date_time(self, val):
        self._prop_dict["approximateLastSignInDateTime"] = val.isoformat()+"Z"

    @property
    def device_id(self):
        """
        Gets and sets the deviceId
        
        Returns:
            str:
                The deviceId
        """
        if "deviceId" in self._prop_dict:
            return self._prop_dict["deviceId"]
        else:
            return None

    @device_id.setter
    def device_id(self, val):
        self._prop_dict["deviceId"] = val

    @property
    def device_metadata(self):
        """
        Gets and sets the deviceMetadata
        
        Returns:
            str:
                The deviceMetadata
        """
        if "deviceMetadata" in self._prop_dict:
            return self._prop_dict["deviceMetadata"]
        else:
            return None

    @device_metadata.setter
    def device_metadata(self, val):
        self._prop_dict["deviceMetadata"] = val

    @property
    def device_version(self):
        """
        Gets and sets the deviceVersion
        
        Returns:
            int:
                The deviceVersion
        """
        if "deviceVersion" in self._prop_dict:
            return self._prop_dict["deviceVersion"]
        else:
            return None

    @device_version.setter
    def device_version(self, val):
        self._prop_dict["deviceVersion"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def is_compliant(self):
        """
        Gets and sets the isCompliant
        
        Returns:
            bool:
                The isCompliant
        """
        if "isCompliant" in self._prop_dict:
            return self._prop_dict["isCompliant"]
        else:
            return None

    @is_compliant.setter
    def is_compliant(self, val):
        self._prop_dict["isCompliant"] = val

    @property
    def is_managed(self):
        """
        Gets and sets the isManaged
        
        Returns:
            bool:
                The isManaged
        """
        if "isManaged" in self._prop_dict:
            return self._prop_dict["isManaged"]
        else:
            return None

    @is_managed.setter
    def is_managed(self, val):
        self._prop_dict["isManaged"] = val

    @property
    def on_premises_last_sync_date_time(self):
        """
        Gets and sets the onPremisesLastSyncDateTime
        
        Returns:
            datetime:
                The onPremisesLastSyncDateTime
        """
        if "onPremisesLastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["onPremisesLastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self, val):
        self._prop_dict["onPremisesLastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def on_premises_sync_enabled(self):
        """
        Gets and sets the onPremisesSyncEnabled
        
        Returns:
            bool:
                The onPremisesSyncEnabled
        """
        if "onPremisesSyncEnabled" in self._prop_dict:
            return self._prop_dict["onPremisesSyncEnabled"]
        else:
            return None

    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self, val):
        self._prop_dict["onPremisesSyncEnabled"] = val

    @property
    def operating_system(self):
        """
        Gets and sets the operatingSystem
        
        Returns:
            str:
                The operatingSystem
        """
        if "operatingSystem" in self._prop_dict:
            return self._prop_dict["operatingSystem"]
        else:
            return None

    @operating_system.setter
    def operating_system(self, val):
        self._prop_dict["operatingSystem"] = val

    @property
    def operating_system_version(self):
        """
        Gets and sets the operatingSystemVersion
        
        Returns:
            str:
                The operatingSystemVersion
        """
        if "operatingSystemVersion" in self._prop_dict:
            return self._prop_dict["operatingSystemVersion"]
        else:
            return None

    @operating_system_version.setter
    def operating_system_version(self, val):
        self._prop_dict["operatingSystemVersion"] = val

    @property
    def physical_ids(self):
        """
        Gets and sets the physicalIds
        
        Returns:
            str:
                The physicalIds
        """
        if "physicalIds" in self._prop_dict:
            return self._prop_dict["physicalIds"]
        else:
            return None

    @physical_ids.setter
    def physical_ids(self, val):
        self._prop_dict["physicalIds"] = val

    @property
    def trust_type(self):
        """
        Gets and sets the trustType
        
        Returns:
            str:
                The trustType
        """
        if "trustType" in self._prop_dict:
            return self._prop_dict["trustType"]
        else:
            return None

    @trust_type.setter
    def trust_type(self, val):
        self._prop_dict["trustType"] = val

    @property
    def registered_owners(self):
        """Gets and sets the registeredOwners
        
        Returns: 
            :class:`RegisteredOwnersCollectionPage<microsoft.graph.request.registered_owners_collection.RegisteredOwnersCollectionPage>`:
                The registeredOwners
        """
        if "registeredOwners" in self._prop_dict:
            return RegisteredOwnersCollectionPage(self._prop_dict["registeredOwners"])
        else:
            return None

    @property
    def registered_users(self):
        """Gets and sets the registeredUsers
        
        Returns: 
            :class:`RegisteredUsersCollectionPage<microsoft.graph.request.registered_users_collection.RegisteredUsersCollectionPage>`:
                The registeredUsers
        """
        if "registeredUsers" in self._prop_dict:
            return RegisteredUsersCollectionPage(self._prop_dict["registeredUsers"])
        else:
            return None

