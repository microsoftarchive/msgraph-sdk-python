# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.response_status import ResponseStatus
from ..model.attendee_type import AttendeeType
from ..graph_object_base import GraphObjectBase


class Attendee(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`ResponseStatus<microsoft.graph.model.response_status.ResponseStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], GraphObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = ResponseStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val
    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`AttendeeType<microsoft.graph.model.attendee_type.AttendeeType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], GraphObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = AttendeeType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
