# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from enum import Enum

class ResponseType(Enum):
    """The Enum ResponseType."""
    #none
    none = 1
    #organizer
    organizer = 2
    #tentatively Accepted
    tentativelyAccepted = 3
    #accepted
    accepted = 4
    #declined
    declined = 5
    #not Responded
    notResponded = 6
