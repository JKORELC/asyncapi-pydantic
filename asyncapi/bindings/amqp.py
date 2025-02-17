"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/amqp
"""

from __future__ import annotations

from typing import (
    Final,
    Literal,
)

from asyncapi.bindings.base import (
    BaseModel,
    Field,
    Binding,
)


CURRENT_VERSION: str = "0.3.0"


__all__ = ["ChannelBinding", "MessageBinding", "OperationBinding", "ServerBinding"]


class AmqpExchange(BaseModel):
    """
    This object contains information about the channel exchange.
    """

    name: str = Field(
        min_length=1,
        max_length=255,
        description="The name of the exchange. It MUST NOT exceed 255 characters long.",
    )
    type_: Literal["topic", "direct", "fanout", "default", "headers"] = Field(
        description="The type of the exchange. Can be either topic, direct, fanout, default or headers."
    )
    durable: bool = Field(
        description="Whether the exchange should survive broker restarts or not."
    )
    auto_delete: bool = Field(
        description="Whether the exchange should be deleted when the last queue is unbound from it."
    )
    vhost: str = Field(description="The virtual host of the exchange. Defaults to /.")


class AmqpQueue(BaseModel):
    """
    This object contains information about the channel queue.
    """

    name: str = Field(
        min_length=1,
        max_length=255,
        description="The name of the queue. It MUST NOT exceed 255 characters long.",
    )
    durable: bool = Field(
        description="Whether the queue should survive broker restarts or not."
    )
    exclusive: bool = Field(
        description="Whether the queue should be used only by one connection or not."
    )
    auto_delete: bool = Field(
        description="Whether the queue should be deleted when the last consumer unsubscribes."
    )
    vhost: str = Field(description="The virtual host of the queue. Defaults to /.")


class ChannelBinding(Binding):
    """
    This object contains information about the channel representation in AMQP.
    """

    is_: Literal["queue", "routingKey"] = Field(
        "routingKey",
        description="Defines what type of channel is it. Can be either queue or routingKey (default).",
    )
    exchange: AmqpExchange | None = Field(
        None,
        description="When is=routingKey, this object defines the exchange properties.",
    )
    queue: AmqpQueue | None = Field(
        None, description="When is=queue, this object defines the queue properties."
    )
    binding_version: str = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object contains information about the message representation in AMQP.
    """

    content_encoding: str
    message_type: str
    binding_version: str = Field(CURRENT_VERSION)


class OperationBinding(Binding):
    """
    This object contains information about the operation representation in AMQP.
    """

    expiration: int
    user_id: str
    cc: list[str]
    priority: int
    mandatory: bool
    bcc: list[str]
    timestamp: bool
    ack: bool
    binding_version: str = Field("0.3.0")


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class AmqpBinding(Binding, extra="allow"):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
