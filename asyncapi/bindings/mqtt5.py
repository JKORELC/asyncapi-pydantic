"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/mqtt5
"""

from pydantic import (
    Field,
)

from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiExtendable,
    Schema,
    Reference,
)


CURRENT_VERSION: str = "0.2.0"


class ChannelBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


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
    session_expiry_interval: int | Schema | Reference | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class Mqtt5Binding(AsyncApiExtendable):
    channel: ChannelBinding
    message: MessageBinding
    operation: OperationBinding
    server: ServerBinding
