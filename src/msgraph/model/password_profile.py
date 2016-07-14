# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class PasswordProfile(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def password(self):
        """Gets and sets the password
        
        Returns: 
            str:
                The password
        """
        if "password" in self._prop_dict:
            return self._prop_dict["password"]
        else:
            return None

    @password.setter
    def password(self, val):
        self._prop_dict["password"] = val

    @property
    def force_change_password_next_sign_in(self):
        """Gets and sets the forceChangePasswordNextSignIn
        
        Returns: 
            bool:
                The forceChangePasswordNextSignIn
        """
        if "forceChangePasswordNextSignIn" in self._prop_dict:
            return self._prop_dict["forceChangePasswordNextSignIn"]
        else:
            return None

    @force_change_password_next_sign_in.setter
    def force_change_password_next_sign_in(self, val):
        self._prop_dict["forceChangePasswordNextSignIn"] = val

