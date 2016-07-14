# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class PhysicalAddress(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def street(self):
        """Gets and sets the street
        
        Returns: 
            str:
                The street
        """
        if "street" in self._prop_dict:
            return self._prop_dict["street"]
        else:
            return None

    @street.setter
    def street(self, val):
        self._prop_dict["street"] = val

    @property
    def city(self):
        """Gets and sets the city
        
        Returns: 
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def state(self):
        """Gets and sets the state
        
        Returns: 
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def country_or_region(self):
        """Gets and sets the countryOrRegion
        
        Returns: 
            str:
                The countryOrRegion
        """
        if "countryOrRegion" in self._prop_dict:
            return self._prop_dict["countryOrRegion"]
        else:
            return None

    @country_or_region.setter
    def country_or_region(self, val):
        self._prop_dict["countryOrRegion"] = val

    @property
    def postal_code(self):
        """Gets and sets the postalCode
        
        Returns: 
            str:
                The postalCode
        """
        if "postalCode" in self._prop_dict:
            return self._prop_dict["postalCode"]
        else:
            return None

    @postal_code.setter
    def postal_code(self, val):
        self._prop_dict["postalCode"] = val

