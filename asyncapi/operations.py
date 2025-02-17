"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#operationsObject
"""


from __future__ import annotations


from pydantic import Field


from asyncapi.base import AsyncApiExtendable
from asyncapi.common import (
    ExternalDocumentation,
    Reference, 
    Tags,
)
from asyncapi.security import SecurityScheme


class OperationReplyAddress(AsyncApiExtendable):
    location: str
    description: str | None = Field(None)


class OperationReply(AsyncApiExtendable):
    address: OperationReplyAddress | Reference
    channel: Reference
    messages: list[Reference]


class OperationTrait(AsyncApiExtendable):
    title: str
    summary: str
    description: str
    security: SecurityScheme | Reference | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    bindings: OperationBindings | Reference | None = Field(None)


class OperationBindings(AsyncApiExtendable):
    http: HttpOperationBinding
    ws: WebSocketsOperationBinding
    kafka: KafkaOperationBinding
    anypointmq: AnypointmqOperationBinding
    amqp: AmqpOperationBinding
    amqp1: Amqp1OperationBinding
    mqtt: MqttOperationBinding
    mqtt5: Mqtt5OperationBinding
    nats: NatsOperationBinding
    jms: JmsOperationBinding
    sns: SnsOperationBinding
    sqs: SqsOperationBinding
    solace: SolaceOperationBinding
    stomp: StompOperationBinding
    redis: RedisOperationBinding
    mercure: MercureOperationBinding
    google: GooglepubsubOperationBinding
    ibmmq: IbmmqOperationBinding
    pulsar: PulsarOperationBinding


class Operation(AsyncApiExtendable):
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
    def __init__(self, **kwargs: P.kwarg) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, Operation.model_validate(val))
