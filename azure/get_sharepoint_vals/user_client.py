import datetime
import json
import logging
import user_auth
from typing import Callable, Optional, Union
import O365
from O365.utils import BaseTokenBackend


class ClientCredentials:  # pylint: disable=too-few-public-methods
    """Class to encapsulate client credentials for the MS Graph API"""

    def __init__(
        self,
        client_id: str,
        client_secret: Optional[str] = None,
        tenant_id: str = 'common',
        auth_flow_type: str = 'authorization',
    ) -> None:
        """Encapsulates client credentials for the MS Graph API

        Args:
            client_id (str): The client_id for the app.
            client_secret (Optional[str], optional): The client_secret for the app. Required unless
            using "public" or "password" for `auth_flow_type`. Defaults to None.
            tenant_id (str, optional): The id of the Office 365 environment. Required for most types
            of auth. Defaults to 'common'.
            auth_flow_type (str, optional): The auth method flow style used. Options:
            - 'authorization': 2 step web style grant flow using an authentication url.
            - 'public': 2 step web style grant flow using an authentication url for public apps
            where client secret cannot be secured.
            - 'credentials': also called client credentials grant flow using only the client id and
            secret
            - 'certificate': like credentials, but using the client id and a JWT assertion (obtained
            from a certificate)
            - 'password': legacy authentication using the client id and the user's username &
            password
            Defaults to 'authorization'.

        Raises:
            ValueError: When an invalid `auth_flow_type` is provided.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.auth_flow_type = auth_flow_type

        if auth_flow_type not in (
            "authorization",
            "public",
            "password",
            "certificate",
            "credentials",
        ):
            raise ValueError(
                '"auth_flow_type" must be "authorization", "public", "password", "certificate" or '
                '"credentials"'
            )

    @property
    def credentials(self) -> Union[tuple[str], tuple[str, str]]:
        """Get the credentials in the format required by O365.Account.

        Raises:
            ValueError: When "client_secret" is required for the auth_flow_type but not provided.

        Returns:
            Union[tuple[str], tuple[str, str]]: credentials in the format required by O365.Account
        """
        if self.auth_flow_type in ('public', 'password'):
            return (self.client_id,)
        if self.client_secret is not None:
            return (self.client_id, self.client_secret)

        raise ValueError(
            f'"client_secret" is required for the auth_flow_type "{self.auth_flow_type}"'
        )


class UserClient(O365.Account):
    def __init__(
        self,
        client_credentials: ClientCredentials,
        token_backend: BaseTokenBackend,
        *,
        use_office365_protocol: bool = False,
        timezone: Union[None, str, datetime.tzinfo] = None,
        main_resource: Optional[str] = None,
        protocol: Optional[O365.Protocol] = None,
        **kwargs,
    ) -> None:
        self.client_credentials = client_credentials

        if protocol is None and use_office365_protocol:
            protocol = O365.MSOffice365Protocol(
                default_resource=main_resource, timezone=timezone)

        super().__init__(
            credentials=client_credentials.credentials,
            protocol=protocol,
            main_resource=main_resource,
            auth_flow_type=client_credentials.auth_flow_type,
            token_backend=token_backend,
            tenant_id=client_credentials.tenant_id,
            **kwargs,
        )

    def authenticate(  # pylint: disable=arguments-differ
        self,
        scopes: Optional[list[str]] = None,
        handle_consent: Callable[[str], str] = user_auth.cli_input,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> bool:
        """Performs the oauth authentication flow in a stored token.

        Args:
            scopes (Optional[list[str]], optional): list of OAuth scopes to request. Defaults to
            the protocol's `.default` scope (all scopes already granted by the user or admin to the
            app) and "offline_access" when `auth_flow_type` is 'authorization' or 'public';
            otherwise None.
            handle_consent (Callable[[str], str], optional): A function to handle the OAuth consent,
            it must accept an authorization url and return a token url. Defaults to `cli_input`
            which provides the authorization url via the console and expects the user to provide the
            token url in response.
            username (Optional[str], optional): Fully qualified username of the user to
            authenticate. Only used for "password" auth_flow_type. Defaults to None.
            password (Optional[str], optional): Password of the user to authenticate. Only used for
            "password" auth_flow_type. Defaults to None.

        Returns:
            bool: Success / Failure
        """
        if self.con.auth_flow_type == 'password':
            self.con.username = username
            self.con.password = password
            return self.con.request_token(None, requested_scopes=scopes)
        if self.con.auth_flow_type in ('credentials', 'certificate'):
            return self.con.request_token(None, requested_scopes=scopes)
        if self.con.auth_flow_type in ('authorization', 'public'):
            if scopes is None:
                scopes = ["offline_access",
                          self.protocol.prefix_scope(".default")]
            self.con.scopes = self.protocol.get_scopes_for(scopes)

            consent_url, _ = self.con.get_authorization_url()

            token_url = handle_consent(consent_url)

            if not token_url:
                logging.error("Authentication Flow aborted.")
                return False

            return self.con.request_token(token_url)

        raise ValueError("Unhandled 'auth_flow_type'.")

    def get_rclone_config(self, drive_type: str, drive_id: str) -> dict:
        """Gets the MS Graph API configuration & token for use with Rclone.

        Args:
            drive_type (str): The type of the drive to connect to ("personal", "business", or
            "documentLibrary")
            drive_id (str): The ID of the drive to use.

        Returns:
            dict: Rclone remote config
        """
        tenat_id = self.client_credentials.tenant_id

        return {
            "type": "onedrive",
            "client_id": self.client_credentials.client_id,
            "client_secret": self.client_credentials.client_secret,
            "token": json.dumps(self.con.token_backend.get_token()),
            "auth_url": f"https://login.microsoftonline.com/{tenat_id}/oauth2/v2.0/authorize",
            "token_url": f"https://login.microsoftonline.com/{tenat_id}/oauth2/v2.0/token",
            "drive_type": drive_type,
            "drive_id": drive_id,
        }
