# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.license_units_detail import LicenseUnitsDetail

from .entity import Entity

class SubscribedSku(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def capability_status(self):
        """
        Gets and sets the capabilityStatus
        
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
    def consumed_units(self):
        """
        Gets and sets the consumedUnits
        
        Returns:
            int:
                The consumedUnits
        """
        if "consumedUnits" in self._prop_dict:
            return self._prop_dict["consumedUnits"]
        else:
            return None

    @consumed_units.setter
    def consumed_units(self, val):
        self._prop_dict["consumedUnits"] = val

    @property
    def prepaid_units(self):
        """
        Gets and sets the prepaidUnits
        
        Returns: 
            :class:`LicenseUnitsDetail<microsoft.graph.model.license_units_detail.LicenseUnitsDetail>`:
                The prepaidUnits
        """
        if "prepaidUnits" in self._prop_dict:
            if isinstance(self._prop_dict["prepaidUnits"], GraphObjectBase):
                return self._prop_dict["prepaidUnits"]
            else:
                self._prop_dict["prepaidUnits"] = LicenseUnitsDetail(self._prop_dict["prepaidUnits"])
                return self._prop_dict["prepaidUnits"]

        return None

    @prepaid_units.setter
    def prepaid_units(self, val):
        self._prop_dict["prepaidUnits"] = val

    @property
    def service_plans(self):
        """Gets and sets the servicePlans
        
        Returns: 
            :class:`ServicePlansCollectionPage<microsoft.graph.request.service_plans_collection.ServicePlansCollectionPage>`:
                The servicePlans
        """
        if "servicePlans" in self._prop_dict:
            return ServicePlansCollectionPage(self._prop_dict["servicePlans"])
        else:
            return None

    @property
    def sku_id(self):
        """
        Gets and sets the skuId
        
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

    @property
    def sku_part_number(self):
        """
        Gets and sets the skuPartNumber
        
        Returns:
            str:
                The skuPartNumber
        """
        if "skuPartNumber" in self._prop_dict:
            return self._prop_dict["skuPartNumber"]
        else:
            return None

    @sku_part_number.setter
    def sku_part_number(self, val):
        self._prop_dict["skuPartNumber"] = val

    @property
    def applies_to(self):
        """
        Gets and sets the appliesTo
        
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

