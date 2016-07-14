# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.file import File
from ..model.file_system_info import FileSystemInfo
from ..model.folder import Folder
from ..model.item_reference import ItemReference
from ..graph_object_base import GraphObjectBase


class RemoteItem(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def file(self):
        """
        Gets and sets the file
        
        Returns: 
            :class:`File<microsoft.graph.model.file.File>`:
                The file
        """
        if "file" in self._prop_dict:
            if isinstance(self._prop_dict["file"], GraphObjectBase):
                return self._prop_dict["file"]
            else :
                self._prop_dict["file"] = File(self._prop_dict["file"])
                return self._prop_dict["file"]

        return None

    @file.setter
    def file(self, val):
        self._prop_dict["file"] = val
    @property
    def file_system_info(self):
        """
        Gets and sets the fileSystemInfo
        
        Returns: 
            :class:`FileSystemInfo<microsoft.graph.model.file_system_info.FileSystemInfo>`:
                The fileSystemInfo
        """
        if "fileSystemInfo" in self._prop_dict:
            if isinstance(self._prop_dict["fileSystemInfo"], GraphObjectBase):
                return self._prop_dict["fileSystemInfo"]
            else :
                self._prop_dict["fileSystemInfo"] = FileSystemInfo(self._prop_dict["fileSystemInfo"])
                return self._prop_dict["fileSystemInfo"]

        return None

    @file_system_info.setter
    def file_system_info(self, val):
        self._prop_dict["fileSystemInfo"] = val
    @property
    def folder(self):
        """
        Gets and sets the folder
        
        Returns: 
            :class:`Folder<microsoft.graph.model.folder.Folder>`:
                The folder
        """
        if "folder" in self._prop_dict:
            if isinstance(self._prop_dict["folder"], GraphObjectBase):
                return self._prop_dict["folder"]
            else :
                self._prop_dict["folder"] = Folder(self._prop_dict["folder"])
                return self._prop_dict["folder"]

        return None

    @folder.setter
    def folder(self, val):
        self._prop_dict["folder"] = val
    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def parent_reference(self):
        """
        Gets and sets the parentReference
        
        Returns: 
            :class:`ItemReference<microsoft.graph.model.item_reference.ItemReference>`:
                The parentReference
        """
        if "parentReference" in self._prop_dict:
            if isinstance(self._prop_dict["parentReference"], GraphObjectBase):
                return self._prop_dict["parentReference"]
            else :
                self._prop_dict["parentReference"] = ItemReference(self._prop_dict["parentReference"])
                return self._prop_dict["parentReference"]

        return None

    @parent_reference.setter
    def parent_reference(self, val):
        self._prop_dict["parentReference"] = val
    @property
    def size(self):
        """Gets and sets the size
        
        Returns: 
            int:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

