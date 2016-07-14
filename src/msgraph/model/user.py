# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.password_profile import PasswordProfile
from ..model.directory_object import DirectoryObject
from datetime import datetime

from .directory_object import DirectoryObject

class User(DirectoryObject):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_enabled(self):
        """
        Gets and sets the accountEnabled
        
        Returns:
            bool:
                The accountEnabled
        """
        if "accountEnabled" in self._prop_dict:
            return self._prop_dict["accountEnabled"]
        else:
            return None

    @account_enabled.setter
    def account_enabled(self, val):
        self._prop_dict["accountEnabled"] = val

    @property
    def assigned_licenses(self):
        """Gets and sets the assignedLicenses
        
        Returns: 
            :class:`AssignedLicensesCollectionPage<microsoft.graph.request.assigned_licenses_collection.AssignedLicensesCollectionPage>`:
                The assignedLicenses
        """
        if "assignedLicenses" in self._prop_dict:
            return AssignedLicensesCollectionPage(self._prop_dict["assignedLicenses"])
        else:
            return None

    @property
    def assigned_plans(self):
        """Gets and sets the assignedPlans
        
        Returns: 
            :class:`AssignedPlansCollectionPage<microsoft.graph.request.assigned_plans_collection.AssignedPlansCollectionPage>`:
                The assignedPlans
        """
        if "assignedPlans" in self._prop_dict:
            return AssignedPlansCollectionPage(self._prop_dict["assignedPlans"])
        else:
            return None

    @property
    def business_phones(self):
        """
        Gets and sets the businessPhones
        
        Returns:
            str:
                The businessPhones
        """
        if "businessPhones" in self._prop_dict:
            return self._prop_dict["businessPhones"]
        else:
            return None

    @business_phones.setter
    def business_phones(self, val):
        self._prop_dict["businessPhones"] = val

    @property
    def city(self):
        """
        Gets and sets the city
        
        Returns:
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def company_name(self):
        """
        Gets and sets the companyName
        
        Returns:
            str:
                The companyName
        """
        if "companyName" in self._prop_dict:
            return self._prop_dict["companyName"]
        else:
            return None

    @company_name.setter
    def company_name(self, val):
        self._prop_dict["companyName"] = val

    @property
    def country(self):
        """
        Gets and sets the country
        
        Returns:
            str:
                The country
        """
        if "country" in self._prop_dict:
            return self._prop_dict["country"]
        else:
            return None

    @country.setter
    def country(self, val):
        self._prop_dict["country"] = val

    @property
    def department(self):
        """
        Gets and sets the department
        
        Returns:
            str:
                The department
        """
        if "department" in self._prop_dict:
            return self._prop_dict["department"]
        else:
            return None

    @department.setter
    def department(self, val):
        self._prop_dict["department"] = val

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
    def given_name(self):
        """
        Gets and sets the givenName
        
        Returns:
            str:
                The givenName
        """
        if "givenName" in self._prop_dict:
            return self._prop_dict["givenName"]
        else:
            return None

    @given_name.setter
    def given_name(self, val):
        self._prop_dict["givenName"] = val

    @property
    def job_title(self):
        """
        Gets and sets the jobTitle
        
        Returns:
            str:
                The jobTitle
        """
        if "jobTitle" in self._prop_dict:
            return self._prop_dict["jobTitle"]
        else:
            return None

    @job_title.setter
    def job_title(self, val):
        self._prop_dict["jobTitle"] = val

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
    def mobile_phone(self):
        """
        Gets and sets the mobilePhone
        
        Returns:
            str:
                The mobilePhone
        """
        if "mobilePhone" in self._prop_dict:
            return self._prop_dict["mobilePhone"]
        else:
            return None

    @mobile_phone.setter
    def mobile_phone(self, val):
        self._prop_dict["mobilePhone"] = val

    @property
    def on_premises_immutable_id(self):
        """
        Gets and sets the onPremisesImmutableId
        
        Returns:
            str:
                The onPremisesImmutableId
        """
        if "onPremisesImmutableId" in self._prop_dict:
            return self._prop_dict["onPremisesImmutableId"]
        else:
            return None

    @on_premises_immutable_id.setter
    def on_premises_immutable_id(self, val):
        self._prop_dict["onPremisesImmutableId"] = val

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
    def password_policies(self):
        """
        Gets and sets the passwordPolicies
        
        Returns:
            str:
                The passwordPolicies
        """
        if "passwordPolicies" in self._prop_dict:
            return self._prop_dict["passwordPolicies"]
        else:
            return None

    @password_policies.setter
    def password_policies(self, val):
        self._prop_dict["passwordPolicies"] = val

    @property
    def password_profile(self):
        """
        Gets and sets the passwordProfile
        
        Returns: 
            :class:`PasswordProfile<microsoft.graph.model.password_profile.PasswordProfile>`:
                The passwordProfile
        """
        if "passwordProfile" in self._prop_dict:
            if isinstance(self._prop_dict["passwordProfile"], GraphObjectBase):
                return self._prop_dict["passwordProfile"]
            else:
                self._prop_dict["passwordProfile"] = PasswordProfile(self._prop_dict["passwordProfile"])
                return self._prop_dict["passwordProfile"]

        return None

    @password_profile.setter
    def password_profile(self, val):
        self._prop_dict["passwordProfile"] = val

    @property
    def office_location(self):
        """
        Gets and sets the officeLocation
        
        Returns:
            str:
                The officeLocation
        """
        if "officeLocation" in self._prop_dict:
            return self._prop_dict["officeLocation"]
        else:
            return None

    @office_location.setter
    def office_location(self, val):
        self._prop_dict["officeLocation"] = val

    @property
    def postal_code(self):
        """
        Gets and sets the postalCode
        
        Returns:
            str:
                The postalCode
        """
        if "postalCode" in self._prop_dict:
            return self._prop_dict["postalCode"]
        else:
            return None

    @postal_code.setter
    def postal_code(self, val):
        self._prop_dict["postalCode"] = val

    @property
    def preferred_language(self):
        """
        Gets and sets the preferredLanguage
        
        Returns:
            str:
                The preferredLanguage
        """
        if "preferredLanguage" in self._prop_dict:
            return self._prop_dict["preferredLanguage"]
        else:
            return None

    @preferred_language.setter
    def preferred_language(self, val):
        self._prop_dict["preferredLanguage"] = val

    @property
    def provisioned_plans(self):
        """Gets and sets the provisionedPlans
        
        Returns: 
            :class:`ProvisionedPlansCollectionPage<microsoft.graph.request.provisioned_plans_collection.ProvisionedPlansCollectionPage>`:
                The provisionedPlans
        """
        if "provisionedPlans" in self._prop_dict:
            return ProvisionedPlansCollectionPage(self._prop_dict["provisionedPlans"])
        else:
            return None

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
    def state(self):
        """
        Gets and sets the state
        
        Returns:
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def street_address(self):
        """
        Gets and sets the streetAddress
        
        Returns:
            str:
                The streetAddress
        """
        if "streetAddress" in self._prop_dict:
            return self._prop_dict["streetAddress"]
        else:
            return None

    @street_address.setter
    def street_address(self, val):
        self._prop_dict["streetAddress"] = val

    @property
    def surname(self):
        """
        Gets and sets the surname
        
        Returns:
            str:
                The surname
        """
        if "surname" in self._prop_dict:
            return self._prop_dict["surname"]
        else:
            return None

    @surname.setter
    def surname(self, val):
        self._prop_dict["surname"] = val

    @property
    def usage_location(self):
        """
        Gets and sets the usageLocation
        
        Returns:
            str:
                The usageLocation
        """
        if "usageLocation" in self._prop_dict:
            return self._prop_dict["usageLocation"]
        else:
            return None

    @usage_location.setter
    def usage_location(self, val):
        self._prop_dict["usageLocation"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def user_type(self):
        """
        Gets and sets the userType
        
        Returns:
            str:
                The userType
        """
        if "userType" in self._prop_dict:
            return self._prop_dict["userType"]
        else:
            return None

    @user_type.setter
    def user_type(self, val):
        self._prop_dict["userType"] = val

    @property
    def about_me(self):
        """
        Gets and sets the aboutMe
        
        Returns:
            str:
                The aboutMe
        """
        if "aboutMe" in self._prop_dict:
            return self._prop_dict["aboutMe"]
        else:
            return None

    @about_me.setter
    def about_me(self, val):
        self._prop_dict["aboutMe"] = val

    @property
    def birthday(self):
        """
        Gets and sets the birthday
        
        Returns:
            datetime:
                The birthday
        """
        if "birthday" in self._prop_dict:
            return datetime.strptime(self._prop_dict["birthday"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @birthday.setter
    def birthday(self, val):
        self._prop_dict["birthday"] = val.isoformat()+"Z"

    @property
    def hire_date(self):
        """
        Gets and sets the hireDate
        
        Returns:
            datetime:
                The hireDate
        """
        if "hireDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["hireDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @hire_date.setter
    def hire_date(self, val):
        self._prop_dict["hireDate"] = val.isoformat()+"Z"

    @property
    def interests(self):
        """
        Gets and sets the interests
        
        Returns:
            str:
                The interests
        """
        if "interests" in self._prop_dict:
            return self._prop_dict["interests"]
        else:
            return None

    @interests.setter
    def interests(self, val):
        self._prop_dict["interests"] = val

    @property
    def my_site(self):
        """
        Gets and sets the mySite
        
        Returns:
            str:
                The mySite
        """
        if "mySite" in self._prop_dict:
            return self._prop_dict["mySite"]
        else:
            return None

    @my_site.setter
    def my_site(self, val):
        self._prop_dict["mySite"] = val

    @property
    def past_projects(self):
        """
        Gets and sets the pastProjects
        
        Returns:
            str:
                The pastProjects
        """
        if "pastProjects" in self._prop_dict:
            return self._prop_dict["pastProjects"]
        else:
            return None

    @past_projects.setter
    def past_projects(self, val):
        self._prop_dict["pastProjects"] = val

    @property
    def preferred_name(self):
        """
        Gets and sets the preferredName
        
        Returns:
            str:
                The preferredName
        """
        if "preferredName" in self._prop_dict:
            return self._prop_dict["preferredName"]
        else:
            return None

    @preferred_name.setter
    def preferred_name(self, val):
        self._prop_dict["preferredName"] = val

    @property
    def responsibilities(self):
        """
        Gets and sets the responsibilities
        
        Returns:
            str:
                The responsibilities
        """
        if "responsibilities" in self._prop_dict:
            return self._prop_dict["responsibilities"]
        else:
            return None

    @responsibilities.setter
    def responsibilities(self, val):
        self._prop_dict["responsibilities"] = val

    @property
    def schools(self):
        """
        Gets and sets the schools
        
        Returns:
            str:
                The schools
        """
        if "schools" in self._prop_dict:
            return self._prop_dict["schools"]
        else:
            return None

    @schools.setter
    def schools(self, val):
        self._prop_dict["schools"] = val

    @property
    def skills(self):
        """
        Gets and sets the skills
        
        Returns:
            str:
                The skills
        """
        if "skills" in self._prop_dict:
            return self._prop_dict["skills"]
        else:
            return None

    @skills.setter
    def skills(self, val):
        self._prop_dict["skills"] = val

    @property
    def owned_devices(self):
        """Gets and sets the ownedDevices
        
        Returns: 
            :class:`OwnedDevicesCollectionPage<microsoft.graph.request.owned_devices_collection.OwnedDevicesCollectionPage>`:
                The ownedDevices
        """
        if "ownedDevices" in self._prop_dict:
            return OwnedDevicesCollectionPage(self._prop_dict["ownedDevices"])
        else:
            return None

    @property
    def registered_devices(self):
        """Gets and sets the registeredDevices
        
        Returns: 
            :class:`RegisteredDevicesCollectionPage<microsoft.graph.request.registered_devices_collection.RegisteredDevicesCollectionPage>`:
                The registeredDevices
        """
        if "registeredDevices" in self._prop_dict:
            return RegisteredDevicesCollectionPage(self._prop_dict["registeredDevices"])
        else:
            return None

    @property
    def manager(self):
        """
        Gets and sets the manager
        
        Returns: 
            :class:`DirectoryObject<microsoft.graph.model.directory_object.DirectoryObject>`:
                The manager
        """
        if "manager" in self._prop_dict:
            if isinstance(self._prop_dict["manager"], GraphObjectBase):
                return self._prop_dict["manager"]
            else:
                self._prop_dict["manager"] = DirectoryObject(self._prop_dict["manager"])
                return self._prop_dict["manager"]

        return None

    @manager.setter
    def manager(self, val):
        self._prop_dict["manager"] = val

    @property
    def direct_reports(self):
        """Gets and sets the directReports
        
        Returns: 
            :class:`DirectReportsCollectionPage<microsoft.graph.request.direct_reports_collection.DirectReportsCollectionPage>`:
                The directReports
        """
        if "directReports" in self._prop_dict:
            return DirectReportsCollectionPage(self._prop_dict["directReports"])
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
    def created_objects(self):
        """Gets and sets the createdObjects
        
        Returns: 
            :class:`CreatedObjectsCollectionPage<microsoft.graph.request.created_objects_collection.CreatedObjectsCollectionPage>`:
                The createdObjects
        """
        if "createdObjects" in self._prop_dict:
            return CreatedObjectsCollectionPage(self._prop_dict["createdObjects"])
        else:
            return None

    @property
    def owned_objects(self):
        """Gets and sets the ownedObjects
        
        Returns: 
            :class:`OwnedObjectsCollectionPage<microsoft.graph.request.owned_objects_collection.OwnedObjectsCollectionPage>`:
                The ownedObjects
        """
        if "ownedObjects" in self._prop_dict:
            return OwnedObjectsCollectionPage(self._prop_dict["ownedObjects"])
        else:
            return None

    @property
    def messages(self):
        """Gets and sets the messages
        
        Returns: 
            :class:`MessagesCollectionPage<microsoft.graph.request.messages_collection.MessagesCollectionPage>`:
                The messages
        """
        if "messages" in self._prop_dict:
            return MessagesCollectionPage(self._prop_dict["messages"])
        else:
            return None

    @property
    def mail_folders(self):
        """Gets and sets the mailFolders
        
        Returns: 
            :class:`MailFoldersCollectionPage<microsoft.graph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The mailFolders
        """
        if "mailFolders" in self._prop_dict:
            return MailFoldersCollectionPage(self._prop_dict["mailFolders"])
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
    def calendars(self):
        """Gets and sets the calendars
        
        Returns: 
            :class:`CalendarsCollectionPage<microsoft.graph.request.calendars_collection.CalendarsCollectionPage>`:
                The calendars
        """
        if "calendars" in self._prop_dict:
            return CalendarsCollectionPage(self._prop_dict["calendars"])
        else:
            return None

    @property
    def calendar_groups(self):
        """Gets and sets the calendarGroups
        
        Returns: 
            :class:`CalendarGroupsCollectionPage<microsoft.graph.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The calendarGroups
        """
        if "calendarGroups" in self._prop_dict:
            return CalendarGroupsCollectionPage(self._prop_dict["calendarGroups"])
        else:
            return None

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
    def contacts(self):
        """Gets and sets the contacts
        
        Returns: 
            :class:`ContactsCollectionPage<microsoft.graph.request.contacts_collection.ContactsCollectionPage>`:
                The contacts
        """
        if "contacts" in self._prop_dict:
            return ContactsCollectionPage(self._prop_dict["contacts"])
        else:
            return None

    @property
    def contact_folders(self):
        """Gets and sets the contactFolders
        
        Returns: 
            :class:`ContactFoldersCollectionPage<microsoft.graph.request.contact_folders_collection.ContactFoldersCollectionPage>`:
                The contactFolders
        """
        if "contactFolders" in self._prop_dict:
            return ContactFoldersCollectionPage(self._prop_dict["contactFolders"])
        else:
            return None

    @property
    def inference_classification(self):
        """
        Gets and sets the inferenceClassification
        
        Returns: 
            :class:`InferenceClassification<microsoft.graph.model.inference_classification.InferenceClassification>`:
                The inferenceClassification
        """
        if "inferenceClassification" in self._prop_dict:
            if isinstance(self._prop_dict["inferenceClassification"], GraphObjectBase):
                return self._prop_dict["inferenceClassification"]
            else:
                self._prop_dict["inferenceClassification"] = InferenceClassification(self._prop_dict["inferenceClassification"])
                return self._prop_dict["inferenceClassification"]

        return None

    @inference_classification.setter
    def inference_classification(self, val):
        self._prop_dict["inferenceClassification"] = val

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

