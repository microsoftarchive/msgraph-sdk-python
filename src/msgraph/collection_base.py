"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

from __future__ import unicode_literals
from .request_base import RequestBase


class CollectionRequestBase(RequestBase):

    def __init__(self, request_url, client, options):
        super(CollectionRequestBase, self).__init__(request_url, client, options)

    def _init_next_page_request(self, next_page_link, client, options):
        # implemented in each collection request
        pass

    def _page_from_response(self, response):
        """Get the collection page from within the response
        
        Args:
            response (:class:`CollectionResponseBase`): 
                The response to get the collection page from

        Returns: 
            The collection page from within the response
        """
        if response:
            if "@odata.nextLink" in response._prop_dict:
                next_page_link = response._prop_dict["@odata.nextLink"]
                response.collection_page._init_next_page_request(next_page_link, self._client, None)
            return response.collection_page
        return None


class CollectionResponseBase(object):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict
        self._collection_page = None

    @property
    def collection_page(self):
        pass


class CollectionPageBase(object):
    
    def __init__(self, prop_list = []):
        self._prop_list = prop_list

    def __len__(self):
        return len(self._prop_list)

    @property
    def next_page_request(self):
        """Gets a request for the next page of a collection, if one exists
        
        Returns:
            The request object to send
        """
        try:
            return self._next_page_request
        except:
            return None
