# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .group_request import GroupRequest
from ..request_builder_base import RequestBuilderBase
from ..request.group_subscribe_by_mail import GroupSubscribeByMailRequestBuilder
from ..request.group_unsubscribe_by_mail import GroupUnsubscribeByMailRequestBuilder
from ..request.group_add_favorite import GroupAddFavoriteRequestBuilder
from ..request.group_remove_favorite import GroupRemoveFavoriteRequestBuilder
from ..request.group_reset_unseen_count import GroupResetUnseenCountRequestBuilder
import asyncio

from ..request import directory_object_collection
from ..request import directory_object_request_builder
from ..request import conversation_thread_collection
from ..request import calendar_request_builder
from ..request import event_collection
from ..request import conversation_collection
from ..request import profile_photo_request_builder
from ..request import drive_request_builder


class GroupRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the GroupRequestBuilder

        Args:
            request_url (str): The url to perform the GroupRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(GroupRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, top=None, filter=None, options=None):
        """Builds the GroupRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`GroupRequest<msgraph.request.group_request.GroupRequest>`:
                The GroupRequest
        """
        req = GroupRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, filter=filter)
        return req

    def delete(self):
        """Deletes the specified Group."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Group."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Group.
        
        Returns:
            :class:`Group<msgraph.model.group.Group>`:
                The Group.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Group in async.

        Returns:
            :class:`Group<msgraph.model.group.Group>`:
                The Group.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, group):
        """Updates the specified Group.
        
        Args:
            group (:class:`Group<msgraph.model.group.Group>`):
                The Group to update.

        Returns:
            :class:`Group<msgraph.model.group.Group>`:
                The updated Group
        """
        return self.request().update(group)

    @asyncio.coroutine
    def update_async(self, group):
        """Updates the specified Group in async
        
        Args:
            group (:class:`Group<msgraph.model.group.Group>`):
                The Group to update.

        Returns:
            :class:`Group<msgraph.model.group.Group>`:
                The updated Group.
        """
        entity = yield from self.request().update_async(group)
        return entity

    @property
    def members(self):
        """The members for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.members_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("members"), self._client)

    @property
    def member_of(self):
        """The member_of for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.member_of_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("memberOf"), self._client)

    @property
    def created_on_behalf_of(self):
        """The created_on_behalf_of for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectRequestBuilder<msgraph.request.directory_object_request.DirectoryObjectRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_request_builder.DirectoryObjectRequestBuilder(self.append_to_request_url("createdOnBehalfOf"), self._client)


    @property
    def owners(self):
        """The owners for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.owners_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("owners"), self._client)

    @property
    def threads(self):
        """The threads for the GroupRequestBuilder

        Returns: 
            :class:`ConversationThreadCollectionRequestBuilder<msgraph.request.threads_collection.ConversationThreadCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return conversation_thread_collection.ConversationThreadCollectionRequestBuilder(self.append_to_request_url("threads"), self._client)

    @property
    def calendar(self):
        """The calendar for the GroupRequestBuilder

        Returns: 
            :class:`CalendarRequestBuilder<msgraph.request.calendar_request.CalendarRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return calendar_request_builder.CalendarRequestBuilder(self.append_to_request_url("calendar"), self._client)


    @property
    def calendar_view(self):
        """The calendar_view for the GroupRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.calendar_view_collection.EventCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("calendarView"), self._client)

    @property
    def events(self):
        """The events for the GroupRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<msgraph.request.events_collection.EventCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("events"), self._client)

    @property
    def conversations(self):
        """The conversations for the GroupRequestBuilder

        Returns: 
            :class:`ConversationCollectionRequestBuilder<msgraph.request.conversations_collection.ConversationCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return conversation_collection.ConversationCollectionRequestBuilder(self.append_to_request_url("conversations"), self._client)

    @property
    def photo(self):
        """The photo for the GroupRequestBuilder

        Returns: 
            :class:`ProfilePhotoRequestBuilder<msgraph.request.profile_photo_request.ProfilePhotoRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return profile_photo_request_builder.ProfilePhotoRequestBuilder(self.append_to_request_url("photo"), self._client)


    @property
    def accepted_senders(self):
        """The accepted_senders for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.accepted_senders_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("acceptedSenders"), self._client)

    @property
    def rejected_senders(self):
        """The rejected_senders for the GroupRequestBuilder

        Returns: 
            :class:`DirectoryObjectCollectionRequestBuilder<msgraph.request.rejected_senders_collection.DirectoryObjectCollectionRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return directory_object_collection.DirectoryObjectCollectionRequestBuilder(self.append_to_request_url("rejectedSenders"), self._client)

    @property
    def drive(self):
        """The drive for the GroupRequestBuilder

        Returns: 
            :class:`DriveRequestBuilder<msgraph.request.drive_request.DriveRequestBuilder>`:
                A request builder created from the GroupRequestBuilder
        """
        return drive_request_builder.DriveRequestBuilder(self.append_to_request_url("drive"), self._client)

    def subscribe_by_mail(self):
        """Executes the subscribeByMail method


        Returns:
            :class:`GroupSubscribeByMailRequestBuilder<msgraph.request.group_subscribe_by_mail.GroupSubscribeByMailRequestBuilder>`:
                A GroupSubscribeByMailRequestBuilder for the method
        """
        return GroupSubscribeByMailRequestBuilder(self.append_to_request_url("subscribeByMail"), self._client)

    def unsubscribe_by_mail(self):
        """Executes the unsubscribeByMail method


        Returns:
            :class:`GroupUnsubscribeByMailRequestBuilder<msgraph.request.group_unsubscribe_by_mail.GroupUnsubscribeByMailRequestBuilder>`:
                A GroupUnsubscribeByMailRequestBuilder for the method
        """
        return GroupUnsubscribeByMailRequestBuilder(self.append_to_request_url("unsubscribeByMail"), self._client)

    def add_favorite(self):
        """Executes the addFavorite method


        Returns:
            :class:`GroupAddFavoriteRequestBuilder<msgraph.request.group_add_favorite.GroupAddFavoriteRequestBuilder>`:
                A GroupAddFavoriteRequestBuilder for the method
        """
        return GroupAddFavoriteRequestBuilder(self.append_to_request_url("addFavorite"), self._client)

    def remove_favorite(self):
        """Executes the removeFavorite method


        Returns:
            :class:`GroupRemoveFavoriteRequestBuilder<msgraph.request.group_remove_favorite.GroupRemoveFavoriteRequestBuilder>`:
                A GroupRemoveFavoriteRequestBuilder for the method
        """
        return GroupRemoveFavoriteRequestBuilder(self.append_to_request_url("removeFavorite"), self._client)

    def reset_unseen_count(self):
        """Executes the resetUnseenCount method


        Returns:
            :class:`GroupResetUnseenCountRequestBuilder<msgraph.request.group_reset_unseen_count.GroupResetUnseenCountRequestBuilder>`:
                A GroupResetUnseenCountRequestBuilder for the method
        """
        return GroupResetUnseenCountRequestBuilder(self.append_to_request_url("resetUnseenCount"), self._client)


