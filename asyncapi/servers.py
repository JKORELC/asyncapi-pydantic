"""
Reference:
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#serversObject
"""

from typing import Union


from pydantic import Field


from asyncapi.common import (
    AsyncApiExtendable,
    ExternalDocumentation,
    Reference,
    Tags,
)

from asyncapi.bindings import (
    AmqpServerBinding,
    Amqp1ServerBinding,
    AnypointmqServerBinding,
    GooglePubSubServerBinding,
    HttpServerBinding,
    IbmmqServerBinding,
    JmsServerBinding,
    KafkaServerBinding,
    MercureServerBinding,
    MqttServerBinding,
    Mqtt5ServerBinding,
    NatsServerBinding,
    PulsarServerBinding,
    RedisServerBinding,
    SnsServerBinding,
    SolaceServerBinding,
    SqsServerBinding,
    StompServerBinding,
    WebSocketServerBinding,
)


from asyncapi.security import (
    SecurityScheme,
)


class ServerVariable(AsyncApiExtendable):
    enum: list[str] | None = Field(None)
    default: str | None = Field(None)
    description: str | None = Field(None)
    examples: list[str] | None = Field(None)


class ServerBindings(AsyncApiExtendable):
    http: HttpServerBinding
    ws: WebSocketServerBinding
    amqp: AmqpServerBinding
    amqp1: Amqp1ServerBinding
    aynpointmq: AnypointmqServerBinding
    nats: NatsServerBinding
    sns: SnsServerBinding
    sqs: SqsServerBinding
    stomp: StompServerBinding
    redis: RedisServerBinding
    googlepubsub: GooglePubSubServerBinding
    mqtt: MqttServerBinding
    mqtt5: Mqtt5ServerBinding  # TODO: deprecated
    kafka: KafkaServerBinding
    jms: JmsServerBinding
    ibmmq: IbmmqServerBinding
    solace: SolaceServerBinding
    pulsar: PulsarServerBinding


class Server(AsyncApiExtendable):
    host: str
    protocol: str
    protocol_version: str | None = Field(None)
    pathname: str | None = Field(None)
    title: str | None = Field(None)
    summary: str | None = Field(None)
    description: str | None = Field(None)
    variables: dict[str, Union[ServerVariable, Reference]] | None = Field(None)
    security: SecurityScheme | Reference | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    bindings: ServerBindings | None = Field(None)


class Servers(AsyncApiExtendable):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        for key, val in kwargs.items():
            setattr(self, key, Server.model_validate(val))
