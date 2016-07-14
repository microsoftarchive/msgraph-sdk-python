# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class ProvisionedPlan(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

