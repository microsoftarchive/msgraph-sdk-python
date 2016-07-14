# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase


class SearchResult(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def on_click_telemetry_url(self):
        """Gets and sets the onClickTelemetryUrl
        
        Returns: 
            str:
                The onClickTelemetryUrl
        """
        if "onClickTelemetryUrl" in self._prop_dict:
            return self._prop_dict["onClickTelemetryUrl"]
        else:
            return None

    @on_click_telemetry_url.setter
    def on_click_telemetry_url(self, val):
        self._prop_dict["onClickTelemetryUrl"] = val

