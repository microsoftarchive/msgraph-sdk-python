# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import reference_attachment_request_builder # import ReferenceAttachmentRequestBuilder
#from .reference_attachment_request_builder import ReferenceAttachmentRequestBuilder
from ..model.reference_attachment import ReferenceAttachment
import json

class ReferenceAttachmentCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ReferenceAttachmentCollectionRequest
        
        Args:
            request_url (str): The url to perform the ReferenceAttachmentCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ReferenceAttachmentCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ReferenceAttachmentCollectionPage

        Returns: 
            :class:`ReferenceAttachmentCollectionPage<microsoft.msgraph.request.reference_attachment_collection.ReferenceAttachmentCollectionPage>`:
                The ReferenceAttachmentCollectionPage
        """
        self.method = "GET"
        collection_response = ReferenceAttachmentCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class ReferenceAttachmentCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ReferenceAttachmentRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ReferenceAttachmentRequestBuilder for
        
        Returns: 
            :class:`ReferenceAttachmentRequestBuilder<microsoft.msgraph.request.reference_attachment_request_builder.ReferenceAttachmentRequestBuilder>`:
                A ReferenceAttachmentRequestBuilder for that key
        """
        return reference_attachment_request_builder.ReferenceAttachmentRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the ReferenceAttachmentCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ReferenceAttachmentCollectionRequest<microsoft.msgraph.request.reference_attachment_collection.ReferenceAttachmentCollectionRequest>`:
                The ReferenceAttachmentCollectionRequest
        """
        req = ReferenceAttachmentCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the ReferenceAttachmentCollectionPage

        Returns: 
            :class:`ReferenceAttachmentCollectionPage<microsoft.msgraph.request.reference_attachment_collection.ReferenceAttachmentCollectionPage>`:
                The ReferenceAttachmentCollectionPage
        """
        return self.request().get()



class ReferenceAttachmentCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ReferenceAttachmentCollectionPage<microsoft.msgraph.request.reference_attachment_collection.ReferenceAttachmentCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ReferenceAttachmentCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ReferenceAttachmentCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ReferenceAttachment at the index specified
        
        Args:
            index (int): The index of the item to get from the ReferenceAttachmentCollectionPage

        Returns:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The ReferenceAttachment at the index
        """
        return ReferenceAttachment(self._prop_list[index])

    def reference_attachment(self):
        """Get a generator of ReferenceAttachment within the ReferenceAttachmentCollectionPage
        
        Yields:
            :class:`ReferenceAttachment<microsoft.msgraph.model.reference_attachment.ReferenceAttachment>`:
                The next ReferenceAttachment in the collection
        """
        for item in self._prop_list:
            yield ReferenceAttachment(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ReferenceAttachmentCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ReferenceAttachmentCollectionRequest(next_page_link, client, options)
