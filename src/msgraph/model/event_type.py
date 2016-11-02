# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from enum import Enum

class EventType(Enum):
    """The Enum EventType."""
    #single Instance
    singleInstance = "0"
    #occurrence
    occurrence = "1"
    #exception
    exception = "2"
    #series Master
    seriesMaster = "3"
