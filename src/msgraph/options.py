"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""


class Option(object):

    def __init__(self, key, value):
        """Initialize the Option, used for passing
        options into requests

        Args:
            key (str): The key for the option
            value (str): The value for the option

        """
        self._key = key
        self._value = value

    @property
    def key(self):
        """Gets and sets the key of the :class:`Option`

        Returns:
            str: The key"""
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        """Gets and sets the value of the :class:`Option`

        Returns:
            str: The value"""
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class QueryOption(Option):
    """Option used for the query string of a request"""
    pass


class HeaderOption(Option):
    """Option used for the header of the request"""
    pass
