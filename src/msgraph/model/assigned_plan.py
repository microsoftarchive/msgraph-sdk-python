# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime
from ..graph_object_base import GraphObjectBase


class AssignedPlan(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def assigned_date_time(self):
        """Gets and sets the assignedDateTime
        
        Returns: 
            datetime:
                The assignedDateTime
        """
        if "assignedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["assignedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @assigned_date_time.setter
    def assigned_date_time(self, val):
        self._prop_dict["assignedDateTime"] = val.isoformat()+"Z"

    @property
    def capability_status(self):
        """Gets and sets the capabilityStatus
        
        Returns: 
            str:
                The capabilityStatus
        """
        if "capabilityStatus" in self._prop_dict:
            return self._prop_dict["capabilityStatus"]
        else:
            return None

    @capability_status.setter
    def capability_status(self, val):
        self._prop_dict["capabilityStatus"] = val

    @property
    def service(self):
        """Gets and sets the service
        
        Returns: 
            str:
                The service
        """
        if "service" in self._prop_dict:
            return self._prop_dict["service"]
        else:
            return None

    @service.setter
    def service(self, val):
        self._prop_dict["service"] = val

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

