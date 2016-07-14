# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime

from .entity import Entity

class ConversationThread(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def to_recipients(self):
        """Gets and sets the toRecipients
        
        Returns: 
            :class:`ToRecipientsCollectionPage<microsoft.graph.request.to_recipients_collection.ToRecipientsCollectionPage>`:
                The toRecipients
        """
        if "toRecipients" in self._prop_dict:
            return ToRecipientsCollectionPage(self._prop_dict["toRecipients"])
        else:
            return None

    @property
    def topic(self):
        """
        Gets and sets the topic
        
        Returns:
            str:
                The topic
        """
        if "topic" in self._prop_dict:
            return self._prop_dict["topic"]
        else:
            return None

    @topic.setter
    def topic(self, val):
        self._prop_dict["topic"] = val

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
    def last_delivered_date_time(self):
        """
        Gets and sets the lastDeliveredDateTime
        
        Returns:
            datetime:
                The lastDeliveredDateTime
        """
        if "lastDeliveredDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastDeliveredDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_delivered_date_time.setter
    def last_delivered_date_time(self, val):
        self._prop_dict["lastDeliveredDateTime"] = val.isoformat()+"Z"

    @property
    def unique_senders(self):
        """
        Gets and sets the uniqueSenders
        
        Returns:
            str:
                The uniqueSenders
        """
        if "uniqueSenders" in self._prop_dict:
            return self._prop_dict["uniqueSenders"]
        else:
            return None

    @unique_senders.setter
    def unique_senders(self, val):
        self._prop_dict["uniqueSenders"] = val

    @property
    def cc_recipients(self):
        """Gets and sets the ccRecipients
        
        Returns: 
            :class:`CcRecipientsCollectionPage<microsoft.graph.request.cc_recipients_collection.CcRecipientsCollectionPage>`:
                The ccRecipients
        """
        if "ccRecipients" in self._prop_dict:
            return CcRecipientsCollectionPage(self._prop_dict["ccRecipients"])
        else:
            return None

    @property
    def preview(self):
        """
        Gets and sets the preview
        
        Returns:
            str:
                The preview
        """
        if "preview" in self._prop_dict:
            return self._prop_dict["preview"]
        else:
            return None

    @preview.setter
    def preview(self, val):
        self._prop_dict["preview"] = val

    @property
    def is_locked(self):
        """
        Gets and sets the isLocked
        
        Returns:
            bool:
                The isLocked
        """
        if "isLocked" in self._prop_dict:
            return self._prop_dict["isLocked"]
        else:
            return None

    @is_locked.setter
    def is_locked(self, val):
        self._prop_dict["isLocked"] = val

    @property
    def posts(self):
        """Gets and sets the posts
        
        Returns: 
            :class:`PostsCollectionPage<microsoft.graph.request.posts_collection.PostsCollectionPage>`:
                The posts
        """
        if "posts" in self._prop_dict:
            return PostsCollectionPage(self._prop_dict["posts"])
        else:
            return None

