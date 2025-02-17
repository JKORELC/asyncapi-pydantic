"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/websockets
"""

from typing import Literal


from pydantic import Field


from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiExtendable,
    Schema,
    Reference,
)


CURRENT_VERSION: str = "0.1.0"


class ChannelBinding(Binding):
    """
    This object MUST contain only the properties defined below.
    """

    method: Literal["GET", "POST"]
    query: Schema | Reference | None = Field(None)
    headers: Schema | Reference | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """


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


class WebSocketBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
