# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .directory_object import DirectoryObject

class DirectoryRole(DirectoryObject):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

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
    def role_template_id(self):
        """
        Gets and sets the roleTemplateId
        
        Returns:
            str:
                The roleTemplateId
        """
        if "roleTemplateId" in self._prop_dict:
            return self._prop_dict["roleTemplateId"]
        else:
            return None

    @role_template_id.setter
    def role_template_id(self, val):
        self._prop_dict["roleTemplateId"] = val

    @property
    def members(self):
        """Gets and sets the members
        
        Returns: 
            :class:`MembersCollectionPage<microsoft.graph.request.members_collection.MembersCollectionPage>`:
                The members
        """
        if "members" in self._prop_dict:
            return MembersCollectionPage(self._prop_dict["members"])
        else:
            return None

