# -*- coding: utf-8 -*-
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
#
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..graph_object_base import GraphObjectBase
from ..model.identity_set import IdentitySet
from ..model.item_reference import ItemReference
from ..model.audio import Audio
from ..model.deleted import Deleted
from ..model.file import File
from ..model.file_system_info import FileSystemInfo
from ..model.folder import Folder
from ..model.image import Image
from ..model.geo_coordinates import GeoCoordinates
from ..model.photo import Photo
from ..model.remote_item import RemoteItem
from ..model.search_result import SearchResult
from ..model.shared import Shared
from ..model.special_folder import SpecialFolder
from ..model.video import Video
from ..model.package import Package
from ..model.user import User
from datetime import datetime

from .entity import Entity

class DriveItem(Entity):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def created_by(self):
        """
        Gets and sets the createdBy

        Returns:
            :class:`IdentitySet<microsoft.graph.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], GraphObjectBase):
                return self._prop_dict["createdBy"]
            else:
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime

        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def c_tag(self):
        """
        Gets and sets the cTag

        Returns:
            str:
                The cTag
        """
        if "cTag" in self._prop_dict:
            return self._prop_dict["cTag"]
        else:
            return None

    @c_tag.setter
    def c_tag(self, val):
        self._prop_dict["cTag"] = val

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
    def e_tag(self):
        """
        Gets and sets the eTag

        Returns:
            str:
                The eTag
        """
        if "eTag" in self._prop_dict:
            return self._prop_dict["eTag"]
        else:
            return None

    @e_tag.setter
    def e_tag(self, val):
        self._prop_dict["eTag"] = val

    @property
    def last_modified_by(self):
        """
        Gets and sets the lastModifiedBy

        Returns:
            :class:`IdentitySet<microsoft.graph.model.identity_set.IdentitySet>`:
                The lastModifiedBy
        """
        if "lastModifiedBy" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedBy"], GraphObjectBase):
                return self._prop_dict["lastModifiedBy"]
            else:
                self._prop_dict["lastModifiedBy"] = IdentitySet(self._prop_dict["lastModifiedBy"])
                return self._prop_dict["lastModifiedBy"]

        return None

    @last_modified_by.setter
    def last_modified_by(self, val):
        self._prop_dict["lastModifiedBy"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime

        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def name(self):
        """
        Gets and sets the name

        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def parent_reference(self):
        """
        Gets and sets the parentReference

        Returns:
            :class:`ItemReference<microsoft.graph.model.item_reference.ItemReference>`:
                The parentReference
        """
        if "parentReference" in self._prop_dict:
            if isinstance(self._prop_dict["parentReference"], GraphObjectBase):
                return self._prop_dict["parentReference"]
            else:
                self._prop_dict["parentReference"] = ItemReference(self._prop_dict["parentReference"])
                return self._prop_dict["parentReference"]

        return None

    @parent_reference.setter
    def parent_reference(self, val):
        self._prop_dict["parentReference"] = val

    @property
    def size(self):
        """
        Gets and sets the size

        Returns:
            int:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

    @property
    def web_dav_url(self):
        """
        Gets and sets the webDavUrl

        Returns:
            str:
                The webDavUrl
        """
        if "webDavUrl" in self._prop_dict:
            return self._prop_dict["webDavUrl"]
        else:
            return None

    @web_dav_url.setter
    def web_dav_url(self, val):
        self._prop_dict["webDavUrl"] = val

    @property
    def web_url(self):
        """
        Gets and sets the webUrl

        Returns:
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

    @property
    def audio(self):
        """
        Gets and sets the audio

        Returns:
            :class:`Audio<microsoft.graph.model.audio.Audio>`:
                The audio
        """
        if "audio" in self._prop_dict:
            if isinstance(self._prop_dict["audio"], GraphObjectBase):
                return self._prop_dict["audio"]
            else:
                self._prop_dict["audio"] = Audio(self._prop_dict["audio"])
                return self._prop_dict["audio"]

        return None

    @audio.setter
    def audio(self, val):
        self._prop_dict["audio"] = val

    @property
    def deleted(self):
        """
        Gets and sets the deleted

        Returns:
            :class:`Deleted<microsoft.graph.model.deleted.Deleted>`:
                The deleted
        """
        if "deleted" in self._prop_dict:
            if isinstance(self._prop_dict["deleted"], GraphObjectBase):
                return self._prop_dict["deleted"]
            else:
                self._prop_dict["deleted"] = Deleted(self._prop_dict["deleted"])
                return self._prop_dict["deleted"]

        return None

    @deleted.setter
    def deleted(self, val):
        self._prop_dict["deleted"] = val

    @property
    def file(self):
        """
        Gets and sets the file

        Returns:
            :class:`File<microsoft.graph.model.file.File>`:
                The file
        """
        if "file" in self._prop_dict:
            if isinstance(self._prop_dict["file"], GraphObjectBase):
                return self._prop_dict["file"]
            else:
                self._prop_dict["file"] = File(self._prop_dict["file"])
                return self._prop_dict["file"]

        return None

    @file.setter
    def file(self, val):
        self._prop_dict["file"] = val

    @property
    def file_system_info(self):
        """
        Gets and sets the fileSystemInfo

        Returns:
            :class:`FileSystemInfo<microsoft.graph.model.file_system_info.FileSystemInfo>`:
                The fileSystemInfo
        """
        if "fileSystemInfo" in self._prop_dict:
            if isinstance(self._prop_dict["fileSystemInfo"], GraphObjectBase):
                return self._prop_dict["fileSystemInfo"]
            else:
                self._prop_dict["fileSystemInfo"] = FileSystemInfo(self._prop_dict["fileSystemInfo"])
                return self._prop_dict["fileSystemInfo"]

        return None

    @file_system_info.setter
    def file_system_info(self, val):
        self._prop_dict["fileSystemInfo"] = val

    @property
    def folder(self):
        """
        Gets and sets the folder

        Returns:
            :class:`Folder<microsoft.graph.model.folder.Folder>`:
                The folder
        """
        if "folder" in self._prop_dict:
            if isinstance(self._prop_dict["folder"], GraphObjectBase):
                return self._prop_dict["folder"]
            else:
                self._prop_dict["folder"] = Folder(self._prop_dict["folder"])
                return self._prop_dict["folder"]

        return None

    @folder.setter
    def folder(self, val):
        self._prop_dict["folder"] = val

    @property
    def image(self):
        """
        Gets and sets the image

        Returns:
            :class:`Image<microsoft.graph.model.image.Image>`:
                The image
        """
        if "image" in self._prop_dict:
            if isinstance(self._prop_dict["image"], GraphObjectBase):
                return self._prop_dict["image"]
            else:
                self._prop_dict["image"] = Image(self._prop_dict["image"])
                return self._prop_dict["image"]

        return None

    @image.setter
    def image(self, val):
        self._prop_dict["image"] = val

    @property
    def location(self):
        """
        Gets and sets the location

        Returns:
            :class:`GeoCoordinates<microsoft.graph.model.geo_coordinates.GeoCoordinates>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], GraphObjectBase):
                return self._prop_dict["location"]
            else:
                self._prop_dict["location"] = GeoCoordinates(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def photo(self):
        """
        Gets and sets the photo

        Returns:
            :class:`Photo<microsoft.graph.model.photo.Photo>`:
                The photo
        """
        if "photo" in self._prop_dict:
            if isinstance(self._prop_dict["photo"], GraphObjectBase):
                return self._prop_dict["photo"]
            else:
                self._prop_dict["photo"] = Photo(self._prop_dict["photo"])
                return self._prop_dict["photo"]

        return None

    @photo.setter
    def photo(self, val):
        self._prop_dict["photo"] = val

    @property
    def remote_item(self):
        """
        Gets and sets the remoteItem

        Returns:
            :class:`RemoteItem<microsoft.graph.model.remote_item.RemoteItem>`:
                The remoteItem
        """
        if "remoteItem" in self._prop_dict:
            if isinstance(self._prop_dict["remoteItem"], GraphObjectBase):
                return self._prop_dict["remoteItem"]
            else:
                self._prop_dict["remoteItem"] = RemoteItem(self._prop_dict["remoteItem"])
                return self._prop_dict["remoteItem"]

        return None

    @remote_item.setter
    def remote_item(self, val):
        self._prop_dict["remoteItem"] = val

    @property
    def search_result(self):
        """
        Gets and sets the searchResult

        Returns:
            :class:`SearchResult<microsoft.graph.model.search_result.SearchResult>`:
                The searchResult
        """
        if "searchResult" in self._prop_dict:
            if isinstance(self._prop_dict["searchResult"], GraphObjectBase):
                return self._prop_dict["searchResult"]
            else:
                self._prop_dict["searchResult"] = SearchResult(self._prop_dict["searchResult"])
                return self._prop_dict["searchResult"]

        return None

    @search_result.setter
    def search_result(self, val):
        self._prop_dict["searchResult"] = val

    @property
    def shared(self):
        """
        Gets and sets the shared

        Returns:
            :class:`Shared<microsoft.graph.model.shared.Shared>`:
                The shared
        """
        if "shared" in self._prop_dict:
            if isinstance(self._prop_dict["shared"], GraphObjectBase):
                return self._prop_dict["shared"]
            else:
                self._prop_dict["shared"] = Shared(self._prop_dict["shared"])
                return self._prop_dict["shared"]

        return None

    @shared.setter
    def shared(self, val):
        self._prop_dict["shared"] = val

    @property
    def special_folder(self):
        """
        Gets and sets the specialFolder

        Returns:
            :class:`SpecialFolder<microsoft.graph.model.special_folder.SpecialFolder>`:
                The specialFolder
        """
        if "specialFolder" in self._prop_dict:
            if isinstance(self._prop_dict["specialFolder"], GraphObjectBase):
                return self._prop_dict["specialFolder"]
            else:
                self._prop_dict["specialFolder"] = SpecialFolder(self._prop_dict["specialFolder"])
                return self._prop_dict["specialFolder"]

        return None

    @special_folder.setter
    def special_folder(self, val):
        self._prop_dict["specialFolder"] = val

    @property
    def video(self):
        """
        Gets and sets the video

        Returns:
            :class:`Video<microsoft.graph.model.video.Video>`:
                The video
        """
        if "video" in self._prop_dict:
            if isinstance(self._prop_dict["video"], GraphObjectBase):
                return self._prop_dict["video"]
            else:
                self._prop_dict["video"] = Video(self._prop_dict["video"])
                return self._prop_dict["video"]

        return None

    @video.setter
    def video(self, val):
        self._prop_dict["video"] = val

    @property
    def package(self):
        """
        Gets and sets the package

        Returns:
            :class:`Package<microsoft.graph.model.package.Package>`:
                The package
        """
        if "package" in self._prop_dict:
            if isinstance(self._prop_dict["package"], GraphObjectBase):
                return self._prop_dict["package"]
            else:
                self._prop_dict["package"] = Package(self._prop_dict["package"])
                return self._prop_dict["package"]

        return None

    @package.setter
    def package(self, val):
        self._prop_dict["package"] = val

    @property
    def created_by_user(self):
        """
        Gets and sets the createdByUser

        Returns:
            :class:`User<microsoft.graph.model.user.User>`:
                The createdByUser
        """
        if "createdByUser" in self._prop_dict:
            if isinstance(self._prop_dict["createdByUser"], GraphObjectBase):
                return self._prop_dict["createdByUser"]
            else:
                self._prop_dict["createdByUser"] = User(self._prop_dict["createdByUser"])
                return self._prop_dict["createdByUser"]

        return None

    @created_by_user.setter
    def created_by_user(self, val):
        self._prop_dict["createdByUser"] = val

    @property
    def last_modified_by_user(self):
        """
        Gets and sets the lastModifiedByUser

        Returns:
            :class:`User<microsoft.graph.model.user.User>`:
                The lastModifiedByUser
        """
        if "lastModifiedByUser" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedByUser"], GraphObjectBase):
                return self._prop_dict["lastModifiedByUser"]
            else:
                self._prop_dict["lastModifiedByUser"] = User(self._prop_dict["lastModifiedByUser"])
                return self._prop_dict["lastModifiedByUser"]

        return None

    @last_modified_by_user.setter
    def last_modified_by_user(self, val):
        self._prop_dict["lastModifiedByUser"] = val

    @property
    def permissions(self):
        """Gets and sets the permissions

        Returns:
            :class:`PermissionsCollectionPage<microsoft.graph.request.permissions_collection.PermissionsCollectionPage>`:
                The permissions
        """
        if "permissions" in self._prop_dict:
            return PermissionsCollectionPage(self._prop_dict["permissions"])
        else:
            return None

    @property
    def children(self):
        """Gets and sets the children

        Returns:
            :class:`ChildrenCollectionPage<microsoft.graph.request.children_collection.ChildrenCollectionPage>`:
                The children
        """
        if "children" in self._prop_dict:
            return ChildrenCollectionPage(self._prop_dict["children"])
        else:
            return None

    @property
    def thumbnails(self):
        """Gets and sets the thumbnails

        Returns:
            :class:`ThumbnailsCollectionPage<microsoft.graph.request.thumbnails_collection.ThumbnailsCollectionPage>`:
                The thumbnails
        """
        if "thumbnails" in self._prop_dict:
            return ThumbnailsCollectionPage(self._prop_dict["thumbnails"])
        else:
            return None

