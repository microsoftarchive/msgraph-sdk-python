# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.physical_address import PhysicalAddress
from ..graph_object_base import GraphObjectBase


class Location(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def address(self):
        """
        Gets and sets the address
        
        Returns: 
            :class:`PhysicalAddress<microsoft.graph.model.physical_address.PhysicalAddress>`:
                The address
        """
        if "address" in self._prop_dict:
            if isinstance(self._prop_dict["address"], GraphObjectBase):
                return self._prop_dict["address"]
            else :
                self._prop_dict["address"] = PhysicalAddress(self._prop_dict["address"])
                return self._prop_dict["address"]

        return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val
