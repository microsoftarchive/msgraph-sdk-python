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
    singleInstance = 1
    #occurrence
    occurrence = 2
    #exception
    exception = 3
    #series Master
    seriesMaster = 4
