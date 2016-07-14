# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.meeting_message_type import MeetingMessageType

from .message import Message

class EventMessage(Message):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def meeting_message_type(self):
        """
        Gets and sets the meetingMessageType
        
        Returns: 
            :class:`MeetingMessageType<microsoft.graph.model.meeting_message_type.MeetingMessageType>`:
                The meetingMessageType
        """
        if "meetingMessageType" in self._prop_dict:
            if isinstance(self._prop_dict["meetingMessageType"], GraphObjectBase):
                return self._prop_dict["meetingMessageType"]
            else:
                self._prop_dict["meetingMessageType"] = MeetingMessageType(self._prop_dict["meetingMessageType"])
                return self._prop_dict["meetingMessageType"]

        return None

    @meeting_message_type.setter
    def meeting_message_type(self, val):
        self._prop_dict["meetingMessageType"] = val

    @property
    def event(self):
        """
        Gets and sets the event
        
        Returns: 
            :class:`Event<microsoft.graph.model.event.Event>`:
                The event
        """
        if "event" in self._prop_dict:
            if isinstance(self._prop_dict["event"], GraphObjectBase):
                return self._prop_dict["event"]
            else:
                self._prop_dict["event"] = Event(self._prop_dict["event"])
                return self._prop_dict["event"]

        return None

    @event.setter
    def event(self, val):
        self._prop_dict["event"] = val

