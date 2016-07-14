# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from datetime import datetime

from .directory_object import DirectoryObject

class Organization(DirectoryObject):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def country_letter_code(self):
        """
        Gets and sets the countryLetterCode
        
        Returns:
            str:
                The countryLetterCode
        """
        if "countryLetterCode" in self._prop_dict:
            return self._prop_dict["countryLetterCode"]
        else:
            return None

    @country_letter_code.setter
    def country_letter_code(self, val):
        self._prop_dict["countryLetterCode"] = val

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
    def marketing_notification_emails(self):
        """
        Gets and sets the marketingNotificationEmails
        
        Returns:
            str:
                The marketingNotificationEmails
        """
        if "marketingNotificationEmails" in self._prop_dict:
            return self._prop_dict["marketingNotificationEmails"]
        else:
            return None

    @marketing_notification_emails.setter
    def marketing_notification_emails(self, val):
        self._prop_dict["marketingNotificationEmails"] = val

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
    def security_compliance_notification_mails(self):
        """
        Gets and sets the securityComplianceNotificationMails
        
        Returns:
            str:
                The securityComplianceNotificationMails
        """
        if "securityComplianceNotificationMails" in self._prop_dict:
            return self._prop_dict["securityComplianceNotificationMails"]
        else:
            return None

    @security_compliance_notification_mails.setter
    def security_compliance_notification_mails(self, val):
        self._prop_dict["securityComplianceNotificationMails"] = val

    @property
    def security_compliance_notification_phones(self):
        """
        Gets and sets the securityComplianceNotificationPhones
        
        Returns:
            str:
                The securityComplianceNotificationPhones
        """
        if "securityComplianceNotificationPhones" in self._prop_dict:
            return self._prop_dict["securityComplianceNotificationPhones"]
        else:
            return None

    @security_compliance_notification_phones.setter
    def security_compliance_notification_phones(self, val):
        self._prop_dict["securityComplianceNotificationPhones"] = val

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
    def street(self):
        """
        Gets and sets the street
        
        Returns:
            str:
                The street
        """
        if "street" in self._prop_dict:
            return self._prop_dict["street"]
        else:
            return None

    @street.setter
    def street(self, val):
        self._prop_dict["street"] = val

    @property
    def technical_notification_mails(self):
        """
        Gets and sets the technicalNotificationMails
        
        Returns:
            str:
                The technicalNotificationMails
        """
        if "technicalNotificationMails" in self._prop_dict:
            return self._prop_dict["technicalNotificationMails"]
        else:
            return None

    @technical_notification_mails.setter
    def technical_notification_mails(self, val):
        self._prop_dict["technicalNotificationMails"] = val

    @property
    def verified_domains(self):
        """Gets and sets the verifiedDomains
        
        Returns: 
            :class:`VerifiedDomainsCollectionPage<microsoft.graph.request.verified_domains_collection.VerifiedDomainsCollectionPage>`:
                The verifiedDomains
        """
        if "verifiedDomains" in self._prop_dict:
            return VerifiedDomainsCollectionPage(self._prop_dict["verifiedDomains"])
        else:
            return None

