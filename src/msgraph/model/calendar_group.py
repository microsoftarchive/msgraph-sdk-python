# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .entity import Entity

class CalendarGroup(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def class_id(self):
        """
        Gets and sets the classId
        
        Returns:
            UUID:
                The classId
        """
        if "classId" in self._prop_dict:
            return self._prop_dict["classId"]
        else:
            return None

    @class_id.setter
    def class_id(self, val):
        self._prop_dict["classId"] = val

    @property
    def change_key(self):
        """
        Gets and sets the changeKey
        
        Returns:
            str:
                The changeKey
        """
        if "changeKey" in self._prop_dict:
            return self._prop_dict["changeKey"]
        else:
            return None

    @change_key.setter
    def change_key(self, val):
        self._prop_dict["changeKey"] = val

    @property
    def calendars(self):
        """Gets and sets the calendars
        
        Returns: 
            :class:`CalendarsCollectionPage<microsoft.graph.request.calendars_collection.CalendarsCollectionPage>`:
                The calendars
        """
        if "calendars" in self._prop_dict:
            return CalendarsCollectionPage(self._prop_dict["calendars"])
        else:
            return None

