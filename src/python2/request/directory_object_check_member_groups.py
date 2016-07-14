# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
from ..request import drive_item_collection 


class DirectoryObjectCheckMemberGroupsRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, group_ids):
        super(DirectoryObjectCheckMemberGroupsRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if group_ids:
            self.body_options["groupIds"] = group_ids

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`DriveItemCollectionResponse<microsoft.msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting collection page from the operation
        """
        self.content_type = "application/json"
        collection_response = drive_item_collection.DriveItemCollectionResponse(json.loads(self.send(self.body_options).content))
        return self._page_from_response(collection_response)



class DirectoryObjectCheckMemberGroupsRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, group_ids):
        super(DirectoryObjectCheckMemberGroupsRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["groupIds"] = group_ids

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the request for the DirectoryObjectCheckMemberGroups
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`DirectoryObjectCheckMemberGroupsRequest<microsoft.msgraph.request.directory_object_check_member_groups.DirectoryObjectCheckMemberGroupsRequest>`:
                The request
        """
        req = DirectoryObjectCheckMemberGroupsRequest(self._request_url, self._client, options, self._method_options["groupIds"])
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`DriveItemCollectionResponse<microsoft.msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
            The resulting DriveItemCollectionResponse from the operation
        """
        return self.request().post()

