"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/mqtt
"""

from __future__ import annotations

from pydantic import Field

from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiBase,
    AsyncApiExtendable,
    Schema,
    Reference,
    Uri,
)


CURRENT_VERSION: str = "0.2.0"


class ChannelBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class MessageBinding(Binding):
    payload_format_indicator: int | None = Field(ge=0, le=1)
    correlation_data: Schema | Reference | None = Field(None)
    content_type: str
    response_topic: Uri | Schema | Reference | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class OperationBinding(Binding):
    qos: int = Field(ge=0, le=2)
    retain: bool
    message_expiry_interval: int | Schema | Reference | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    client_id: str
    client_session: bool
    last_will: LastWill
    keep_alive: int
    session_expiry_interval: int | Schema | Reference | None = Field(None)
    maximum_packet_siez: int | Schema | Reference | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class LastWill(AsyncApiBase):
    topic: str
    qos: str
    message: str
    retain: bool


class MqttBinding(AsyncApiExtendable):
    channel: ChannelBinding
    message: MessageBinding
    operation: OperationBinding
    server: ServerBinding
