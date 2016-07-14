# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .entity import Entity

class ContactFolder(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def parent_folder_id(self):
        """
        Gets and sets the parentFolderId
        
        Returns:
            str:
                The parentFolderId
        """
        if "parentFolderId" in self._prop_dict:
            return self._prop_dict["parentFolderId"]
        else:
            return None

    @parent_folder_id.setter
    def parent_folder_id(self, val):
        self._prop_dict["parentFolderId"] = val

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
    def contacts(self):
        """Gets and sets the contacts
        
        Returns: 
            :class:`ContactsCollectionPage<microsoft.graph.request.contacts_collection.ContactsCollectionPage>`:
                The contacts
        """
        if "contacts" in self._prop_dict:
            return ContactsCollectionPage(self._prop_dict["contacts"])
        else:
            return None

    @property
    def child_folders(self):
        """Gets and sets the childFolders
        
        Returns: 
            :class:`ChildFoldersCollectionPage<microsoft.graph.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The childFolders
        """
        if "childFolders" in self._prop_dict:
            return ChildFoldersCollectionPage(self._prop_dict["childFolders"])
        else:
            return None

