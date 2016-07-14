# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..request_base import RequestBase
from ..model.device import Device
import json

class DeviceRequest(RequestBase):
    """The type DeviceRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DeviceRequest.

        Args:
            request_url (str): The url to perform the DeviceRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(DeviceRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Device."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Device.
        
        Returns:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The Device.
        """
        self.method = "GET"
        entity = Device(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, device):
        """Updates the specified Device.
        
        Args:
            device (:class:`Device<microsoft.msgraph.model.device.Device>`):
                The Device to update.

        Returns:
            :class:`Device<microsoft.msgraph.model.device.Device>`:
                The updated Device.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Device(json.loads(self.send(device).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.alternative_security_ids and value.alternative_security_ids._prop_dict:
                if "alternative_security_ids@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["alternative_security_ids@odata.nextLink"]
                    value.alternative_security_ids._init_next_page_request(next_page_link, self._client, None)
            if value.registered_owners and value.registered_owners._prop_dict:
                if "registered_owners@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["registered_owners@odata.nextLink"]
                    value.registered_owners._init_next_page_request(next_page_link, self._client, None)
            if value.registered_users and value.registered_users._prop_dict:
                if "registered_users@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["registered_users@odata.nextLink"]
                    value.registered_users._init_next_page_request(next_page_link, self._client, None)
