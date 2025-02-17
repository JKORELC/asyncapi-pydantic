"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#securitySchemeObject
"""

from typing import Literal


from pydantic import (
    Field,
    field_validator,
)


from asyncapi.base import AsyncApiBase


SecurityTypes = Literal[
    "userPassword",
    "apiKey",
    "X509",
    "symmetricEncryption",
    "asymmetricEncryption",
    "httpApiKey",
    "http",
    "oauth2",
    "openIdConnect",
    "plain",
    "scramSha256",
    "scramSha512",
    "gssapi",
]


class OAuthFlow(AsyncApiBase):
    """
    OAuth Flow class.
    """

    authorization_url: str
    token_url: str
    refresh_url: str | None = Field(None)
    available_scopes: str


class OAuthFlows(AsyncApiBase):
    """
    OAuth Flows class.
    """

    implicit: OAuthFlow
    password: OAuthFlow
    client_credentials: OAuthFlow
    authorization_code: OAuthFlow


class SecurityScheme(AsyncApiBase):
    """
    Security Scheme class.
    """

    type_: str
    description: str
    name: str
    in_: str
    scheme: str
    bearer_format: str | None
    flows: OAuthFlows
    open_id_connect_url: str
    scopes: list[str]

    @field_validator("type_")
    def check_type(self, value: str) -> str:
        """
        Validate security types.
        """

        if value not in SecurityTypes:
            raise ValueError(f"Invalid security type: {value}")

        return value
