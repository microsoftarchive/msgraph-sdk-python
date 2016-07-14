# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime

from .entity import Entity

class Attachment(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def name(self):
        """
        Gets and sets the name
        
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
    def content_type(self):
        """
        Gets and sets the contentType
        
        Returns:
            str:
                The contentType
        """
        if "contentType" in self._prop_dict:
            return self._prop_dict["contentType"]
        else:
            return None

    @content_type.setter
    def content_type(self, val):
        self._prop_dict["contentType"] = val

    @property
    def size(self):
        """
        Gets and sets the size
        
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

    @property
    def is_inline(self):
        """
        Gets and sets the isInline
        
        Returns:
            bool:
                The isInline
        """
        if "isInline" in self._prop_dict:
            return self._prop_dict["isInline"]
        else:
            return None

    @is_inline.setter
    def is_inline(self, val):
        self._prop_dict["isInline"] = val

