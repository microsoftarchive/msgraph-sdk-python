# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .message_request import MessageRequest
from ..request_builder_base import RequestBuilderBase
from ..request.message_copy import MessageCopyRequestBuilder
from ..request.message_move import MessageMoveRequestBuilder
from ..request.message_create_reply import MessageCreateReplyRequestBuilder
from ..request.message_create_reply_all import MessageCreateReplyAllRequestBuilder
from ..request.message_create_forward import MessageCreateForwardRequestBuilder
from ..request.message_reply import MessageReplyRequestBuilder
from ..request.message_reply_all import MessageReplyAllRequestBuilder
from ..request.message_forward import MessageForwardRequestBuilder
from ..request.message_send import MessageSendRequestBuilder
from ..request import attachment_collection


class MessageRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the MessageRequestBuilder

        Args:
            request_url (str): The url to perform the MessageRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(MessageRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the MessageRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`MessageRequest<microsoft.msgraph.request.message_request.MessageRequest>`:
                The MessageRequest
        """
        req = MessageRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Message."""
        self.request().delete()

    def get(self):
        """Gets the specified Message.
        
        Returns:
            :class:`Message<microsoft.msgraph.model.message.Message>`:
                The Message.
        """
        return self.request().get()

    def update(self, message):
        """Updates the specified Message.
        
        Args:
            message (:class:`Message<microsoft.msgraph.model.message.Message>`):
                The Message to update.

        Returns:
            :class:`Message<microsoft.msgraph.model.message.Message>`:
                The updated Message
        """
        return self.request().update(message)

    @property
    def event_message(self):
        """The event_message for the MessageRequestBuilder

        Returns:
            :class:`EventMessageRequestBuilder<microsoft.msgraph.request.event_message_request.EventMessageRequestBuilder>`:
                A request builder created from the MessageRequestBuilder
        """
        return EventMessageRequestBuilder(self.append_to_request_url("eventMessage"), self._client)


    @property
    def attachments(self):
        """The attachments for the MessageRequestBuilder

        Returns: 
            :class:`AttachmentCollectionRequestBuilder<microsoft.msgraph.request.attachments_collection.AttachmentCollectionRequestBuilder>`:
                A request builder created from the MessageRequestBuilder
        """
        return attachment_collection.AttachmentCollectionRequestBuilder(self.append_to_request_url("attachments"), self._client)
    def copy(self, destination_id=None):
        """Executes the copy method

        Args:
            destination_id (str):
                The destination_id to use in the method request          

        Returns:
            :class:`MessageCopyRequestBuilder<microsoft.msgraph.request.message_copy.MessageCopyRequestBuilder>`:
                A MessageCopyRequestBuilder for the method
        """
        return MessageCopyRequestBuilder(self.append_to_request_url("copy"), self._client, destination_id=destination_id)

    def move(self, destination_id=None):
        """Executes the move method

        Args:
            destination_id (str):
                The destination_id to use in the method request          

        Returns:
            :class:`MessageMoveRequestBuilder<microsoft.msgraph.request.message_move.MessageMoveRequestBuilder>`:
                A MessageMoveRequestBuilder for the method
        """
        return MessageMoveRequestBuilder(self.append_to_request_url("move"), self._client, destination_id=destination_id)

    def create_reply(self):
        """Executes the createReply method


        Returns:
            :class:`MessageCreateReplyRequestBuilder<microsoft.msgraph.request.message_create_reply.MessageCreateReplyRequestBuilder>`:
                A MessageCreateReplyRequestBuilder for the method
        """
        return MessageCreateReplyRequestBuilder(self.append_to_request_url("createReply"), self._client)

    def create_reply_all(self):
        """Executes the createReplyAll method


        Returns:
            :class:`MessageCreateReplyAllRequestBuilder<microsoft.msgraph.request.message_create_reply_all.MessageCreateReplyAllRequestBuilder>`:
                A MessageCreateReplyAllRequestBuilder for the method
        """
        return MessageCreateReplyAllRequestBuilder(self.append_to_request_url("createReplyAll"), self._client)

    def create_forward(self):
        """Executes the createForward method


        Returns:
            :class:`MessageCreateForwardRequestBuilder<microsoft.msgraph.request.message_create_forward.MessageCreateForwardRequestBuilder>`:
                A MessageCreateForwardRequestBuilder for the method
        """
        return MessageCreateForwardRequestBuilder(self.append_to_request_url("createForward"), self._client)

    def reply(self, comment=None):
        """Executes the reply method

        Args:
            comment (str):
                The comment to use in the method request          

        Returns:
            :class:`MessageReplyRequestBuilder<microsoft.msgraph.request.message_reply.MessageReplyRequestBuilder>`:
                A MessageReplyRequestBuilder for the method
        """
        return MessageReplyRequestBuilder(self.append_to_request_url("reply"), self._client, comment=comment)

    def reply_all(self, comment=None):
        """Executes the replyAll method

        Args:
            comment (str):
                The comment to use in the method request          

        Returns:
            :class:`MessageReplyAllRequestBuilder<microsoft.msgraph.request.message_reply_all.MessageReplyAllRequestBuilder>`:
                A MessageReplyAllRequestBuilder for the method
        """
        return MessageReplyAllRequestBuilder(self.append_to_request_url("replyAll"), self._client, comment=comment)

    def forward(self, comment=None, to_recipients=None):
        """Executes the forward method

        Args:
            comment (str):
                The comment to use in the method request          
            to_recipients (:class:`Recipient<microsoft.msgraph.model.recipient.Recipient>`):
                Defaults to None, The to_recipients to use in the method request

        Returns:
            :class:`MessageForwardRequestBuilder<microsoft.msgraph.request.message_forward.MessageForwardRequestBuilder>`:
                A MessageForwardRequestBuilder for the method
        """
        return MessageForwardRequestBuilder(self.append_to_request_url("forward"), self._client, comment=comment, to_recipients=to_recipients)

    def send(self):
        """Executes the send method


        Returns:
            :class:`MessageSendRequestBuilder<microsoft.msgraph.request.message_send.MessageSendRequestBuilder>`:
                A MessageSendRequestBuilder for the method
        """
        return MessageSendRequestBuilder(self.append_to_request_url("send"), self._client)


