"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/solace
"""

# TODO: test yamls


from enum import Enum


from pydantic import Field


from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiBase,
    AsyncApiExtendable,
    Schema,
    Reference,
)


CURRENT_VERSION: str = "0.4.0"


class AccessType(str, Enum):
    EXCLUSIVE: str = "exclusive"
    NONEXCLUSIVE: str = "nonexclusive"


class DestinationType(str, Enum):
    QUEUE: str = "queue"
    TOPIC: str = "topic"


class DeliveryMode(str, Enum):
    DIRECT: str = "direct"
    PERSISTENT: str = "persistent"


class DestinationQueue(AsyncApiBase):
    name: str
    topic_subscriptions: list[str]
    access_type: AccessType
    max_msg_spool_size: str
    max_ttl: str
    topic_subscriptions: list[str]


class Destination(AsyncApiBase):
    destination_type: DestinationType
    delivery_mode: DeliveryMode | None = Field(DeliveryMode.PERSISTENT)
    queue: DestinationQueue | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


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
    destinations: list[Destination] | None = Field(None)
    time_to_live: int | Schema | Reference | None = Field(None)
    priority: int | Schema | Reference | None = Field(None)
    dmq_eligible: bool | None = Field(False)
    binding_version: str | None = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    msg_vpn: str | None = Field(None)
    client_name: str | None = Field(None, max_length=160)
    binding_version: str | None = Field(CURRENT_VERSION)


class SolaceBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
