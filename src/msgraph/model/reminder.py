# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.location import Location
from ..graph_object_base import GraphObjectBase


class Reminder(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def event_id(self):
        """Gets and sets the eventId
        
        Returns: 
            str:
                The eventId
        """
        if "eventId" in self._prop_dict:
            return self._prop_dict["eventId"]
        else:
            return None

    @event_id.setter
    def event_id(self, val):
        self._prop_dict["eventId"] = val

    @property
    def event_start_time(self):
        """
        Gets and sets the eventStartTime
        
        Returns: 
            :class:`DateTimeTimeZone<microsoft.graph.model.date_time_time_zone.DateTimeTimeZone>`:
                The eventStartTime
        """
        if "eventStartTime" in self._prop_dict:
            if isinstance(self._prop_dict["eventStartTime"], GraphObjectBase):
                return self._prop_dict["eventStartTime"]
            else :
                self._prop_dict["eventStartTime"] = DateTimeTimeZone(self._prop_dict["eventStartTime"])
                return self._prop_dict["eventStartTime"]

        return None

    @event_start_time.setter
    def event_start_time(self, val):
        self._prop_dict["eventStartTime"] = val
    @property
    def event_end_time(self):
        """
        Gets and sets the eventEndTime
        
        Returns: 
            :class:`DateTimeTimeZone<microsoft.graph.model.date_time_time_zone.DateTimeTimeZone>`:
                The eventEndTime
        """
        if "eventEndTime" in self._prop_dict:
            if isinstance(self._prop_dict["eventEndTime"], GraphObjectBase):
                return self._prop_dict["eventEndTime"]
            else :
                self._prop_dict["eventEndTime"] = DateTimeTimeZone(self._prop_dict["eventEndTime"])
                return self._prop_dict["eventEndTime"]

        return None

    @event_end_time.setter
    def event_end_time(self, val):
        self._prop_dict["eventEndTime"] = val
    @property
    def change_key(self):
        """Gets and sets the changeKey
        
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
    def event_subject(self):
        """Gets and sets the eventSubject
        
        Returns: 
            str:
                The eventSubject
        """
        if "eventSubject" in self._prop_dict:
            return self._prop_dict["eventSubject"]
        else:
            return None

    @event_subject.setter
    def event_subject(self, val):
        self._prop_dict["eventSubject"] = val

    @property
    def event_location(self):
        """
        Gets and sets the eventLocation
        
        Returns: 
            :class:`Location<microsoft.graph.model.location.Location>`:
                The eventLocation
        """
        if "eventLocation" in self._prop_dict:
            if isinstance(self._prop_dict["eventLocation"], GraphObjectBase):
                return self._prop_dict["eventLocation"]
            else :
                self._prop_dict["eventLocation"] = Location(self._prop_dict["eventLocation"])
                return self._prop_dict["eventLocation"]

        return None

    @event_location.setter
    def event_location(self, val):
        self._prop_dict["eventLocation"] = val
    @property
    def event_web_link(self):
        """Gets and sets the eventWebLink
        
        Returns: 
            str:
                The eventWebLink
        """
        if "eventWebLink" in self._prop_dict:
            return self._prop_dict["eventWebLink"]
        else:
            return None

    @event_web_link.setter
    def event_web_link(self, val):
        self._prop_dict["eventWebLink"] = val

    @property
    def reminder_fire_time(self):
        """
        Gets and sets the reminderFireTime
        
        Returns: 
            :class:`DateTimeTimeZone<microsoft.graph.model.date_time_time_zone.DateTimeTimeZone>`:
                The reminderFireTime
        """
        if "reminderFireTime" in self._prop_dict:
            if isinstance(self._prop_dict["reminderFireTime"], GraphObjectBase):
                return self._prop_dict["reminderFireTime"]
            else :
                self._prop_dict["reminderFireTime"] = DateTimeTimeZone(self._prop_dict["reminderFireTime"])
                return self._prop_dict["reminderFireTime"]

        return None

    @reminder_fire_time.setter
    def reminder_fire_time(self, val):
        self._prop_dict["reminderFireTime"] = val
