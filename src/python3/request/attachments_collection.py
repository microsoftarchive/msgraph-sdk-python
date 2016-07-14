# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import attachment_request_builder 
from ..model.attachment import Attachment
import json
import asyncio

class AttachmentsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the AttachmentsCollectionRequest
        
        Args:
            request_url (str): The url to perform the AttachmentsCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(AttachmentsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the AttachmentsCollectionPage

        Returns: 
            :class:`AttachmentsCollectionPage<msgraph.request.attachments_collection.AttachmentsCollectionPage>`:
                The AttachmentsCollectionPage
        """
        self.method = "GET"
        collection_response = AttachmentsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the AttachmentsCollectionPage in async

        Yields: 
            :class:`AttachmentsCollectionPage<msgraph.request.attachments_collection.AttachmentsCollectionPage>`:
                The AttachmentsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class AttachmentsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the AttachmentRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a AttachmentRequestBuilder for
        
        Returns: 
            :class:`AttachmentRequestBuilder<msgraph.request.attachment_request_builder.AttachmentRequestBuilder>`:
                A AttachmentRequestBuilder for that key
        """
        return attachment_request_builder.AttachmentRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the AttachmentsCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`AttachmentsCollectionRequest<msgraph.request.attachments_collection.AttachmentsCollectionRequest>`:
                The AttachmentsCollectionRequest
        """
        req = AttachmentsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the AttachmentsCollectionPage

        Returns: 
            :class:`AttachmentsCollectionPage<msgraph.request.attachments_collection.AttachmentsCollectionPage>`:
                The AttachmentsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the AttachmentsCollectionPage in async

        Yields: 
            :class:`AttachmentsCollectionPage<msgraph.request.attachments_collection.AttachmentsCollectionPage>`:
                The AttachmentsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class AttachmentsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`AttachmentsCollectionPage<msgraph.request.attachments_collection.AttachmentsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = AttachmentsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class AttachmentsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Attachment at the index specified
        
        Args:
            index (int): The index of the item to get from the AttachmentsCollectionPage

        Returns:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The Attachment at the index
        """
        return Attachment(self._prop_list[index])

    def attachments(self):
        """Get a generator of Attachment within the AttachmentsCollectionPage
        
        Yields:
            :class:`Attachment<msgraph.model.attachment.Attachment>`:
                The next Attachment in the collection
        """
        for item in self._prop_list:
            yield Attachment(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the AttachmentsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = AttachmentsCollectionRequest(next_page_link, client, options)
