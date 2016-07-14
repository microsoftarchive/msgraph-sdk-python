# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..model.physical_address import PhysicalAddress
from datetime import datetime

from .outlook_item import OutlookItem

class Contact(OutlookItem):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def file_as(self):
        """
        Gets and sets the fileAs
        
        Returns:
            str:
                The fileAs
        """
        if "fileAs" in self._prop_dict:
            return self._prop_dict["fileAs"]
        else:
            return None

    @file_as.setter
    def file_as(self, val):
        self._prop_dict["fileAs"] = val

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
    def initials(self):
        """
        Gets and sets the initials
        
        Returns:
            str:
                The initials
        """
        if "initials" in self._prop_dict:
            return self._prop_dict["initials"]
        else:
            return None

    @initials.setter
    def initials(self, val):
        self._prop_dict["initials"] = val

    @property
    def middle_name(self):
        """
        Gets and sets the middleName
        
        Returns:
            str:
                The middleName
        """
        if "middleName" in self._prop_dict:
            return self._prop_dict["middleName"]
        else:
            return None

    @middle_name.setter
    def middle_name(self, val):
        self._prop_dict["middleName"] = val

    @property
    def nick_name(self):
        """
        Gets and sets the nickName
        
        Returns:
            str:
                The nickName
        """
        if "nickName" in self._prop_dict:
            return self._prop_dict["nickName"]
        else:
            return None

    @nick_name.setter
    def nick_name(self, val):
        self._prop_dict["nickName"] = val

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
    def title(self):
        """
        Gets and sets the title
        
        Returns:
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def yomi_given_name(self):
        """
        Gets and sets the yomiGivenName
        
        Returns:
            str:
                The yomiGivenName
        """
        if "yomiGivenName" in self._prop_dict:
            return self._prop_dict["yomiGivenName"]
        else:
            return None

    @yomi_given_name.setter
    def yomi_given_name(self, val):
        self._prop_dict["yomiGivenName"] = val

    @property
    def yomi_surname(self):
        """
        Gets and sets the yomiSurname
        
        Returns:
            str:
                The yomiSurname
        """
        if "yomiSurname" in self._prop_dict:
            return self._prop_dict["yomiSurname"]
        else:
            return None

    @yomi_surname.setter
    def yomi_surname(self, val):
        self._prop_dict["yomiSurname"] = val

    @property
    def yomi_company_name(self):
        """
        Gets and sets the yomiCompanyName
        
        Returns:
            str:
                The yomiCompanyName
        """
        if "yomiCompanyName" in self._prop_dict:
            return self._prop_dict["yomiCompanyName"]
        else:
            return None

    @yomi_company_name.setter
    def yomi_company_name(self, val):
        self._prop_dict["yomiCompanyName"] = val

    @property
    def generation(self):
        """
        Gets and sets the generation
        
        Returns:
            str:
                The generation
        """
        if "generation" in self._prop_dict:
            return self._prop_dict["generation"]
        else:
            return None

    @generation.setter
    def generation(self, val):
        self._prop_dict["generation"] = val

    @property
    def email_addresses(self):
        """Gets and sets the emailAddresses
        
        Returns: 
            :class:`EmailAddressesCollectionPage<microsoft.graph.request.email_addresses_collection.EmailAddressesCollectionPage>`:
                The emailAddresses
        """
        if "emailAddresses" in self._prop_dict:
            return EmailAddressesCollectionPage(self._prop_dict["emailAddresses"])
        else:
            return None

    @property
    def im_addresses(self):
        """
        Gets and sets the imAddresses
        
        Returns:
            str:
                The imAddresses
        """
        if "imAddresses" in self._prop_dict:
            return self._prop_dict["imAddresses"]
        else:
            return None

    @im_addresses.setter
    def im_addresses(self, val):
        self._prop_dict["imAddresses"] = val

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
    def profession(self):
        """
        Gets and sets the profession
        
        Returns:
            str:
                The profession
        """
        if "profession" in self._prop_dict:
            return self._prop_dict["profession"]
        else:
            return None

    @profession.setter
    def profession(self, val):
        self._prop_dict["profession"] = val

    @property
    def business_home_page(self):
        """
        Gets and sets the businessHomePage
        
        Returns:
            str:
                The businessHomePage
        """
        if "businessHomePage" in self._prop_dict:
            return self._prop_dict["businessHomePage"]
        else:
            return None

    @business_home_page.setter
    def business_home_page(self, val):
        self._prop_dict["businessHomePage"] = val

    @property
    def assistant_name(self):
        """
        Gets and sets the assistantName
        
        Returns:
            str:
                The assistantName
        """
        if "assistantName" in self._prop_dict:
            return self._prop_dict["assistantName"]
        else:
            return None

    @assistant_name.setter
    def assistant_name(self, val):
        self._prop_dict["assistantName"] = val

    @property
    def manager(self):
        """
        Gets and sets the manager
        
        Returns:
            str:
                The manager
        """
        if "manager" in self._prop_dict:
            return self._prop_dict["manager"]
        else:
            return None

    @manager.setter
    def manager(self, val):
        self._prop_dict["manager"] = val

    @property
    def home_phones(self):
        """
        Gets and sets the homePhones
        
        Returns:
            str:
                The homePhones
        """
        if "homePhones" in self._prop_dict:
            return self._prop_dict["homePhones"]
        else:
            return None

    @home_phones.setter
    def home_phones(self, val):
        self._prop_dict["homePhones"] = val

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
    def home_address(self):
        """
        Gets and sets the homeAddress
        
        Returns: 
            :class:`PhysicalAddress<microsoft.graph.model.physical_address.PhysicalAddress>`:
                The homeAddress
        """
        if "homeAddress" in self._prop_dict:
            if isinstance(self._prop_dict["homeAddress"], GraphObjectBase):
                return self._prop_dict["homeAddress"]
            else:
                self._prop_dict["homeAddress"] = PhysicalAddress(self._prop_dict["homeAddress"])
                return self._prop_dict["homeAddress"]

        return None

    @home_address.setter
    def home_address(self, val):
        self._prop_dict["homeAddress"] = val

    @property
    def business_address(self):
        """
        Gets and sets the businessAddress
        
        Returns: 
            :class:`PhysicalAddress<microsoft.graph.model.physical_address.PhysicalAddress>`:
                The businessAddress
        """
        if "businessAddress" in self._prop_dict:
            if isinstance(self._prop_dict["businessAddress"], GraphObjectBase):
                return self._prop_dict["businessAddress"]
            else:
                self._prop_dict["businessAddress"] = PhysicalAddress(self._prop_dict["businessAddress"])
                return self._prop_dict["businessAddress"]

        return None

    @business_address.setter
    def business_address(self, val):
        self._prop_dict["businessAddress"] = val

    @property
    def other_address(self):
        """
        Gets and sets the otherAddress
        
        Returns: 
            :class:`PhysicalAddress<microsoft.graph.model.physical_address.PhysicalAddress>`:
                The otherAddress
        """
        if "otherAddress" in self._prop_dict:
            if isinstance(self._prop_dict["otherAddress"], GraphObjectBase):
                return self._prop_dict["otherAddress"]
            else:
                self._prop_dict["otherAddress"] = PhysicalAddress(self._prop_dict["otherAddress"])
                return self._prop_dict["otherAddress"]

        return None

    @other_address.setter
    def other_address(self, val):
        self._prop_dict["otherAddress"] = val

    @property
    def spouse_name(self):
        """
        Gets and sets the spouseName
        
        Returns:
            str:
                The spouseName
        """
        if "spouseName" in self._prop_dict:
            return self._prop_dict["spouseName"]
        else:
            return None

    @spouse_name.setter
    def spouse_name(self, val):
        self._prop_dict["spouseName"] = val

    @property
    def personal_notes(self):
        """
        Gets and sets the personalNotes
        
        Returns:
            str:
                The personalNotes
        """
        if "personalNotes" in self._prop_dict:
            return self._prop_dict["personalNotes"]
        else:
            return None

    @personal_notes.setter
    def personal_notes(self, val):
        self._prop_dict["personalNotes"] = val

    @property
    def children(self):
        """
        Gets and sets the children
        
        Returns:
            str:
                The children
        """
        if "children" in self._prop_dict:
            return self._prop_dict["children"]
        else:
            return None

    @children.setter
    def children(self, val):
        self._prop_dict["children"] = val

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

