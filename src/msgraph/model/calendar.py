# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.calendar_color import CalendarColor

from .entity import Entity

class Calendar(Entity):
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
    def color(self):
        """
        Gets and sets the color
        
        Returns: 
            :class:`CalendarColor<microsoft.graph.model.calendar_color.CalendarColor>`:
                The color
        """
        if "color" in self._prop_dict:
            if isinstance(self._prop_dict["color"], GraphObjectBase):
                return self._prop_dict["color"]
            else:
                self._prop_dict["color"] = CalendarColor(self._prop_dict["color"])
                return self._prop_dict["color"]

        return None

    @color.setter
    def color(self, val):
        self._prop_dict["color"] = val

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
    def events(self):
        """Gets and sets the events
        
        Returns: 
            :class:`EventsCollectionPage<microsoft.graph.request.events_collection.EventsCollectionPage>`:
                The events
        """
        if "events" in self._prop_dict:
            return EventsCollectionPage(self._prop_dict["events"])
        else:
            return None

    @property
    def calendar_view(self):
        """Gets and sets the calendarView
        
        Returns: 
            :class:`CalendarViewCollectionPage<microsoft.graph.request.calendar_view_collection.CalendarViewCollectionPage>`:
                The calendarView
        """
        if "calendarView" in self._prop_dict:
            return CalendarViewCollectionPage(self._prop_dict["calendarView"])
        else:
            return None

