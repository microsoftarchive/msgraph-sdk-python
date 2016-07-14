# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.response_status import ResponseStatus
from ..model.item_body import ItemBody
from ..model.importance import Importance
from ..model.sensitivity import Sensitivity
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.location import Location
from ..model.patterned_recurrence import PatternedRecurrence
from ..model.free_busy_status import FreeBusyStatus
from ..model.event_type import EventType
from ..model.recipient import Recipient
from datetime import datetime

from .outlook_item import OutlookItem

class Event(OutlookItem):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def original_start_time_zone(self):
        """
        Gets and sets the originalStartTimeZone
        
        Returns:
            str:
                The originalStartTimeZone
        """
        if "originalStartTimeZone" in self._prop_dict:
            return self._prop_dict["originalStartTimeZone"]
        else:
            return None

    @original_start_time_zone.setter
    def original_start_time_zone(self, val):
        self._prop_dict["originalStartTimeZone"] = val

    @property
    def original_end_time_zone(self):
        """
        Gets and sets the originalEndTimeZone
        
        Returns:
            str:
                The originalEndTimeZone
        """
        if "originalEndTimeZone" in self._prop_dict:
            return self._prop_dict["originalEndTimeZone"]
        else:
            return None

    @original_end_time_zone.setter
    def original_end_time_zone(self, val):
        self._prop_dict["originalEndTimeZone"] = val

    @property
    def response_status(self):
        """
        Gets and sets the responseStatus
        
        Returns: 
            :class:`ResponseStatus<microsoft.graph.model.response_status.ResponseStatus>`:
                The responseStatus
        """
        if "responseStatus" in self._prop_dict:
            if isinstance(self._prop_dict["responseStatus"], GraphObjectBase):
                return self._prop_dict["responseStatus"]
            else:
                self._prop_dict["responseStatus"] = ResponseStatus(self._prop_dict["responseStatus"])
                return self._prop_dict["responseStatus"]

        return None

    @response_status.setter
    def response_status(self, val):
        self._prop_dict["responseStatus"] = val

    @property
    def i_cal_u_id(self):
        """
        Gets and sets the iCalUId
        
        Returns:
            str:
                The iCalUId
        """
        if "iCalUId" in self._prop_dict:
            return self._prop_dict["iCalUId"]
        else:
            return None

    @i_cal_u_id.setter
    def i_cal_u_id(self, val):
        self._prop_dict["iCalUId"] = val

    @property
    def reminder_minutes_before_start(self):
        """
        Gets and sets the reminderMinutesBeforeStart
        
        Returns:
            int:
                The reminderMinutesBeforeStart
        """
        if "reminderMinutesBeforeStart" in self._prop_dict:
            return self._prop_dict["reminderMinutesBeforeStart"]
        else:
            return None

    @reminder_minutes_before_start.setter
    def reminder_minutes_before_start(self, val):
        self._prop_dict["reminderMinutesBeforeStart"] = val

    @property
    def is_reminder_on(self):
        """
        Gets and sets the isReminderOn
        
        Returns:
            bool:
                The isReminderOn
        """
        if "isReminderOn" in self._prop_dict:
            return self._prop_dict["isReminderOn"]
        else:
            return None

    @is_reminder_on.setter
    def is_reminder_on(self, val):
        self._prop_dict["isReminderOn"] = val

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
    def sensitivity(self):
        """
        Gets and sets the sensitivity
        
        Returns: 
            :class:`Sensitivity<microsoft.graph.model.sensitivity.Sensitivity>`:
                The sensitivity
        """
        if "sensitivity" in self._prop_dict:
            if isinstance(self._prop_dict["sensitivity"], GraphObjectBase):
                return self._prop_dict["sensitivity"]
            else:
                self._prop_dict["sensitivity"] = Sensitivity(self._prop_dict["sensitivity"])
                return self._prop_dict["sensitivity"]

        return None

    @sensitivity.setter
    def sensitivity(self, val):
        self._prop_dict["sensitivity"] = val

    @property
    def start(self):
        """
        Gets and sets the start
        
        Returns: 
            :class:`DateTimeTimeZone<microsoft.graph.model.date_time_time_zone.DateTimeTimeZone>`:
                The start
        """
        if "start" in self._prop_dict:
            if isinstance(self._prop_dict["start"], GraphObjectBase):
                return self._prop_dict["start"]
            else:
                self._prop_dict["start"] = DateTimeTimeZone(self._prop_dict["start"])
                return self._prop_dict["start"]

        return None

    @start.setter
    def start(self, val):
        self._prop_dict["start"] = val

    @property
    def original_start(self):
        """
        Gets and sets the originalStart
        
        Returns:
            datetime:
                The originalStart
        """
        if "originalStart" in self._prop_dict:
            return datetime.strptime(self._prop_dict["originalStart"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @original_start.setter
    def original_start(self, val):
        self._prop_dict["originalStart"] = val.isoformat()+"Z"

    @property
    def end(self):
        """
        Gets and sets the end
        
        Returns: 
            :class:`DateTimeTimeZone<microsoft.graph.model.date_time_time_zone.DateTimeTimeZone>`:
                The end
        """
        if "end" in self._prop_dict:
            if isinstance(self._prop_dict["end"], GraphObjectBase):
                return self._prop_dict["end"]
            else:
                self._prop_dict["end"] = DateTimeTimeZone(self._prop_dict["end"])
                return self._prop_dict["end"]

        return None

    @end.setter
    def end(self, val):
        self._prop_dict["end"] = val

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns: 
            :class:`Location<microsoft.graph.model.location.Location>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], GraphObjectBase):
                return self._prop_dict["location"]
            else:
                self._prop_dict["location"] = Location(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def is_all_day(self):
        """
        Gets and sets the isAllDay
        
        Returns:
            bool:
                The isAllDay
        """
        if "isAllDay" in self._prop_dict:
            return self._prop_dict["isAllDay"]
        else:
            return None

    @is_all_day.setter
    def is_all_day(self, val):
        self._prop_dict["isAllDay"] = val

    @property
    def is_cancelled(self):
        """
        Gets and sets the isCancelled
        
        Returns:
            bool:
                The isCancelled
        """
        if "isCancelled" in self._prop_dict:
            return self._prop_dict["isCancelled"]
        else:
            return None

    @is_cancelled.setter
    def is_cancelled(self, val):
        self._prop_dict["isCancelled"] = val

    @property
    def is_organizer(self):
        """
        Gets and sets the isOrganizer
        
        Returns:
            bool:
                The isOrganizer
        """
        if "isOrganizer" in self._prop_dict:
            return self._prop_dict["isOrganizer"]
        else:
            return None

    @is_organizer.setter
    def is_organizer(self, val):
        self._prop_dict["isOrganizer"] = val

    @property
    def recurrence(self):
        """
        Gets and sets the recurrence
        
        Returns: 
            :class:`PatternedRecurrence<microsoft.graph.model.patterned_recurrence.PatternedRecurrence>`:
                The recurrence
        """
        if "recurrence" in self._prop_dict:
            if isinstance(self._prop_dict["recurrence"], GraphObjectBase):
                return self._prop_dict["recurrence"]
            else:
                self._prop_dict["recurrence"] = PatternedRecurrence(self._prop_dict["recurrence"])
                return self._prop_dict["recurrence"]

        return None

    @recurrence.setter
    def recurrence(self, val):
        self._prop_dict["recurrence"] = val

    @property
    def response_requested(self):
        """
        Gets and sets the responseRequested
        
        Returns:
            bool:
                The responseRequested
        """
        if "responseRequested" in self._prop_dict:
            return self._prop_dict["responseRequested"]
        else:
            return None

    @response_requested.setter
    def response_requested(self, val):
        self._prop_dict["responseRequested"] = val

    @property
    def series_master_id(self):
        """
        Gets and sets the seriesMasterId
        
        Returns:
            str:
                The seriesMasterId
        """
        if "seriesMasterId" in self._prop_dict:
            return self._prop_dict["seriesMasterId"]
        else:
            return None

    @series_master_id.setter
    def series_master_id(self, val):
        self._prop_dict["seriesMasterId"] = val

    @property
    def show_as(self):
        """
        Gets and sets the showAs
        
        Returns: 
            :class:`FreeBusyStatus<microsoft.graph.model.free_busy_status.FreeBusyStatus>`:
                The showAs
        """
        if "showAs" in self._prop_dict:
            if isinstance(self._prop_dict["showAs"], GraphObjectBase):
                return self._prop_dict["showAs"]
            else:
                self._prop_dict["showAs"] = FreeBusyStatus(self._prop_dict["showAs"])
                return self._prop_dict["showAs"]

        return None

    @show_as.setter
    def show_as(self, val):
        self._prop_dict["showAs"] = val

    @property
    def type_(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`EventType<microsoft.graph.model.event_type.EventType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], GraphObjectBase):
                return self._prop_dict["type"]
            else:
                self._prop_dict["type"] = EventType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type_.setter
    def type_(self, val):
        self._prop_dict["type"] = val

    @property
    def attendees(self):
        """Gets and sets the attendees
        
        Returns: 
            :class:`AttendeesCollectionPage<microsoft.graph.request.attendees_collection.AttendeesCollectionPage>`:
                The attendees
        """
        if "attendees" in self._prop_dict:
            return AttendeesCollectionPage(self._prop_dict["attendees"])
        else:
            return None

    @property
    def organizer(self):
        """
        Gets and sets the organizer
        
        Returns: 
            :class:`Recipient<microsoft.graph.model.recipient.Recipient>`:
                The organizer
        """
        if "organizer" in self._prop_dict:
            if isinstance(self._prop_dict["organizer"], GraphObjectBase):
                return self._prop_dict["organizer"]
            else:
                self._prop_dict["organizer"] = Recipient(self._prop_dict["organizer"])
                return self._prop_dict["organizer"]

        return None

    @organizer.setter
    def organizer(self, val):
        self._prop_dict["organizer"] = val

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
    def instances(self):
        """Gets and sets the instances
        
        Returns: 
            :class:`InstancesCollectionPage<microsoft.graph.request.instances_collection.InstancesCollectionPage>`:
                The instances
        """
        if "instances" in self._prop_dict:
            return InstancesCollectionPage(self._prop_dict["instances"])
        else:
            return None

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

