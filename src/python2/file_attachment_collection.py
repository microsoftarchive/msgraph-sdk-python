# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import file_attachment_request_builder # import FileAttachmentRequestBuilder
#from .file_attachment_request_builder import FileAttachmentRequestBuilder
from ..model.file_attachment import FileAttachment
import json

class FileAttachmentCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the FileAttachmentCollectionRequest
        
        Args:
            request_url (str): The url to perform the FileAttachmentCollectionRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(FileAttachmentCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the FileAttachmentCollectionPage

        Returns: 
            :class:`FileAttachmentCollectionPage<microsoft.msgraph.request.file_attachment_collection.FileAttachmentCollectionPage>`:
                The FileAttachmentCollectionPage
        """
        self.method = "GET"
        collection_response = FileAttachmentCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class FileAttachmentCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the FileAttachmentRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a FileAttachmentRequestBuilder for
        
        Returns: 
            :class:`FileAttachmentRequestBuilder<microsoft.msgraph.request.file_attachment_request_builder.FileAttachmentRequestBuilder>`:
                A FileAttachmentRequestBuilder for that key
        """
        return file_attachment_request_builder.FileAttachmentRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the FileAttachmentCollectionRequest
        
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
            :class:`FileAttachmentCollectionRequest<microsoft.msgraph.request.file_attachment_collection.FileAttachmentCollectionRequest>`:
                The FileAttachmentCollectionRequest
        """
        req = FileAttachmentCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the FileAttachmentCollectionPage

        Returns: 
            :class:`FileAttachmentCollectionPage<microsoft.msgraph.request.file_attachment_collection.FileAttachmentCollectionPage>`:
                The FileAttachmentCollectionPage
        """
        return self.request().get()



class FileAttachmentCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`FileAttachmentCollectionPage<microsoft.msgraph.request.file_attachment_collection.FileAttachmentCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = FileAttachmentCollectionPage(self._prop_dict["value"])

        return self._collection_page


class FileAttachmentCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the FileAttachment at the index specified
        
        Args:
            index (int): The index of the item to get from the FileAttachmentCollectionPage

        Returns:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The FileAttachment at the index
        """
        return FileAttachment(self._prop_list[index])

    def file_attachment(self):
        """Get a generator of FileAttachment within the FileAttachmentCollectionPage
        
        Yields:
            :class:`FileAttachment<microsoft.msgraph.model.file_attachment.FileAttachment>`:
                The next FileAttachment in the collection
        """
        for item in self._prop_list:
            yield FileAttachment(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the FileAttachmentCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<microsoft.msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<microsoft.msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = FileAttachmentCollectionRequest(next_page_link, client, options)
