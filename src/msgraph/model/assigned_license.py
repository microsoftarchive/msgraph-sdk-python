# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class AssignedLicense(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def disabled_plans(self):
        """Gets and sets the disabledPlans
        
        Returns: 
            UUID:
                The disabledPlans
        """
        if "disabledPlans" in self._prop_dict:
            return self._prop_dict["disabledPlans"]
        else:
            return None

    @disabled_plans.setter
    def disabled_plans(self, val):
        self._prop_dict["disabledPlans"] = val

    @property
    def sku_id(self):
        """Gets and sets the skuId
        
        Returns: 
            UUID:
                The skuId
        """
        if "skuId" in self._prop_dict:
            return self._prop_dict["skuId"]
        else:
            return None

    @sku_id.setter
    def sku_id(self, val):
        self._prop_dict["skuId"] = val

