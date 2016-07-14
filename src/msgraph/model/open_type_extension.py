# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .extension import Extension

class OpenTypeExtension(Extension):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def extension_name(self):
        """
        Gets and sets the extensionName
        
        Returns:
            str:
                The extensionName
        """
        if "extensionName" in self._prop_dict:
            return self._prop_dict["extensionName"]
        else:
            return None

    @extension_name.setter
    def extension_name(self, val):
        self._prop_dict["extensionName"] = val

