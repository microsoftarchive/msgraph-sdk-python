# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class AlternativeSecurityId(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            int:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def identity_provider(self):
        """Gets and sets the identityProvider
        
        Returns: 
            str:
                The identityProvider
        """
        if "identityProvider" in self._prop_dict:
            return self._prop_dict["identityProvider"]
        else:
            return None

    @identity_provider.setter
    def identity_provider(self, val):
        self._prop_dict["identityProvider"] = val

