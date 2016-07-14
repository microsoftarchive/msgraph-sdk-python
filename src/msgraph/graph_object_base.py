"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""


class GraphObjectBase(object):

    def to_dict(self):
        """Returns the serialized form of the :class:`GraphObjectBase`
        as a dict. All sub-objects that are based off of :class:`GraphObjectBase`
        are also serialized and inserted into the dict
        
        Returns:
            dict: The serialized form of the :class:`GraphObjectBase`
        """
        serialized = {}

        for prop in self._prop_dict:
            if isinstance(self._prop_dict[prop], GraphObjectBase):
                serialized[prop] = self._prop_dict[prop].to_dict()
            else:
                serialized[prop] = self._prop_dict[prop]

        return serialized
