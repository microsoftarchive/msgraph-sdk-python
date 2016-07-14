# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.recurrence_range_type import RecurrenceRangeType
from datetime import datetime
from ..graph_object_base import GraphObjectBase


class RecurrenceRange(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`RecurrenceRangeType<microsoft.graph.model.recurrence_range_type.RecurrenceRangeType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], GraphObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = RecurrenceRangeType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
    @property
    def start_date(self):
        """Gets and sets the startDate
        
        Returns: 
            datetime:
                The startDate
        """
        if "startDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date.setter
    def start_date(self, val):
        self._prop_dict["startDate"] = val.isoformat()+"Z"

    @property
    def end_date(self):
        """Gets and sets the endDate
        
        Returns: 
            datetime:
                The endDate
        """
        if "endDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date.setter
    def end_date(self, val):
        self._prop_dict["endDate"] = val.isoformat()+"Z"

    @property
    def recurrence_time_zone(self):
        """Gets and sets the recurrenceTimeZone
        
        Returns: 
            str:
                The recurrenceTimeZone
        """
        if "recurrenceTimeZone" in self._prop_dict:
            return self._prop_dict["recurrenceTimeZone"]
        else:
            return None

    @recurrence_time_zone.setter
    def recurrence_time_zone(self, val):
        self._prop_dict["recurrenceTimeZone"] = val

    @property
    def number_of_occurrences(self):
        """Gets and sets the numberOfOccurrences
        
        Returns: 
            int:
                The numberOfOccurrences
        """
        if "numberOfOccurrences" in self._prop_dict:
            return self._prop_dict["numberOfOccurrences"]
        else:
            return None

    @number_of_occurrences.setter
    def number_of_occurrences(self, val):
        self._prop_dict["numberOfOccurrences"] = val

