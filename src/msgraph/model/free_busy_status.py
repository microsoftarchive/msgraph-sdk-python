# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from enum import Enum

class FreeBusyStatus(Enum):
    """The Enum FreeBusyStatus."""
    #free
    free = "0"
    #tentative
    tentative = "1"
    #busy
    busy = "2"
    #oof
    oof = "3"
    #working Elsewhere
    workingElsewhere = "4"
    #unknown
    unknown = "5"
