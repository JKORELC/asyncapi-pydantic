"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#operationsObject
"""

from __future__ import annotations


from typing import (
    Literal,
    ParamSpec,
)


from pydantic import Field


from asyncapi.base import AsyncApiExtendable
from asyncapi.bindings import (
    AmqpOperationBinding,
    Amqp1OperationBinding,
    AnypointmqOperationBinding,
    GooglePubSubOperationBinding,
    HttpOperationBinding,
    IbmmqOperationBinding,
    JmsOperationBinding,
    KafkaOperationBinding,
    MercureOperationBinding,
    MqttOperationBinding,
    Mqtt5OperationBinding,
    NatsOperationBinding,
    PulsarOperationBinding,
    RedisOperationBinding,
    SnsOperationBinding,
    SolaceOperationBinding,
    SqsOperationBinding,
    StompOperationBinding,
    WebSocketOperationBinding,
)
from asyncapi.common import (
    ExternalDocumentation,
    Reference,
    Tags,
)
from asyncapi.security import SecurityScheme


P = ParamSpec("P")


class OperationReplyAddress(AsyncApiExtendable):
    """
    AsyncAPI Operation Reply Address class.
    """

    location: str
    description: str | None = Field(None)


class OperationReply(AsyncApiExtendable):
    """
    AsyncAPI Operation Reply class.
    """

    address: OperationReplyAddress | Reference
    channel: Reference
    messages: list[Reference]


class OperationTrait(AsyncApiExtendable):
    """
    AsyncAPI Operation Trait class.
    """

    title: str
    summary: str
    description: str
    security: SecurityScheme | Reference | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    bindings: OperationBindings | Reference | None = Field(None)


class OperationBindings(AsyncApiExtendable):
    """
    AsyncAPI Operation Bindings class.
    """

    http: HttpOperationBinding | None = Field(None)
    ws: WebSocketOperationBinding | None = Field(None)
    kafka: KafkaOperationBinding | None = Field(None)
    anypointmq: AnypointmqOperationBinding | None = Field(None)
    amqp: AmqpOperationBinding | None = Field(None)
    amqp1: Amqp1OperationBinding | None = Field(None)
    mqtt: MqttOperationBinding | None = Field(None)
    mqtt5: Mqtt5OperationBinding | None = Field(
        None, deprecated=True, deprecation="Deprecated in favor of MQTT Bindings."
    )
    nats: NatsOperationBinding | None = Field(None)
    jms: JmsOperationBinding | None = Field(None)
    sns: SnsOperationBinding | None = Field(None)
    sqs: SqsOperationBinding | None = Field(None)
    solace: SolaceOperationBinding | None = Field(None)
    stomp: StompOperationBinding | None = Field(None)
    redis: RedisOperationBinding | None = Field(None)
    mercure: MercureOperationBinding | None = Field(None)
    google: GooglePubSubOperationBinding | None = Field(None)
    ibmmq: IbmmqOperationBinding | None = Field(None)
    pulsar: PulsarOperationBinding | None = Field(None)


class Operation(AsyncApiExtendable):
    """
    AsyncAPI Operation class.
    """

    action: Literal["send", "receive"]
    channel: Reference
    title: str | None = Field(None)
    summary: str | None = Field(None)
    security: SecurityScheme | Reference | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    bindings: OperationBindings | Reference | None = Field(None)
    traits: OperationTrait | Reference | None = Field(None)
    messages: Reference | None = Field(None)
    reply: OperationReply | Reference | None = Field(None)


class Operations(AsyncApiExtendable):
    """
    AsyncAPI Operations class.
    """

    def __init__(self, **kwargs: P.kwarg) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, Operation.model_validate(val))
