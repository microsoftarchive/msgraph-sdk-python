# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..graph_object_base import GraphObjectBase


class Shared(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
            else :
                self._prop_dict["owner"] = IdentitySet(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val
    @property
    def scope(self):
        """Gets and sets the scope
        
        Returns: 
            str:
                The scope
        """
        if "scope" in self._prop_dict:
            return self._prop_dict["scope"]
        else:
            return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val

