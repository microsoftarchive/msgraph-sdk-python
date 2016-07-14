# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class DateTimeTimeZone(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def date_time(self):
        """Gets and sets the dateTime
        
        Returns: 
            str:
                The dateTime
        """
        if "dateTime" in self._prop_dict:
            return self._prop_dict["dateTime"]
        else:
            return None

    @date_time.setter
    def date_time(self, val):
        self._prop_dict["dateTime"] = val

    @property
    def time_zone(self):
        """Gets and sets the timeZone
        
        Returns: 
            str:
                The timeZone
        """
        if "timeZone" in self._prop_dict:
            return self._prop_dict["timeZone"]
        else:
            return None

    @time_zone.setter
    def time_zone(self, val):
        self._prop_dict["timeZone"] = val

