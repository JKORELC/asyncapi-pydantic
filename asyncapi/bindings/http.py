"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/http
"""

from typing import Literal

from pydantic import Field

from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiExtendable,
    Schema,
    Reference,
)


CURRENT_VERSION: str = "0.3.0"


class ChannelBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class MessageBinding(Binding):
    headers: Schema | Reference
    status_code: int = Field(gt=99, lt=600)
    binding_version: str = Field(CURRENT_VERSION)


class OperationBinding(Binding):
    method: str
    query: Schema | Reference
    binding_version: str = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class HttpBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
