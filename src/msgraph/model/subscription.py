# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime

from .entity import Entity

class Subscription(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource(self):
        """
        Gets and sets the resource
        
        Returns:
            str:
                The resource
        """
        if "resource" in self._prop_dict:
            return self._prop_dict["resource"]
        else:
            return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val

    @property
    def change_type(self):
        """
        Gets and sets the changeType
        
        Returns:
            str:
                The changeType
        """
        if "changeType" in self._prop_dict:
            return self._prop_dict["changeType"]
        else:
            return None

    @change_type.setter
    def change_type(self, val):
        self._prop_dict["changeType"] = val

    @property
    def client_state(self):
        """
        Gets and sets the clientState
        
        Returns:
            str:
                The clientState
        """
        if "clientState" in self._prop_dict:
            return self._prop_dict["clientState"]
        else:
            return None

    @client_state.setter
    def client_state(self, val):
        self._prop_dict["clientState"] = val

    @property
    def notification_url(self):
        """
        Gets and sets the notificationUrl
        
        Returns:
            str:
                The notificationUrl
        """
        if "notificationUrl" in self._prop_dict:
            return self._prop_dict["notificationUrl"]
        else:
            return None

    @notification_url.setter
    def notification_url(self, val):
        self._prop_dict["notificationUrl"] = val

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

