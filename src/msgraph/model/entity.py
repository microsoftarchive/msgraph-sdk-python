# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from ..graph_object_base import GraphObjectBase

class Entity(GraphObjectBase):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id_(self):
        """
        Gets and sets the id
        
        Returns:
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id_.setter
    def id_(self, val):
        self._prop_dict["id"] = val

