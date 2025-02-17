"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/anypointmq
"""

from typing import (
    Any,
    Final,
    Literal,
    TypeAlias,
)

from pydantic import (
    BaseModel,
    Field,
    AnyUrl,
)

from asyncapi.common import Reference

from asyncapi.bindings.base import Binding
from asyncapi.common import AsyncApiExtendable


CURRENT_VERSION: str = "0.1.0"


__all__ = [
    "AnypointmqChannelBinding",
    "AnypointmqMessageBinding",
    "AnypointmqOperationBinding",
    "AnypointmqServerBinding",
]


AnypointmqChannelBinding: TypeAlias = "ChannelBinding"
AnypointmqMessageBinding: TypeAlias = "MessageBinding"
AnypointmqOperatorBinding: TypeAlias = "OperatorBinding"
AnypointmqServerBinding: TypeAlias = "ServerBinding"


# TODO: relocate and centralize
class ClientCredentials(BaseModel):
    token_url: AnyUrl
    scopes: dict[str, Any]


class SecuritySchemeFlows(BaseModel):
    client_credentials: ClientCredentials


class SecurityScheme(BaseModel):
    type: Literal["oauth2"]
    flows: SecuritySchemeFlows


# TODO: relocate and centralize


class Server(BaseModel, extra="forbid"):
    protocol: Final = "anypointmq"
    host: AnyUrl
    pathname: str
    protocol_version: str | None = Field("v1")
    security: (
        str | Reference
    )  # TODO: suitably configured OAuth 2.0 client credentials grant type


class ChannelBinding(Binding):
    destination: str | None = Field(None)
    destination_type: Literal["exchange", "queue", "fifo-queue"] | None = Field(None)
    binding_version: str = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class OperationBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class AnypointmqBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
