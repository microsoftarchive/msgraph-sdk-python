# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..graph_object_base import GraphObjectBase


class SharingInvitation(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def email(self):
        """Gets and sets the email
        
        Returns: 
            str:
                The email
        """
        if "email" in self._prop_dict:
            return self._prop_dict["email"]
        else:
            return None

    @email.setter
    def email(self, val):
        self._prop_dict["email"] = val

    @property
    def invited_by(self):
        """
        Gets and sets the invitedBy
        
        Returns: 
            :class:`IdentitySet<microsoft.graph.model.identity_set.IdentitySet>`:
                The invitedBy
        """
        if "invitedBy" in self._prop_dict:
            if isinstance(self._prop_dict["invitedBy"], GraphObjectBase):
                return self._prop_dict["invitedBy"]
            else :
                self._prop_dict["invitedBy"] = IdentitySet(self._prop_dict["invitedBy"])
                return self._prop_dict["invitedBy"]

        return None

    @invited_by.setter
    def invited_by(self, val):
        self._prop_dict["invitedBy"] = val
    @property
    def redeemed_by(self):
        """Gets and sets the redeemedBy
        
        Returns: 
            str:
                The redeemedBy
        """
        if "redeemedBy" in self._prop_dict:
            return self._prop_dict["redeemedBy"]
        else:
            return None

    @redeemed_by.setter
    def redeemed_by(self, val):
        self._prop_dict["redeemedBy"] = val

    @property
    def sign_in_required(self):
        """Gets and sets the signInRequired
        
        Returns: 
            bool:
                The signInRequired
        """
        if "signInRequired" in self._prop_dict:
            return self._prop_dict["signInRequired"]
        else:
            return None

    @sign_in_required.setter
    def sign_in_required(self, val):
        self._prop_dict["signInRequired"] = val

