# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class ServicePlanInfo(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def service_plan_id(self):
        """Gets and sets the servicePlanId
        
        Returns: 
            UUID:
                The servicePlanId
        """
        if "servicePlanId" in self._prop_dict:
            return self._prop_dict["servicePlanId"]
        else:
            return None

    @service_plan_id.setter
    def service_plan_id(self, val):
        self._prop_dict["servicePlanId"] = val

    @property
    def service_plan_name(self):
        """Gets and sets the servicePlanName
        
        Returns: 
            str:
                The servicePlanName
        """
        if "servicePlanName" in self._prop_dict:
            return self._prop_dict["servicePlanName"]
        else:
            return None

    @service_plan_name.setter
    def service_plan_name(self, val):
        self._prop_dict["servicePlanName"] = val

    @property
    def provisioning_status(self):
        """Gets and sets the provisioningStatus
        
        Returns: 
            str:
                The provisioningStatus
        """
        if "provisioningStatus" in self._prop_dict:
            return self._prop_dict["provisioningStatus"]
        else:
            return None

    @provisioning_status.setter
    def provisioning_status(self, val):
        self._prop_dict["provisioningStatus"] = val

    @property
    def applies_to(self):
        """Gets and sets the appliesTo
        
        Returns: 
            str:
                The appliesTo
        """
        if "appliesTo" in self._prop_dict:
            return self._prop_dict["appliesTo"]
        else:
            return None

    @applies_to.setter
    def applies_to(self, val):
        self._prop_dict["appliesTo"] = val

