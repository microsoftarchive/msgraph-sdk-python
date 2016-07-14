# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.recurrence_pattern import RecurrencePattern
from ..model.recurrence_range import RecurrenceRange
from ..graph_object_base import GraphObjectBase


class PatternedRecurrence(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def pattern(self):
        """
        Gets and sets the pattern
        
        Returns: 
            :class:`RecurrencePattern<microsoft.graph.model.recurrence_pattern.RecurrencePattern>`:
                The pattern
        """
        if "pattern" in self._prop_dict:
            if isinstance(self._prop_dict["pattern"], GraphObjectBase):
                return self._prop_dict["pattern"]
            else :
                self._prop_dict["pattern"] = RecurrencePattern(self._prop_dict["pattern"])
                return self._prop_dict["pattern"]

        return None

    @pattern.setter
    def pattern(self, val):
        self._prop_dict["pattern"] = val
    @property
    def range(self):
        """
        Gets and sets the range
        
        Returns: 
            :class:`RecurrenceRange<microsoft.graph.model.recurrence_range.RecurrenceRange>`:
                The range
        """
        if "range" in self._prop_dict:
            if isinstance(self._prop_dict["range"], GraphObjectBase):
                return self._prop_dict["range"]
            else :
                self._prop_dict["range"] = RecurrenceRange(self._prop_dict["range"])
                return self._prop_dict["range"]

        return None

    @range.setter
    def range(self, val):
        self._prop_dict["range"] = val
