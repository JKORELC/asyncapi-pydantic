"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#messagesObject
"""

from __future__ import annotations

from typing import (
    Annotated,
    Any,
    Union,
)

from pydantic import Field


from asyncapi.bindings import (
    AmqpMessageBinding,
    Amqp1MessageBinding,
    GooglePubSubMessageBinding,
    HttpMessageBinding,
    JmsMessageBinding,
    IbmmqMessageBinding,
    KafkaMessageBinding,
    MercureMessageBinding,
    MqttMessageBinding,
    Mqtt5MessageBinding,
    NatsMessageBinding,
    PulsarMessageBinding,
    RedisMessageBinding,
    SnsMessageBinding,
    SolaceMessageBinding,
    StompMessageBinding,
    SqsMessageBinding,
    WebSocketBinding,
)


from asyncapi.common import (
    AsyncApiBase,
    AsyncApiExtendable,
    CorrelationID,
    ExternalDocumentation,
    MultiFormatSchema,
    Schema,
    Reference,
    Tags,
)


MessageHeaders = Annotated[Union[MultiFormatSchema, Schema, Reference], ...]
MessagePayload = Annotated[Union[MultiFormatSchema, Schema, Reference], ...]


class MessageBindings(AsyncApiExtendable):
    amqp: AmqpMessageBinding | None = Field(None)
    amqp1: Amqp1MessageBinding | None = Field(None)
    googlepubsub: GooglePubSubMessageBinding | None = Field(None)
    http: HttpMessageBinding | None = Field(None)
    jms: JmsMessageBinding | None = Field(None)
    ibmmq: IbmmqMessageBinding | None = Field(None)
    kafka: KafkaMessageBinding | None = Field(None)
    mercure: MercureMessageBinding | None = Field(None)
    mqtt: MqttMessageBinding | None = Field(None)
    mqtt5: Mqtt5MessageBinding | None = Field(
        None, deprecation="Deprecated in favor of MQTT Bindings."
    )
    nats: NatsMessageBinding | None = Field(None)
    pulsar: PulsarMessageBinding | None = Field(None)
    redis: RedisMessageBinding | None = Field(None)
    sns: SnsMessageBinding | None = Field(None)
    solace: SolaceMessageBinding | None = Field(None)
    stomp: StompMessageBinding | None = Field(None)
    sqs: SqsMessageBinding | None = Field(None)
    ws: WebsocketMessageBinding | None = Field(None)


class MessageExample(AsyncApiExtendable):
    # https://www.asyncapi.com/docs/reference/specification/v3.0.0#messageExampleObject
    headers: dict[str, MessageHeaders] | None = Field(
        None
    )  # TODO: this value MUST validate against Message.headers
    payload: dict[str, MessagePayload] | None = Field(
        None
    )  # TODO: this value MUST validate against Message.payload
    name: str | None = Field(None)
    summary: str | None = Field(None)


class MessageTrait(AsyncApiExtendable):
    headers: MultiFormatSchema | Schema | Reference | None = Field(None)
    correlation_id: CorrelationID | Reference
    content_type: str
    name: str
    title: str
    summary: str
    description: str | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | None = Field(None)
    bindings: MessageBinding | Reference | None = Field(None)


class Message(AsyncApiExtendable):
    headers: MultiFormatSchema | Schema | Reference | None = Field(None)
    payload: MultiFormatSchema | Schema | Reference | None = Field(None)
    correlation_id: CorrelationID | Reference | None = Field(None)
    content_type: str | None = Field(
        "application/json"
    )  # TODO: validate content_type values
    name: str | None = Field(None)
    title: str | None = Field(None)
    summary: str | None = Field(None)
    description: str | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | None = Field(None)
    bindings: Any  # MessageBindings | Reference | None
    examples: list[MessageExample] | None = Field(None)
    traits: list[MessageTrait] | None = Field(None)


class Messages(AsyncApiBase):
    def __init__(self, **kwargs: P.kwargs) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, Message.model_validate(val))
