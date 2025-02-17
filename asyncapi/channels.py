"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#channelsObject
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#channelBindingsObject
"""

from __future__ import annotations

from pydantic import (
    Field,
)

from asyncapi.common import (
    AsyncApiExtendable,
    ExternalDocumentation,
    Parameters,
    Reference,
    Tags,
)


from asyncapi.bindings import (
    AmqpChannelBinding,
    Amqp1ChannelBinding,
    GooglePubSubChannelBinding,
    HttpChannelBinding,
    JmsChannelBinding,
    IbmmqChannelBinding,
    KafkaChannelBinding,
    MercureChannelBinding,
    MqttChannelBinding,
    Mqtt5ChannelBinding,
    NatsChannelBinding,
    PulsarChannelBinding,
    RedisChannelBinding,
    SnsChannelBinding,
    SolaceChannelBinding,
    StompChannelBinding,
    SqsChannelBinding,
    WebSocketBinding,
)

from asyncapi.messages import Messages


class Channel(AsyncApiExtendable):
    address: str | None = Field(None)
    messages: Messages | None = Field(None)
    title: str | None = Field(None)
    summary: str | None = Field(None)
    description: str | None = Field(None)
    servers: list[Reference] | None = Field(None)
    parameters: Parameters | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    bindings: ChannelBindings | Reference | None = Field(None)


class Channels(AsyncApiExtendable):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, Channel.model_validate(val))


class ChannelBindings(AsyncApiExtendable):
    amqp: AmqpChannelBinding | None = Field(None)
    amqp1: Amqp1ChannelBinding | None = Field(None)
    googlepubsub: GooglePubSubChannelBinding | None = Field(None)
    http: HttpChannelBinding | None = Field(None)
    jms: JmsChannelBinding | None = Field(None)
    ibmmq: IbmmqChannelBinding | None = Field(None)
    kafka: KafkaChannelBinding | None = Field(None)
    mercure: MercureChannelBinding | None = Field(None)
    mqtt: MqttChannelBinding | None = Field(None)
    mqtt5: Mqtt5ChannelBinding | None = Field(
        None, deprecation="Deprecated in favor of MQTT Bindings."
    )
    nats: NatsChannelBinding | None = Field(None)
    pulsar: PulsarChannelBinding | None = Field(None)
    redis: RedisChannelBinding | None = Field(None)
    sns: SnsChannelBinding | None = Field(None)
    solace: SolaceChannelBinding | None = Field(None)
    stomp: StompChannelBinding | None = Field(None)
    sqs: SqsChannelBinding | None = Field(None)
    ws: WebsocketChannelBinding | None = Field(None)
