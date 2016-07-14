"""
Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
"""

import abc


class SessionBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self,
                 token_type,
                 expires_in,
                 scope_string,
                 access_token,
                 client_id,
                 auth_server_url,
                 redirect_uri,
                 refresh_token=None,
                 client_secret=None):
        pass
    
    @abc.abstractmethod
    def is_expired(self):
        pass

    @abc.abstractmethod
    def refresh_session(self, expires_in, scope_string, access_token, refresh_token):
        pass
    
    @abc.abstractmethod
    def save_session(self, **save_session_kwargs):
        """Save the current session.
        IMPORTANT: This implementation should only be used for debugging.
        For real applications, the Session object should be subclassed and
        both save_session() and load_session() should be overwritten using
        the client system's correct mechanism (keychain, database, etc.).
        Remember, the access_token should be treated the same as a password.

        Args:
            save_session_kwargs (dicr): To be used by implementation
            of save_session, however save_session wants to use them. The
            default implementation (this one) takes a relative or absolute
            file path for pickle save location, under the name "path"
        """
        pass
    
    @abc.abstractmethod
    def load_session(**load_session_kwargs):
        """Save the current session.
        IMPORTANT: This implementation should only be used for debugging.
        For real applications, the Session object should be subclassed and
        both save_session() and load_session() should be overwritten using
        the client system's correct mechanism (keychain, database, etc.).
        Remember, the access_token should be treated the same as a password.

        Args:
            load_session_kwargs (dict): To be used by implementation
            of load_session, however load_session wants to use them. The
            default implementation (this one) takes a relative or absolute
            file path for pickle save location, under the name "path"

        Returns:
            :class:`Session`: The loaded session
        """
        pass
