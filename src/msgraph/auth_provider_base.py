"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

import abc


class AuthProviderBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, http_provider, client_id, scopes, access_token):
        """Initialize the authentication provider for authenticating
        requests sent to Graph

        Args:
            http_provider (:class:`HttpProviderBase<microsoft.http_provider_base>`):
                The HTTP provider to use for all auth requests
            client_id (str): Defaults to None, the client id for your
                application
            scopes (list of str): Defaults to None, the scopes
                that are required for your application
            access_token (str): Defaults to None, the access token
                for your application
            session_type (:class:`SessionBase<microsoft.session_base.SessionBase>`):
                Defaults to :class:`Session<microsoft.session.Session>`,
                the implementation of SessionBase that stores your
                session. WARNING: THE DEFAULT IMPLEMENTATION ONLY
                STORES SESSIONS TO THE RUN DIRECTORY IN PLAIN TEXT.
                THIS IS UNSAFE. IT IS HIGHLY RECOMMENDED THAT YOU
                IMPLEMENT YOUR OWN VERSION.
            loop (BaseEventLoop): Defaults to None, the asyncio
                loop to use for all async requests. If none is provided,
                asyncio.new_event_loop() will be called. If using Python
                3.3 or below this does not need to be specified
        """
        pass

    @property
    def client_id(self):
        """Gets and sets the client_id for the
        AuthProvider

        Returns:
            str: The client id
        """
        pass

    @client_id.setter
    @abc.abstractmethod
    def client_id(self, value):
        pass

    @property
    def scopes(self):
        """Gets and sets the scopes for the
        AuthProvider

        Returns:
            list of str: The scopes
        """
        pass

    @scopes.setter
    @abc.abstractmethod
    def scopes(self, value):
        pass

    @property
    def access_token(self):
        """Gets and sets the access_token for the
        AuthProvider

        Returns:
            str: The access token
        """
        pass

    @access_token.setter
    @abc.abstractmethod
    def access_token(self, value):
        pass

    @abc.abstractmethod
    def get_auth_url(self, auth_server_url, redirect_uri):
        """Build the auth url using the params provided
        and the auth_provider

        Args:
            redirect_uri (str): The URI to redirect the response
                to
        """
        pass

    @abc.abstractmethod
    def authenticate(self, code, auth_server_url, redirect_uri, client_secret):
        """Takes in a code string, gets the access token,
        and creates session property bag

        Args:
            code (str):
                The code provided by the oauth provider
            redirect_uri (str): The URI to redirect the callback
                to
            client_secret (str): Defaults to None, the client
                secret of your app
        """
        pass

    @abc.abstractmethod
    def authenticate_request(self, request):
        """Append the required authentication headers
        to the specified request. This will only function
        if a session has been successfully created using
        :func:`authenticate`. This will also refresh the
        authentication token if necessary.

        Args:
            request (:class:`RequestBase<microsoft.request_base.RequestBase>`):
                The request to authenticate
        """
        pass

    @abc.abstractmethod
    def refresh_token(self):
        """Refresh the token currently used by the session"""
        pass
