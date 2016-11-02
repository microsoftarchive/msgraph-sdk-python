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
    none = "0"
    #meeting Request
    meetingRequest = "1"
    #meeting Cancelled
    meetingCancelled = "2"
    #meeting Accepted
    meetingAccepted = "3"
    #meeting Tenatively Accepted
    meetingTenativelyAccepted = "4"
    #meeting Declined
    meetingDeclined = "5"
