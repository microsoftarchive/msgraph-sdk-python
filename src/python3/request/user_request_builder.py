# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .user_request import UserRequest
from ..request_builder_base import RequestBuilderBase
from ..request.user_assign_license import UserAssignLicenseRequestBuilder
from ..request.user_change_password import UserChangePasswordRequestBuilder
from ..request.user_send_mail import UserSendMailRequestBuilder
from ..request.user_reminder_view import UserReminderViewRequestBuilder
import asyncio

from ..request import directory_object_collection
from ..request import directory_object_request_builder
from ..request import message_collection
from ..request import mail_folder_collection
from ..request import calendar_request_builder
from ..request import calendar_collection
from ..request import calendar_group_collection
from ..request import event_collection
from ..request import contact_collection
from ..request import contact_folder_collection
from ..request import inference_classification_request_builder
from ..request import profile_photo_request_builder
from ..request import drive_request_builder


class UserRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the UserRequestBuilder

        Args:
            request_url (str): The url to perform the UserRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(UserRequestBuilder, self).__init__(request_url, client)

    def request(self, options=None):
        """Builds the UserRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`UserRequest<msgraph.request.user_request.UserRequest>`:
                The UserRequest
        """
        req = UserRequest(self._request_url, self._client, options)
        req._set_query_options()
        return req

    def delete(self):
        """Deletes the specified User."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified User."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified User.
        
        Returns:
            :class:`User<msgraph.model.user.User>`:
                The User.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified User in async.

        Returns:
            :class:`User<msgraph.model.user.User>`:
                The User.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, user):
        """Updates the specified User.
        
        Args:
            user (:class:`User<msgraph.model.user.User>`):
                The User to update.

        Returns:
            :class:`User<msgraph.model.user.User>`:
                The updated User
        """
        return self.request().update(user)

    @asyncio.coroutine
    def update_async(self, user):
        """Updates the specified User in async
        
        Args:
            user (:class:`User<msgraph.model.user.User>`):
                The User to update.

        Returns:
            :class:`User<msgraph.model.user.User>`:
                The updated User.
        """
        entity = yield from self.request().update_async(user)
        return entity

    @property
    def owned_devices(self):
        """The owned_devices for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.owned_devices_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("ownedDevices"), self._client)

    @property
    def registered_devices(self):
        """The registered_devices for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.registered_devices_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("registeredDevices"), self._client)

    @property
    def manager(self):
        """The manager for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectRequestBuilder<msgraph.request.directory_object_request.DirectoryObjectRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_request_builder.DirectoryObjectRequestBuilder(self.append_to_request_url("manager"), self._client)


    @property
    def direct_reports(self):
        """The direct_reports for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.direct_reports_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("directReports"), self._client)

    @property
    def member_of(self):
        """The member_of for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.member_of_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("memberOf"), self._client)

    @property
    def created_objects(self):
        """The created_objects for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.created_objects_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("createdObjects"), self._client)

    @property
    def owned_objects(self):
        """The owned_objects for the UserRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.owned_objects_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("ownedObjects"), self._client)

    @property
    def messages(self):
        """The messages for the UserRequestBuilder

        Returns: 
            :class:`MessageCollectionRequestBuilder<msgraph.request.messages_collection.MessageCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return message_collection.MessageCollectionRequestBuilder(self.append_to_request_url("messages"), self._client)

    @property
    def mail_folders(self):
        """The mail_folders for the UserRequestBuilder

        Returns: 
            :class:`MailFolderCollectionRequestBuilder<msgraph.request.mail_folders_collection.MailFolderCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return mail_folder_collection.MailFolderCollectionRequestBuilder(self.append_to_request_url("mailFolders"), self._client)

    @property
    def calendar(self):
        """The calendar for the UserRequestBuilder

        Returns: 
            :class:`CalendarRequestBuilder<msgraph.request.calendar_request.CalendarRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return calendar_request_builder.CalendarRequestBuilder(self.append_to_request_url("calendar"), self._client)


    @property
    def calendars(self):
        """The calendars for the UserRequestBuilder

        Returns: 
            :class:`CalendarCollectionRequestBuilder<msgraph.request.calendars_collection.CalendarCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return calendar_collection.CalendarCollectionRequestBuilder(self.append_to_request_url("calendars"), self._client)

    @property
    def calendar_groups(self):
        """The calendar_groups for the UserRequestBuilder

        Returns: 
            :class:`CalendarGroupCollectionRequestBuilder<msgraph.request.calendar_groups_collection.CalendarGroupCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return calendar_group_collection.CalendarGroupCollectionRequestBuilder(self.append_to_request_url("calendarGroups"), self._client)

    @property
    def calendar_view(self):
        """The calendar_view for the UserRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.calendar_view_collection.EventCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("calendarView"), self._client)

    @property
    def events(self):
        """The events for the UserRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.events_collection.EventCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("events"), self._client)

    @property
    def contacts(self):
        """The contacts for the UserRequestBuilder

        Returns: 
            :class:`ContactCollectionRequestBuilder<msgraph.request.contacts_collection.ContactCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return contact_collection.ContactCollectionRequestBuilder(self.append_to_request_url("contacts"), self._client)

    @property
    def contact_folders(self):
        """The contact_folders for the UserRequestBuilder

        Returns: 
            :class:`ContactFolderCollectionRequestBuilder<msgraph.request.contact_folders_collection.ContactFolderCollectionRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return contact_folder_collection.ContactFolderCollectionRequestBuilder(self.append_to_request_url("contactFolders"), self._client)

    @property
    def inference_classification(self):
        """The inference_classification for the UserRequestBuilder

        Returns: 
            :class:`InferenceClassificationRequestBuilder<msgraph.request.inference_classification_request.InferenceClassificationRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return inference_classification_request_builder.InferenceClassificationRequestBuilder(self.append_to_request_url("inferenceClassification"), self._client)


    @property
    def photo(self):
        """The photo for the UserRequestBuilder

        Returns: 
            :class:`ProfilePhotoRequestBuilder<msgraph.request.profile_photo_request.ProfilePhotoRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return profile_photo_request_builder.ProfilePhotoRequestBuilder(self.append_to_request_url("photo"), self._client)


    @property
    def drive(self):
        """The drive for the UserRequestBuilder

        Returns: 
            :class:`DriveRequestBuilder<msgraph.request.drive_request.DriveRequestBuilder>`:
                A request builder created from the UserRequestBuilder
        """
        return drive_request_builder.DriveRequestBuilder(self.append_to_request_url("drive"), self._client)

    def assign_license(self, add_licenses, remove_licenses):
        """Executes the assignLicense method

        Args:
            add_licenses (:class:`AssignedLicense<msgraph.model.assigned_license.AssignedLicense>`):
                The add_licenses to use in the method request
            remove_licenses (UUID):
                The remove_licenses to use in the method request          

        Returns:
            :class:`UserAssignLicenseRequestBuilder<msgraph.request.user_assign_license.UserAssignLicenseRequestBuilder>`:
                A UserAssignLicenseRequestBuilder for the method
        """
        return UserAssignLicenseRequestBuilder(self.append_to_request_url("assignLicense"), self._client, add_licenses, remove_licenses)

    def change_password(self, current_password=None, new_password=None):
        """Executes the changePassword method

        Args:
            current_password (str):
                The current_password to use in the method request          
            new_password (str):
                The new_password to use in the method request          

        Returns:
            :class:`UserChangePasswordRequestBuilder<msgraph.request.user_change_password.UserChangePasswordRequestBuilder>`:
                A UserChangePasswordRequestBuilder for the method
        """
        return UserChangePasswordRequestBuilder(self.append_to_request_url("changePassword"), self._client, current_password=current_password, new_password=new_password)

    def send_mail(self, message, save_to_sent_items=None):
        """Executes the sendMail method

        Args:
            message (:class:`Message<msgraph.model.message.Message>`):
                The message to use in the method request
            save_to_sent_items (bool):
                The save_to_sent_items to use in the method request          

        Returns:
            :class:`UserSendMailRequestBuilder<msgraph.request.user_send_mail.UserSendMailRequestBuilder>`:
                A UserSendMailRequestBuilder for the method
        """
        return UserSendMailRequestBuilder(self.append_to_request_url("sendMail"), self._client, message, save_to_sent_items=save_to_sent_items)

    def reminder_view(self, start_date_time, end_date_time=None):
        """Executes the reminderView method

        Args:
            start_date_time (str):
                The start_date_time to use in the method request          
            end_date_time (str):
                The end_date_time to use in the method request          

        Returns:
            :class:`UserReminderViewRequestBuilder<msgraph.request.user_reminder_view.UserReminderViewRequestBuilder>`:
                A UserReminderViewRequestBuilder for the method
        """
        return UserReminderViewRequestBuilder(self.append_to_request_url("reminderView"), self._client, start_date_time, end_date_time=end_date_time)


