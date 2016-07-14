# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.body_type import BodyType
from ..graph_object_base import GraphObjectBase


class ItemBody(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def content_type(self):
        """
        Gets and sets the contentType
        
        Returns: 
            :class:`BodyType<microsoft.graph.model.body_type.BodyType>`:
                The contentType
        """
        if "contentType" in self._prop_dict:
            if isinstance(self._prop_dict["contentType"], GraphObjectBase):
                return self._prop_dict["contentType"]
            else :
                self._prop_dict["contentType"] = BodyType(self._prop_dict["contentType"])
                return self._prop_dict["contentType"]

        return None

    @content_type.setter
    def content_type(self, val):
        self._prop_dict["contentType"] = val
    @property
    def content(self):
        """Gets and sets the content
        
        Returns: 
            str:
                The content
        """
        if "content" in self._prop_dict:
            return self._prop_dict["content"]
        else:
            return None

    @content.setter
    def content(self, val):
        self._prop_dict["content"] = val

