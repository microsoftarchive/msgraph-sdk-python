# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .entity import Entity

class MailFolder(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def child_folder_count(self):
        """
        Gets and sets the childFolderCount
        
        Returns:
            int:
                The childFolderCount
        """
        if "childFolderCount" in self._prop_dict:
            return self._prop_dict["childFolderCount"]
        else:
            return None

    @child_folder_count.setter
    def child_folder_count(self, val):
        self._prop_dict["childFolderCount"] = val

    @property
    def unread_item_count(self):
        """
        Gets and sets the unreadItemCount
        
        Returns:
            int:
                The unreadItemCount
        """
        if "unreadItemCount" in self._prop_dict:
            return self._prop_dict["unreadItemCount"]
        else:
            return None

    @unread_item_count.setter
    def unread_item_count(self, val):
        self._prop_dict["unreadItemCount"] = val

    @property
    def total_item_count(self):
        """
        Gets and sets the totalItemCount
        
        Returns:
            int:
                The totalItemCount
        """
        if "totalItemCount" in self._prop_dict:
            return self._prop_dict["totalItemCount"]
        else:
            return None

    @total_item_count.setter
    def total_item_count(self, val):
        self._prop_dict["totalItemCount"] = val

    @property
    def messages(self):
        """Gets and sets the messages
        
        Returns: 
            :class:`MessagesCollectionPage<microsoft.graph.request.messages_collection.MessagesCollectionPage>`:
                The messages
        """
        if "messages" in self._prop_dict:
            return MessagesCollectionPage(self._prop_dict["messages"])
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

