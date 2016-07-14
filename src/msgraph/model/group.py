# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.directory_object import DirectoryObject
from datetime import datetime

from .directory_object import DirectoryObject

class Group(DirectoryObject):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def group_types(self):
        """
        Gets and sets the groupTypes
        
        Returns:
            str:
                The groupTypes
        """
        if "groupTypes" in self._prop_dict:
            return self._prop_dict["groupTypes"]
        else:
            return None

    @group_types.setter
    def group_types(self, val):
        self._prop_dict["groupTypes"] = val

    @property
    def mail(self):
        """
        Gets and sets the mail
        
        Returns:
            str:
                The mail
        """
        if "mail" in self._prop_dict:
            return self._prop_dict["mail"]
        else:
            return None

    @mail.setter
    def mail(self, val):
        self._prop_dict["mail"] = val

    @property
    def mail_enabled(self):
        """
        Gets and sets the mailEnabled
        
        Returns:
            bool:
                The mailEnabled
        """
        if "mailEnabled" in self._prop_dict:
            return self._prop_dict["mailEnabled"]
        else:
            return None

    @mail_enabled.setter
    def mail_enabled(self, val):
        self._prop_dict["mailEnabled"] = val

    @property
    def mail_nickname(self):
        """
        Gets and sets the mailNickname
        
        Returns:
            str:
                The mailNickname
        """
        if "mailNickname" in self._prop_dict:
            return self._prop_dict["mailNickname"]
        else:
            return None

    @mail_nickname.setter
    def mail_nickname(self, val):
        self._prop_dict["mailNickname"] = val

    @property
    def on_premises_last_sync_date_time(self):
        """
        Gets and sets the onPremisesLastSyncDateTime
        
        Returns:
            datetime:
                The onPremisesLastSyncDateTime
        """
        if "onPremisesLastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["onPremisesLastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self, val):
        self._prop_dict["onPremisesLastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def on_premises_security_identifier(self):
        """
        Gets and sets the onPremisesSecurityIdentifier
        
        Returns:
            str:
                The onPremisesSecurityIdentifier
        """
        if "onPremisesSecurityIdentifier" in self._prop_dict:
            return self._prop_dict["onPremisesSecurityIdentifier"]
        else:
            return None

    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self, val):
        self._prop_dict["onPremisesSecurityIdentifier"] = val

    @property
    def on_premises_sync_enabled(self):
        """
        Gets and sets the onPremisesSyncEnabled
        
        Returns:
            bool:
                The onPremisesSyncEnabled
        """
        if "onPremisesSyncEnabled" in self._prop_dict:
            return self._prop_dict["onPremisesSyncEnabled"]
        else:
            return None

    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self, val):
        self._prop_dict["onPremisesSyncEnabled"] = val

    @property
    def proxy_addresses(self):
        """
        Gets and sets the proxyAddresses
        
        Returns:
            str:
                The proxyAddresses
        """
        if "proxyAddresses" in self._prop_dict:
            return self._prop_dict["proxyAddresses"]
        else:
            return None

    @proxy_addresses.setter
    def proxy_addresses(self, val):
        self._prop_dict["proxyAddresses"] = val

    @property
    def security_enabled(self):
        """
        Gets and sets the securityEnabled
        
        Returns:
            bool:
                The securityEnabled
        """
        if "securityEnabled" in self._prop_dict:
            return self._prop_dict["securityEnabled"]
        else:
            return None

    @security_enabled.setter
    def security_enabled(self, val):
        self._prop_dict["securityEnabled"] = val

    @property
    def visibility(self):
        """
        Gets and sets the visibility
        
        Returns:
            str:
                The visibility
        """
        if "visibility" in self._prop_dict:
            return self._prop_dict["visibility"]
        else:
            return None

    @visibility.setter
    def visibility(self, val):
        self._prop_dict["visibility"] = val

    @property
    def allow_external_senders(self):
        """
        Gets and sets the allowExternalSenders
        
        Returns:
            bool:
                The allowExternalSenders
        """
        if "allowExternalSenders" in self._prop_dict:
            return self._prop_dict["allowExternalSenders"]
        else:
            return None

    @allow_external_senders.setter
    def allow_external_senders(self, val):
        self._prop_dict["allowExternalSenders"] = val

    @property
    def auto_subscribe_new_members(self):
        """
        Gets and sets the autoSubscribeNewMembers
        
        Returns:
            bool:
                The autoSubscribeNewMembers
        """
        if "autoSubscribeNewMembers" in self._prop_dict:
            return self._prop_dict["autoSubscribeNewMembers"]
        else:
            return None

    @auto_subscribe_new_members.setter
    def auto_subscribe_new_members(self, val):
        self._prop_dict["autoSubscribeNewMembers"] = val

    @property
    def is_subscribed_by_mail(self):
        """
        Gets and sets the isSubscribedByMail
        
        Returns:
            bool:
                The isSubscribedByMail
        """
        if "isSubscribedByMail" in self._prop_dict:
            return self._prop_dict["isSubscribedByMail"]
        else:
            return None

    @is_subscribed_by_mail.setter
    def is_subscribed_by_mail(self, val):
        self._prop_dict["isSubscribedByMail"] = val

    @property
    def unseen_count(self):
        """
        Gets and sets the unseenCount
        
        Returns:
            int:
                The unseenCount
        """
        if "unseenCount" in self._prop_dict:
            return self._prop_dict["unseenCount"]
        else:
            return None

    @unseen_count.setter
    def unseen_count(self, val):
        self._prop_dict["unseenCount"] = val

    @property
    def members(self):
        """Gets and sets the members
        
        Returns: 
            :class:`MembersCollectionPage<microsoft.graph.request.members_collection.MembersCollectionPage>`:
                The members
        """
        if "members" in self._prop_dict:
            return MembersCollectionPage(self._prop_dict["members"])
        else:
            return None

    @property
    def member_of(self):
        """Gets and sets the memberOf
        
        Returns: 
            :class:`MemberOfCollectionPage<microsoft.graph.request.member_of_collection.MemberOfCollectionPage>`:
                The memberOf
        """
        if "memberOf" in self._prop_dict:
            return MemberOfCollectionPage(self._prop_dict["memberOf"])
        else:
            return None

    @property
    def created_on_behalf_of(self):
        """
        Gets and sets the createdOnBehalfOf
        
        Returns: 
            :class:`DirectoryObject<microsoft.graph.model.directory_object.DirectoryObject>`:
                The createdOnBehalfOf
        """
        if "createdOnBehalfOf" in self._prop_dict:
            if isinstance(self._prop_dict["createdOnBehalfOf"], GraphObjectBase):
                return self._prop_dict["createdOnBehalfOf"]
            else:
                self._prop_dict["createdOnBehalfOf"] = DirectoryObject(self._prop_dict["createdOnBehalfOf"])
                return self._prop_dict["createdOnBehalfOf"]

        return None

    @created_on_behalf_of.setter
    def created_on_behalf_of(self, val):
        self._prop_dict["createdOnBehalfOf"] = val

    @property
    def owners(self):
        """Gets and sets the owners
        
        Returns: 
            :class:`OwnersCollectionPage<microsoft.graph.request.owners_collection.OwnersCollectionPage>`:
                The owners
        """
        if "owners" in self._prop_dict:
            return OwnersCollectionPage(self._prop_dict["owners"])
        else:
            return None

    @property
    def threads(self):
        """Gets and sets the threads
        
        Returns: 
            :class:`ThreadsCollectionPage<microsoft.graph.request.threads_collection.ThreadsCollectionPage>`:
                The threads
        """
        if "threads" in self._prop_dict:
            return ThreadsCollectionPage(self._prop_dict["threads"])
        else:
            return None

    @property
    def calendar(self):
        """
        Gets and sets the calendar
        
        Returns: 
            :class:`Calendar<microsoft.graph.model.calendar.Calendar>`:
                The calendar
        """
        if "calendar" in self._prop_dict:
            if isinstance(self._prop_dict["calendar"], GraphObjectBase):
                return self._prop_dict["calendar"]
            else:
                self._prop_dict["calendar"] = Calendar(self._prop_dict["calendar"])
                return self._prop_dict["calendar"]

        return None

    @calendar.setter
    def calendar(self, val):
        self._prop_dict["calendar"] = val

    @property
    def calendar_view(self):
        """Gets and sets the calendarView
        
        Returns: 
            :class:`CalendarViewCollectionPage<microsoft.graph.request.calendar_view_collection.CalendarViewCollectionPage>`:
                The calendarView
        """
        if "calendarView" in self._prop_dict:
            return CalendarViewCollectionPage(self._prop_dict["calendarView"])
        else:
            return None

    @property
    def events(self):
        """Gets and sets the events
        
        Returns: 
            :class:`EventsCollectionPage<microsoft.graph.request.events_collection.EventsCollectionPage>`:
                The events
        """
        if "events" in self._prop_dict:
            return EventsCollectionPage(self._prop_dict["events"])
        else:
            return None

    @property
    def conversations(self):
        """Gets and sets the conversations
        
        Returns: 
            :class:`ConversationsCollectionPage<microsoft.graph.request.conversations_collection.ConversationsCollectionPage>`:
                The conversations
        """
        if "conversations" in self._prop_dict:
            return ConversationsCollectionPage(self._prop_dict["conversations"])
        else:
            return None

    @property
    def photo(self):
        """
        Gets and sets the photo
        
        Returns: 
            :class:`ProfilePhoto<microsoft.graph.model.profile_photo.ProfilePhoto>`:
                The photo
        """
        if "photo" in self._prop_dict:
            if isinstance(self._prop_dict["photo"], GraphObjectBase):
                return self._prop_dict["photo"]
            else:
                self._prop_dict["photo"] = ProfilePhoto(self._prop_dict["photo"])
                return self._prop_dict["photo"]

        return None

    @photo.setter
    def photo(self, val):
        self._prop_dict["photo"] = val

    @property
    def accepted_senders(self):
        """Gets and sets the acceptedSenders
        
        Returns: 
            :class:`AcceptedSendersCollectionPage<microsoft.graph.request.accepted_senders_collection.AcceptedSendersCollectionPage>`:
                The acceptedSenders
        """
        if "acceptedSenders" in self._prop_dict:
            return AcceptedSendersCollectionPage(self._prop_dict["acceptedSenders"])
        else:
            return None

    @property
    def rejected_senders(self):
        """Gets and sets the rejectedSenders
        
        Returns: 
            :class:`RejectedSendersCollectionPage<microsoft.graph.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The rejectedSenders
        """
        if "rejectedSenders" in self._prop_dict:
            return RejectedSendersCollectionPage(self._prop_dict["rejectedSenders"])
        else:
            return None

    @property
    def drive(self):
        """
        Gets and sets the drive
        
        Returns: 
            :class:`Drive<microsoft.graph.model.drive.Drive>`:
                The drive
        """
        if "drive" in self._prop_dict:
            if isinstance(self._prop_dict["drive"], GraphObjectBase):
                return self._prop_dict["drive"]
            else:
                self._prop_dict["drive"] = Drive(self._prop_dict["drive"])
                return self._prop_dict["drive"]

        return None

    @drive.setter
    def drive(self, val):
        self._prop_dict["drive"] = val

