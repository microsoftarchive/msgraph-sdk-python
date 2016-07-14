"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

from __future__ import unicode_literals


class GraphError(Exception):

    def __init__(self, prop_dict, status_code):
        """Initialize a GraphError given the JSON
        error response dictionary, and the HTTP status code

        Args:
            prop_dict (dict): A dictionary containing the response
                from Graph
            status_code (int): The HTTP status code (ex. 200, 201, etc.)
        """
        if "code" not in prop_dict or "message" not in prop_dict:
            prop_dict["code"] = ErrorCode.Malformed.value
            prop_dict["message"] = "The received response was malformed"
            super(GraphError, self).__init__(prop_dict["code"] + " - " + prop_dict["message"])
        else:
            super(GraphError, self).__init__(prop_dict["code"] + " - " + prop_dict["message"])
        self._prop_dict = prop_dict
        self._status_code = status_code

    @property
    def status_code(self):
        """The HTTP status code

        Returns:
            int: The HTTP status code
        """
        return self._status_code

    @property
    def code(self):
        """The Graph error code sent back in
        the response. Possible codes can be found
        in the :class:`ErrorCode` enum.

        Returns:
            str: The error code
        """
        return self._prop_dict["code"]

    @property
    def inner_error(self):
        """Creates a GraphError object from the specified inner
        error within the response.

        Returns:
            :class:`GraphError`: Error from within the inner
                response
        """
        return GraphError(self._prop_dict["innererror"], self.status_code) if "innererror" in self._prop_dict else None

    def matches(self, code):
        """Recursively searches the :class:`GraphError` to find
        if the specified code was found

        Args:
            code (str): The error code to search for

        Returns:
            bool: True if the error code was found, false otherwise
        """
        if self.code == code:
            return True

        return False if self.inner_error is None else self.inner_error.matches(code)


class ErrorCode(object):
    #: Access was denied to the resource
    AccessDenied = "accessDenied"
    #: The activity limit has been reached
    ActivityLimitReached = "activityLimitReached"
    #: A general exception occured
    GeneralException = "generalException"
    #: An invalid range was provided
    InvalidRange = "invalidRange"
    #: An invalid request was provided
    InvalidRequest = "invalidRequest"
    #: The requested resource was not found
    ItemNotFound = "itemNotFound"
    #: Malware was detected in the resource
    MalwareDetected = "malwareDetected"
    #: The name already exists
    NameAlreadyExists = "nameAlreadyExists"
    #: The action was not allowed
    NotAllowed = "notAllowed"
    #: The action was not supported
    NotSupported = "notSupported"
    #: The resource was modified
    ResourceModified = "resourceModified"
    #: A resync is required
    ResyncRequired = "resyncRequired"
    #: The Graph service is not available
    ServiceNotAvailable = "serviceNotAvailable"
    #: The quota for this OneDrive has been reached
    QuotaLimitReached = "quotaLimitReached"
    #: The user is unauthenticated
    Unauthenticated = "unauthenticated"

    #: The response was malformed
    Malformed = "malformed"
