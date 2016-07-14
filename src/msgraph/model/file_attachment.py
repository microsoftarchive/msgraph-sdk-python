# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals

from .attachment import Attachment

class FileAttachment(Attachment):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def content_id(self):
        """
        Gets and sets the contentId
        
        Returns:
            str:
                The contentId
        """
        if "contentId" in self._prop_dict:
            return self._prop_dict["contentId"]
        else:
            return None

    @content_id.setter
    def content_id(self, val):
        self._prop_dict["contentId"] = val

    @property
    def content_location(self):
        """
        Gets and sets the contentLocation
        
        Returns:
            str:
                The contentLocation
        """
        if "contentLocation" in self._prop_dict:
            return self._prop_dict["contentLocation"]
        else:
            return None

    @content_location.setter
    def content_location(self, val):
        self._prop_dict["contentLocation"] = val

