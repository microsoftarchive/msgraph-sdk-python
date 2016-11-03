# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from enum import Enum

class RecurrencePatternType(Enum):
    """The Enum RecurrencePatternType."""
    #daily
    daily = "0"
    #weekly
    weekly = "1"
    #absolute Monthly
    absoluteMonthly = "2"
    #relative Monthly
    relativeMonthly = "3"
    #absolute Yearly
    absoluteYearly = "4"
    #relative Yearly
    relativeYearly = "5"
