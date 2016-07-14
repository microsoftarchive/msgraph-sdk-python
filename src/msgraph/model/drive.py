# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.quota import Quota

from .entity import Entity

class Drive(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def drive_type(self):
        """
        Gets and sets the driveType
        
        Returns:
            str:
                The driveType
        """
        if "driveType" in self._prop_dict:
            return self._prop_dict["driveType"]
        else:
            return None

    @drive_type.setter
    def drive_type(self, val):
        self._prop_dict["driveType"] = val

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns: 
            :class:`IdentitySet<microsoft.graph.model.identity_set.IdentitySet>`:
                The owner
        """
        if "owner" in self._prop_dict:
            if isinstance(self._prop_dict["owner"], GraphObjectBase):
                return self._prop_dict["owner"]
            else:
                self._prop_dict["owner"] = IdentitySet(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def quota(self):
        """
        Gets and sets the quota
        
        Returns: 
            :class:`Quota<microsoft.graph.model.quota.Quota>`:
                The quota
        """
        if "quota" in self._prop_dict:
            if isinstance(self._prop_dict["quota"], GraphObjectBase):
                return self._prop_dict["quota"]
            else:
                self._prop_dict["quota"] = Quota(self._prop_dict["quota"])
                return self._prop_dict["quota"]

        return None

    @quota.setter
    def quota(self, val):
        self._prop_dict["quota"] = val

    @property
    def items(self):
        """Gets and sets the items
        
        Returns: 
            :class:`ItemsCollectionPage<microsoft.graph.request.items_collection.ItemsCollectionPage>`:
                The items
        """
        if "items" in self._prop_dict:
            return ItemsCollectionPage(self._prop_dict["items"])
        else:
            return None

    @property
    def special(self):
        """Gets and sets the special
        
        Returns: 
            :class:`SpecialCollectionPage<microsoft.graph.request.special_collection.SpecialCollectionPage>`:
                The special
        """
        if "special" in self._prop_dict:
            return SpecialCollectionPage(self._prop_dict["special"])
        else:
            return None

    @property
    def root(self):
        """
        Gets and sets the root
        
        Returns: 
            :class:`DriveItem<microsoft.graph.model.drive_item.DriveItem>`:
                The root
        """
        if "root" in self._prop_dict:
            if isinstance(self._prop_dict["root"], GraphObjectBase):
                return self._prop_dict["root"]
            else:
                self._prop_dict["root"] = DriveItem(self._prop_dict["root"])
                return self._prop_dict["root"]

        return None

    @root.setter
    def root(self, val):
        self._prop_dict["root"] = val

