# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.item_body import ItemBody
from ..model.recipient import Recipient
from datetime import datetime

from .outlook_item import OutlookItem

class Post(OutlookItem):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def body(self):
        """
        Gets and sets the body
        
        Returns: 
            :class:`ItemBody<microsoft.graph.model.item_body.ItemBody>`:
                The body
        """
        if "body" in self._prop_dict:
            if isinstance(self._prop_dict["body"], GraphObjectBase):
                return self._prop_dict["body"]
            else:
                self._prop_dict["body"] = ItemBody(self._prop_dict["body"])
                return self._prop_dict["body"]

        return None

    @body.setter
    def body(self, val):
        self._prop_dict["body"] = val

    @property
    def received_date_time(self):
        """
        Gets and sets the receivedDateTime
        
        Returns:
            datetime:
                The receivedDateTime
        """
        if "receivedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["receivedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @received_date_time.setter
    def received_date_time(self, val):
        self._prop_dict["receivedDateTime"] = val.isoformat()+"Z"

    @property
    def has_attachments(self):
        """
        Gets and sets the hasAttachments
        
        Returns:
            bool:
                The hasAttachments
        """
        if "hasAttachments" in self._prop_dict:
            return self._prop_dict["hasAttachments"]
        else:
            return None

    @has_attachments.setter
    def has_attachments(self, val):
        self._prop_dict["hasAttachments"] = val

    @property
    def from_(self):
        """
        Gets and sets the from
        
        Returns: 
            :class:`Recipient<microsoft.graph.model.recipient.Recipient>`:
                The from
        """
        if "from" in self._prop_dict:
            if isinstance(self._prop_dict["from"], GraphObjectBase):
                return self._prop_dict["from"]
            else:
                self._prop_dict["from"] = Recipient(self._prop_dict["from"])
                return self._prop_dict["from"]

        return None

    @from_.setter
    def from_(self, val):
        self._prop_dict["from"] = val

    @property
    def sender(self):
        """
        Gets and sets the sender
        
        Returns: 
            :class:`Recipient<microsoft.graph.model.recipient.Recipient>`:
                The sender
        """
        if "sender" in self._prop_dict:
            if isinstance(self._prop_dict["sender"], GraphObjectBase):
                return self._prop_dict["sender"]
            else:
                self._prop_dict["sender"] = Recipient(self._prop_dict["sender"])
                return self._prop_dict["sender"]

        return None

    @sender.setter
    def sender(self, val):
        self._prop_dict["sender"] = val

    @property
    def conversation_thread_id(self):
        """
        Gets and sets the conversationThreadId
        
        Returns:
            str:
                The conversationThreadId
        """
        if "conversationThreadId" in self._prop_dict:
            return self._prop_dict["conversationThreadId"]
        else:
            return None

    @conversation_thread_id.setter
    def conversation_thread_id(self, val):
        self._prop_dict["conversationThreadId"] = val

    @property
    def new_participants(self):
        """Gets and sets the newParticipants
        
        Returns: 
            :class:`NewParticipantsCollectionPage<microsoft.graph.request.new_participants_collection.NewParticipantsCollectionPage>`:
                The newParticipants
        """
        if "newParticipants" in self._prop_dict:
            return NewParticipantsCollectionPage(self._prop_dict["newParticipants"])
        else:
            return None

    @property
    def conversation_id(self):
        """
        Gets and sets the conversationId
        
        Returns:
            str:
                The conversationId
        """
        if "conversationId" in self._prop_dict:
            return self._prop_dict["conversationId"]
        else:
            return None

    @conversation_id.setter
    def conversation_id(self, val):
        self._prop_dict["conversationId"] = val

    @property
    def extensions(self):
        """Gets and sets the extensions
        
        Returns: 
            :class:`ExtensionsCollectionPage<microsoft.graph.request.extensions_collection.ExtensionsCollectionPage>`:
                The extensions
        """
        if "extensions" in self._prop_dict:
            return ExtensionsCollectionPage(self._prop_dict["extensions"])
        else:
            return None

    @property
    def in_reply_to(self):
        """
        Gets and sets the inReplyTo
        
        Returns: 
            :class:`Post<microsoft.graph.model.post.Post>`:
                The inReplyTo
        """
        if "inReplyTo" in self._prop_dict:
            if isinstance(self._prop_dict["inReplyTo"], GraphObjectBase):
                return self._prop_dict["inReplyTo"]
            else:
                self._prop_dict["inReplyTo"] = Post(self._prop_dict["inReplyTo"])
                return self._prop_dict["inReplyTo"]

        return None

    @in_reply_to.setter
    def in_reply_to(self, val):
        self._prop_dict["inReplyTo"] = val

    @property
    def attachments(self):
        """Gets and sets the attachments
        
        Returns: 
            :class:`AttachmentsCollectionPage<microsoft.graph.request.attachments_collection.AttachmentsCollectionPage>`:
                The attachments
        """
        if "attachments" in self._prop_dict:
            return AttachmentsCollectionPage(self._prop_dict["attachments"])
        else:
            return None

