# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.item_body import ItemBody
from ..model.importance import Importance
from ..model.recipient import Recipient
from ..model.inference_classification_type import InferenceClassificationType
from datetime import datetime

from .outlook_item import OutlookItem

class Message(OutlookItem):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def sent_date_time(self):
        """
        Gets and sets the sentDateTime
        
        Returns:
            datetime:
                The sentDateTime
        """
        if "sentDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["sentDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @sent_date_time.setter
    def sent_date_time(self, val):
        self._prop_dict["sentDateTime"] = val.isoformat()+"Z"

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
    def internet_message_id(self):
        """
        Gets and sets the internetMessageId
        
        Returns:
            str:
                The internetMessageId
        """
        if "internetMessageId" in self._prop_dict:
            return self._prop_dict["internetMessageId"]
        else:
            return None

    @internet_message_id.setter
    def internet_message_id(self, val):
        self._prop_dict["internetMessageId"] = val

    @property
    def subject(self):
        """
        Gets and sets the subject
        
        Returns:
            str:
                The subject
        """
        if "subject" in self._prop_dict:
            return self._prop_dict["subject"]
        else:
            return None

    @subject.setter
    def subject(self, val):
        self._prop_dict["subject"] = val

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
    def body_preview(self):
        """
        Gets and sets the bodyPreview
        
        Returns:
            str:
                The bodyPreview
        """
        if "bodyPreview" in self._prop_dict:
            return self._prop_dict["bodyPreview"]
        else:
            return None

    @body_preview.setter
    def body_preview(self, val):
        self._prop_dict["bodyPreview"] = val

    @property
    def importance(self):
        """
        Gets and sets the importance
        
        Returns: 
            :class:`Importance<microsoft.graph.model.importance.Importance>`:
                The importance
        """
        if "importance" in self._prop_dict:
            if isinstance(self._prop_dict["importance"], GraphObjectBase):
                return self._prop_dict["importance"]
            else:
                self._prop_dict["importance"] = Importance(self._prop_dict["importance"])
                return self._prop_dict["importance"]

        return None

    @importance.setter
    def importance(self, val):
        self._prop_dict["importance"] = val

    @property
    def parent_folder_id(self):
        """
        Gets and sets the parentFolderId
        
        Returns:
            str:
                The parentFolderId
        """
        if "parentFolderId" in self._prop_dict:
            return self._prop_dict["parentFolderId"]
        else:
            return None

    @parent_folder_id.setter
    def parent_folder_id(self, val):
        self._prop_dict["parentFolderId"] = val

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
    def bcc_recipients(self):
        """Gets and sets the bccRecipients
        
        Returns: 
            :class:`BccRecipientsCollectionPage<microsoft.graph.request.bcc_recipients_collection.BccRecipientsCollectionPage>`:
                The bccRecipients
        """
        if "bccRecipients" in self._prop_dict:
            return BccRecipientsCollectionPage(self._prop_dict["bccRecipients"])
        else:
            return None

    @property
    def reply_to(self):
        """Gets and sets the replyTo
        
        Returns: 
            :class:`ReplyToCollectionPage<microsoft.graph.request.reply_to_collection.ReplyToCollectionPage>`:
                The replyTo
        """
        if "replyTo" in self._prop_dict:
            return ReplyToCollectionPage(self._prop_dict["replyTo"])
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
    def unique_body(self):
        """
        Gets and sets the uniqueBody
        
        Returns: 
            :class:`ItemBody<microsoft.graph.model.item_body.ItemBody>`:
                The uniqueBody
        """
        if "uniqueBody" in self._prop_dict:
            if isinstance(self._prop_dict["uniqueBody"], GraphObjectBase):
                return self._prop_dict["uniqueBody"]
            else:
                self._prop_dict["uniqueBody"] = ItemBody(self._prop_dict["uniqueBody"])
                return self._prop_dict["uniqueBody"]

        return None

    @unique_body.setter
    def unique_body(self, val):
        self._prop_dict["uniqueBody"] = val

    @property
    def is_delivery_receipt_requested(self):
        """
        Gets and sets the isDeliveryReceiptRequested
        
        Returns:
            bool:
                The isDeliveryReceiptRequested
        """
        if "isDeliveryReceiptRequested" in self._prop_dict:
            return self._prop_dict["isDeliveryReceiptRequested"]
        else:
            return None

    @is_delivery_receipt_requested.setter
    def is_delivery_receipt_requested(self, val):
        self._prop_dict["isDeliveryReceiptRequested"] = val

    @property
    def is_read_receipt_requested(self):
        """
        Gets and sets the isReadReceiptRequested
        
        Returns:
            bool:
                The isReadReceiptRequested
        """
        if "isReadReceiptRequested" in self._prop_dict:
            return self._prop_dict["isReadReceiptRequested"]
        else:
            return None

    @is_read_receipt_requested.setter
    def is_read_receipt_requested(self, val):
        self._prop_dict["isReadReceiptRequested"] = val

    @property
    def is_read(self):
        """
        Gets and sets the isRead
        
        Returns:
            bool:
                The isRead
        """
        if "isRead" in self._prop_dict:
            return self._prop_dict["isRead"]
        else:
            return None

    @is_read.setter
    def is_read(self, val):
        self._prop_dict["isRead"] = val

    @property
    def is_draft(self):
        """
        Gets and sets the isDraft
        
        Returns:
            bool:
                The isDraft
        """
        if "isDraft" in self._prop_dict:
            return self._prop_dict["isDraft"]
        else:
            return None

    @is_draft.setter
    def is_draft(self, val):
        self._prop_dict["isDraft"] = val

    @property
    def web_link(self):
        """
        Gets and sets the webLink
        
        Returns:
            str:
                The webLink
        """
        if "webLink" in self._prop_dict:
            return self._prop_dict["webLink"]
        else:
            return None

    @web_link.setter
    def web_link(self, val):
        self._prop_dict["webLink"] = val

    @property
    def inference_classification(self):
        """
        Gets and sets the inferenceClassification
        
        Returns: 
            :class:`InferenceClassificationType<microsoft.graph.model.inference_classification_type.InferenceClassificationType>`:
                The inferenceClassification
        """
        if "inferenceClassification" in self._prop_dict:
            if isinstance(self._prop_dict["inferenceClassification"], GraphObjectBase):
                return self._prop_dict["inferenceClassification"]
            else:
                self._prop_dict["inferenceClassification"] = InferenceClassificationType(self._prop_dict["inferenceClassification"])
                return self._prop_dict["inferenceClassification"]

        return None

    @inference_classification.setter
    def inference_classification(self, val):
        self._prop_dict["inferenceClassification"] = val

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

