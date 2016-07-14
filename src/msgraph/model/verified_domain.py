# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class VerifiedDomain(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def capabilities(self):
        """Gets and sets the capabilities
        
        Returns: 
            str:
                The capabilities
        """
        if "capabilities" in self._prop_dict:
            return self._prop_dict["capabilities"]
        else:
            return None

    @capabilities.setter
    def capabilities(self, val):
        self._prop_dict["capabilities"] = val

    @property
    def is_default(self):
        """Gets and sets the isDefault
        
        Returns: 
            bool:
                The isDefault
        """
        if "isDefault" in self._prop_dict:
            return self._prop_dict["isDefault"]
        else:
            return None

    @is_default.setter
    def is_default(self, val):
        self._prop_dict["isDefault"] = val

    @property
    def is_initial(self):
        """Gets and sets the isInitial
        
        Returns: 
            bool:
                The isInitial
        """
        if "isInitial" in self._prop_dict:
            return self._prop_dict["isInitial"]
        else:
            return None

    @is_initial.setter
    def is_initial(self, val):
        self._prop_dict["isInitial"] = val

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
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

