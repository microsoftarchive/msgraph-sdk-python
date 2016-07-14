# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

#from ..model.user import User
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json


class UserAssignLicenseRequest(RequestBase):

    def __init__(self, request_url, client, options, add_licenses, remove_licenses):
        super(UserAssignLicenseRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if add_licenses:
            self.body_options["addLicenses"] = add_licenses
        if remove_licenses:
            self.body_options["removeLicenses"] = remove_licenses

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`User<microsoft.msgraph.model.user.User>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = User(json.loads(self.send(self.body_options).content))
        return entity



class UserAssignLicenseRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, add_licenses, remove_licenses):
        super(UserAssignLicenseRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["addLicenses"] = add_licenses._prop_dict
        self._method_options["removeLicenses"] = remove_licenses

    def request(self, options=None):
        """Builds the request for the UserAssignLicense
        
        Args:
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`UserAssignLicenseRequest<microsoft.msgraph.request.user_assign_license.UserAssignLicenseRequest>`:
                The request
        """
        req = UserAssignLicenseRequest(self._request_url, self._client, options, self._method_options["addLicenses"], self._method_options["removeLicenses"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`User<microsoft.msgraph.model.user.User>`:
            The resulting User from the operation
        """
        return self.request().post()

