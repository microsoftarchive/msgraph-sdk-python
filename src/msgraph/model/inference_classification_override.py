# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.inference_classification_type import InferenceClassificationType
from ..model.email_address import EmailAddress

from .entity import Entity

class InferenceClassificationOverride(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def classify_as(self):
        """
        Gets and sets the classifyAs
        
        Returns: 
            :class:`InferenceClassificationType<microsoft.graph.model.inference_classification_type.InferenceClassificationType>`:
                The classifyAs
        """
        if "classifyAs" in self._prop_dict:
            if isinstance(self._prop_dict["classifyAs"], GraphObjectBase):
                return self._prop_dict["classifyAs"]
            else:
                self._prop_dict["classifyAs"] = InferenceClassificationType(self._prop_dict["classifyAs"])
                return self._prop_dict["classifyAs"]

        return None

    @classify_as.setter
    def classify_as(self, val):
        self._prop_dict["classifyAs"] = val

    @property
    def sender_email_address(self):
        """
        Gets and sets the senderEmailAddress
        
        Returns: 
            :class:`EmailAddress<microsoft.graph.model.email_address.EmailAddress>`:
                The senderEmailAddress
        """
        if "senderEmailAddress" in self._prop_dict:
            if isinstance(self._prop_dict["senderEmailAddress"], GraphObjectBase):
                return self._prop_dict["senderEmailAddress"]
            else:
                self._prop_dict["senderEmailAddress"] = EmailAddress(self._prop_dict["senderEmailAddress"])
                return self._prop_dict["senderEmailAddress"]

        return None

    @sender_email_address.setter
    def sender_email_address(self, val):
        self._prop_dict["senderEmailAddress"] = val

