# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from enum import Enum

class MeetingMessageType(Enum):
    """The Enum MeetingMessageType."""
    #none
    none = 1
    #meeting Request
    meetingRequest = 2
    #meeting Cancelled
    meetingCancelled = 3
    #meeting Accepted
    meetingAccepted = 4
    #meeting Tenatively Accepted
    meetingTenativelyAccepted = 5
    #meeting Declined
    meetingDeclined = 6
