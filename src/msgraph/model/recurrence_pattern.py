# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.recurrence_pattern_type import RecurrencePatternType
from ..model.day_of_week import DayOfWeek
from ..model.week_index import WeekIndex
from ..graph_object_base import GraphObjectBase


class RecurrencePattern(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`RecurrencePatternType<microsoft.graph.model.recurrence_pattern_type.RecurrencePatternType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], GraphObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = RecurrencePatternType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
    @property
    def interval(self):
        """Gets and sets the interval
        
        Returns: 
            int:
                The interval
        """
        if "interval" in self._prop_dict:
            return self._prop_dict["interval"]
        else:
            return None

    @interval.setter
    def interval(self, val):
        self._prop_dict["interval"] = val

    @property
    def month(self):
        """Gets and sets the month
        
        Returns: 
            int:
                The month
        """
        if "month" in self._prop_dict:
            return self._prop_dict["month"]
        else:
            return None

    @month.setter
    def month(self, val):
        self._prop_dict["month"] = val

    @property
    def day_of_month(self):
        """Gets and sets the dayOfMonth
        
        Returns: 
            int:
                The dayOfMonth
        """
        if "dayOfMonth" in self._prop_dict:
            return self._prop_dict["dayOfMonth"]
        else:
            return None

    @day_of_month.setter
    def day_of_month(self, val):
        self._prop_dict["dayOfMonth"] = val

    @property
    def days_of_week(self):
        """
        Gets and sets the daysOfWeek
        
        Returns: 
            :class:`DayOfWeek<microsoft.graph.model.day_of_week.DayOfWeek>`:
                The daysOfWeek
        """
        if "daysOfWeek" in self._prop_dict:
            if isinstance(self._prop_dict["daysOfWeek"], GraphObjectBase):
                return self._prop_dict["daysOfWeek"]
            else :
                self._prop_dict["daysOfWeek"] = DayOfWeek(self._prop_dict["daysOfWeek"])
                return self._prop_dict["daysOfWeek"]

        return None

    @days_of_week.setter
    def days_of_week(self, val):
        self._prop_dict["daysOfWeek"] = val
    @property
    def first_day_of_week(self):
        """
        Gets and sets the firstDayOfWeek
        
        Returns: 
            :class:`DayOfWeek<microsoft.graph.model.day_of_week.DayOfWeek>`:
                The firstDayOfWeek
        """
        if "firstDayOfWeek" in self._prop_dict:
            if isinstance(self._prop_dict["firstDayOfWeek"], GraphObjectBase):
                return self._prop_dict["firstDayOfWeek"]
            else :
                self._prop_dict["firstDayOfWeek"] = DayOfWeek(self._prop_dict["firstDayOfWeek"])
                return self._prop_dict["firstDayOfWeek"]

        return None

    @first_day_of_week.setter
    def first_day_of_week(self, val):
        self._prop_dict["firstDayOfWeek"] = val
    @property
    def index(self):
        """
        Gets and sets the index
        
        Returns: 
            :class:`WeekIndex<microsoft.graph.model.week_index.WeekIndex>`:
                The index
        """
        if "index" in self._prop_dict:
            if isinstance(self._prop_dict["index"], GraphObjectBase):
                return self._prop_dict["index"]
            else :
                self._prop_dict["index"] = WeekIndex(self._prop_dict["index"])
                return self._prop_dict["index"]

        return None

    @index.setter
    def index(self, val):
        self._prop_dict["index"] = val
