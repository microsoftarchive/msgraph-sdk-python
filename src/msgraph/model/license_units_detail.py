# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class LicenseUnitsDetail(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enabled(self):
        """Gets and sets the enabled
        
        Returns: 
            int:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def suspended(self):
        """Gets and sets the suspended
        
        Returns: 
            int:
                The suspended
        """
        if "suspended" in self._prop_dict:
            return self._prop_dict["suspended"]
        else:
            return None

    @suspended.setter
    def suspended(self, val):
        self._prop_dict["suspended"] = val

    @property
    def warning(self):
        """Gets and sets the warning
        
        Returns: 
            int:
                The warning
        """
        if "warning" in self._prop_dict:
            return self._prop_dict["warning"]
        else:
            return None

    @warning.setter
    def warning(self, val):
        self._prop_dict["warning"] = val

