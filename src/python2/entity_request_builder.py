# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .entity_request import EntityRequest
from ..request_builder_base import RequestBuilderBase


class EntityRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the EntityRequestBuilder

        Args:
            request_url (str): The url to perform the EntityRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(EntityRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the EntityRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EntityRequest<microsoft.msgraph.request.entity_request.EntityRequest>`:
                The EntityRequest
        """
        req = EntityRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Entity."""
        self.request().delete()

    def get(self):
        """Gets the specified Entity.
        
        Returns:
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The Entity.
        """
        return self.request().get()

    def update(self, entity):
        """Updates the specified Entity.
        
        Args:
            entity (:class:`Entity<microsoft.msgraph.model.entity.Entity>`):
                The Entity to update.

        Returns:
            :class:`Entity<microsoft.msgraph.model.entity.Entity>`:
                The updated Entity
        """
        return self.request().update(entity)

    @property
    def directory_object(self):
        """The directory_object for the EntityRequestBuilder

        Returns:
            :class:`DirectoryObjectRequestBuilder<microsoft.msgraph.request.directory_object_request.DirectoryObjectRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return DirectoryObjectRequestBuilder(self.append_to_request_url("directoryObject"), self._client)

    @property
    def conversation_thread(self):
        """The conversation_thread for the EntityRequestBuilder

        Returns:
            :class:`ConversationThreadRequestBuilder<microsoft.msgraph.request.conversation_thread_request.ConversationThreadRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return ConversationThreadRequestBuilder(self.append_to_request_url("conversationThread"), self._client)

    @property
    def calendar(self):
        """The calendar for the EntityRequestBuilder

        Returns:
            :class:`CalendarRequestBuilder<microsoft.msgraph.request.calendar_request.CalendarRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return CalendarRequestBuilder(self.append_to_request_url("calendar"), self._client)

    @property
    def outlook_item(self):
        """The outlook_item for the EntityRequestBuilder

        Returns:
            :class:`OutlookItemRequestBuilder<microsoft.msgraph.request.outlook_item_request.OutlookItemRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return OutlookItemRequestBuilder(self.append_to_request_url("outlookItem"), self._client)

    @property
    def conversation(self):
        """The conversation for the EntityRequestBuilder

        Returns:
            :class:`ConversationRequestBuilder<microsoft.msgraph.request.conversation_request.ConversationRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return ConversationRequestBuilder(self.append_to_request_url("conversation"), self._client)

    @property
    def profile_photo(self):
        """The profile_photo for the EntityRequestBuilder

        Returns:
            :class:`ProfilePhotoRequestBuilder<microsoft.msgraph.request.profile_photo_request.ProfilePhotoRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return ProfilePhotoRequestBuilder(self.append_to_request_url("profilePhoto"), self._client)

    @property
    def drive(self):
        """The drive for the EntityRequestBuilder

        Returns:
            :class:`DriveRequestBuilder<microsoft.msgraph.request.drive_request.DriveRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return DriveRequestBuilder(self.append_to_request_url("drive"), self._client)

    @property
    def subscribed_sku(self):
        """The subscribed_sku for the EntityRequestBuilder

        Returns:
            :class:`SubscribedSkuRequestBuilder<microsoft.msgraph.request.subscribed_sku_request.SubscribedSkuRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return SubscribedSkuRequestBuilder(self.append_to_request_url("subscribedSku"), self._client)

    @property
    def mail_folder(self):
        """The mail_folder for the EntityRequestBuilder

        Returns:
            :class:`MailFolderRequestBuilder<microsoft.msgraph.request.mail_folder_request.MailFolderRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return MailFolderRequestBuilder(self.append_to_request_url("mailFolder"), self._client)

    @property
    def calendar_group(self):
        """The calendar_group for the EntityRequestBuilder

        Returns:
            :class:`CalendarGroupRequestBuilder<microsoft.msgraph.request.calendar_group_request.CalendarGroupRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return CalendarGroupRequestBuilder(self.append_to_request_url("calendarGroup"), self._client)

    @property
    def contact_folder(self):
        """The contact_folder for the EntityRequestBuilder

        Returns:
            :class:`ContactFolderRequestBuilder<microsoft.msgraph.request.contact_folder_request.ContactFolderRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return ContactFolderRequestBuilder(self.append_to_request_url("contactFolder"), self._client)

    @property
    def attachment(self):
        """The attachment for the EntityRequestBuilder

        Returns:
            :class:`AttachmentRequestBuilder<microsoft.msgraph.request.attachment_request.AttachmentRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return AttachmentRequestBuilder(self.append_to_request_url("attachment"), self._client)

    @property
    def drive_item(self):
        """The drive_item for the EntityRequestBuilder

        Returns:
            :class:`DriveItemRequestBuilder<microsoft.msgraph.request.drive_item_request.DriveItemRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return DriveItemRequestBuilder(self.append_to_request_url("driveItem"), self._client)

    @property
    def permission(self):
        """The permission for the EntityRequestBuilder

        Returns:
            :class:`PermissionRequestBuilder<microsoft.msgraph.request.permission_request.PermissionRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return PermissionRequestBuilder(self.append_to_request_url("permission"), self._client)

    @property
    def thumbnail_set(self):
        """The thumbnail_set for the EntityRequestBuilder

        Returns:
            :class:`ThumbnailSetRequestBuilder<microsoft.msgraph.request.thumbnail_set_request.ThumbnailSetRequestBuilder>`:
                A request builder created from the EntityRequestBuilder
        """
        return ThumbnailSetRequestBuilder(self.append_to_request_url("thumbnailSet"), self._client)


