# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.identity import Identity
from ..graph_object_base import GraphObjectBase


class SharingLink(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def application(self):
        """
        Gets and sets the application
        
        Returns: 
            :class:`Identity<microsoft.graph.model.identity.Identity>`:
                The application
        """
        if "application" in self._prop_dict:
            if isinstance(self._prop_dict["application"], GraphObjectBase):
                return self._prop_dict["application"]
            else :
                self._prop_dict["application"] = Identity(self._prop_dict["application"])
                return self._prop_dict["application"]

        return None

    @application.setter
    def application(self, val):
        self._prop_dict["application"] = val
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

    @property
    def web_url(self):
        """Gets and sets the webUrl
        
        Returns: 
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

