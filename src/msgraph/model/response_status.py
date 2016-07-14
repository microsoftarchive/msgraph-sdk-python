# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.response_type import ResponseType
from datetime import datetime
from ..graph_object_base import GraphObjectBase


class ResponseStatus(GraphObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def response(self):
        """
        Gets and sets the response
        
        Returns: 
            :class:`ResponseType<microsoft.graph.model.response_type.ResponseType>`:
                The response
        """
        if "response" in self._prop_dict:
            if isinstance(self._prop_dict["response"], GraphObjectBase):
                return self._prop_dict["response"]
            else :
                self._prop_dict["response"] = ResponseType(self._prop_dict["response"])
                return self._prop_dict["response"]

        return None

    @response.setter
    def response(self, val):
        self._prop_dict["response"] = val
    @property
    def time(self):
        """Gets and sets the time
        
        Returns: 
            datetime:
                The time
        """
        if "time" in self._prop_dict:
            return datetime.strptime(self._prop_dict["time"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @time.setter
    def time(self, val):
        self._prop_dict["time"] = val.isoformat()+"Z"

