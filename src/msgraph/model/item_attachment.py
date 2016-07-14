# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .attachment import Attachment

class ItemAttachment(Attachment):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def item(self):
        """
        Gets and sets the item
        
        Returns: 
            :class:`OutlookItem<microsoft.graph.model.outlook_item.OutlookItem>`:
                The item
        """
        if "item" in self._prop_dict:
            if isinstance(self._prop_dict["item"], GraphObjectBase):
                return self._prop_dict["item"]
            else:
                self._prop_dict["item"] = OutlookItem(self._prop_dict["item"])
                return self._prop_dict["item"]

        return None

    @item.setter
    def item(self, val):
        self._prop_dict["item"] = val

