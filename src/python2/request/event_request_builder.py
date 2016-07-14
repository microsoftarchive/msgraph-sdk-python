# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from .event_request import EventRequest
from ..request_builder_base import RequestBuilderBase
from ..request.event_accept import EventAcceptRequestBuilder
from ..request.event_decline import EventDeclineRequestBuilder
from ..request.event_tentatively_accept import EventTentativelyAcceptRequestBuilder
from ..request.event_snooze_reminder import EventSnoozeReminderRequestBuilder
from ..request.event_dismiss_reminder import EventDismissReminderRequestBuilder
from ..request import calendar_request_builder
from ..request import event_collection
from ..request import attachment_collection


class EventRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the EventRequestBuilder

        Args:
            request_url (str): The url to perform the EventRequest
                on
            client (:class:`GraphClient<microsoft.msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
        """
        super(EventRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the EventRequest

        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            options (list of :class:`Option<microsoft.msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EventRequest<microsoft.msgraph.request.event_request.EventRequest>`:
                The EventRequest
        """
        req = EventRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Event."""
        self.request().delete()

    def get(self):
        """Gets the specified Event.
        
        Returns:
            :class:`Event<microsoft.msgraph.model.event.Event>`:
                The Event.
        """
        return self.request().get()

    def update(self, event):
        """Updates the specified Event.
        
        Args:
            event (:class:`Event<microsoft.msgraph.model.event.Event>`):
                The Event to update.

        Returns:
            :class:`Event<microsoft.msgraph.model.event.Event>`:
                The updated Event
        """
        return self.request().update(event)


    @property
    def calendar(self):
        """The calendar for the EventRequestBuilder

        Returns: 
            :class:`CalendarRequestBuilder<microsoft.msgraph.request.calendar_request.CalendarRequestBuilder>`:
                A request builder created from the EventRequestBuilder
        """
        return calendar_request_builder.CalendarRequestBuilder(self.append_to_request_url("calendar"), self._client)


    @property
    def instances(self):
        """The instances for the EventRequestBuilder

        Returns: 
            :class:`EventCollectionRequestBuilder<microsoft.msgraph.request.instances_collection.EventCollectionRequestBuilder>`:
                A request builder created from the EventRequestBuilder
        """
        return event_collection.EventCollectionRequestBuilder(self.append_to_request_url("instances"), self._client)

    @property
    def attachments(self):
        """The attachments for the EventRequestBuilder

        Returns: 
            :class:`AttachmentCollectionRequestBuilder<microsoft.msgraph.request.attachments_collection.AttachmentCollectionRequestBuilder>`:
                A request builder created from the EventRequestBuilder
        """
        return attachment_collection.AttachmentCollectionRequestBuilder(self.append_to_request_url("attachments"), self._client)
    def accept(self, comment=None, send_response=None):
        """Executes the accept method

        Args:
            comment (str):
                The comment to use in the method request          
            send_response (bool):
                The send_response to use in the method request          

        Returns:
            :class:`EventAcceptRequestBuilder<microsoft.msgraph.request.event_accept.EventAcceptRequestBuilder>`:
                A EventAcceptRequestBuilder for the method
        """
        return EventAcceptRequestBuilder(self.append_to_request_url("accept"), self._client, comment=comment, send_response=send_response)

    def decline(self, comment=None, send_response=None):
        """Executes the decline method

        Args:
            comment (str):
                The comment to use in the method request          
            send_response (bool):
                The send_response to use in the method request          

        Returns:
            :class:`EventDeclineRequestBuilder<microsoft.msgraph.request.event_decline.EventDeclineRequestBuilder>`:
                A EventDeclineRequestBuilder for the method
        """
        return EventDeclineRequestBuilder(self.append_to_request_url("decline"), self._client, comment=comment, send_response=send_response)

    def tentatively_accept(self, comment=None, send_response=None):
        """Executes the tentativelyAccept method

        Args:
            comment (str):
                The comment to use in the method request          
            send_response (bool):
                The send_response to use in the method request          

        Returns:
            :class:`EventTentativelyAcceptRequestBuilder<microsoft.msgraph.request.event_tentatively_accept.EventTentativelyAcceptRequestBuilder>`:
                A EventTentativelyAcceptRequestBuilder for the method
        """
        return EventTentativelyAcceptRequestBuilder(self.append_to_request_url("tentativelyAccept"), self._client, comment=comment, send_response=send_response)

    def snooze_reminder(self, new_reminder_time):
        """Executes the snoozeReminder method

        Args:
            new_reminder_time (:class:`DateTimeTimeZone<microsoft.msgraph.model.date_time_time_zone.DateTimeTimeZone>`):
                The new_reminder_time to use in the method request

        Returns:
            :class:`EventSnoozeReminderRequestBuilder<microsoft.msgraph.request.event_snooze_reminder.EventSnoozeReminderRequestBuilder>`:
                A EventSnoozeReminderRequestBuilder for the method
        """
        return EventSnoozeReminderRequestBuilder(self.append_to_request_url("snoozeReminder"), self._client, new_reminder_time)

    def dismiss_reminder(self):
        """Executes the dismissReminder method


        Returns:
            :class:`EventDismissReminderRequestBuilder<microsoft.msgraph.request.event_dismiss_reminder.EventDismissReminderRequestBuilder>`:
                A EventDismissReminderRequestBuilder for the method
        """
        return EventDismissReminderRequestBuilder(self.append_to_request_url("dismissReminder"), self._client)


