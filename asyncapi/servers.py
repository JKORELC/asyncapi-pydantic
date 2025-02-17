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
    ServerVariable,
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


class ServerBindings(AsyncApiExtendable):
    http: HttpServerBinding | None = Field(None)
    ws: WebSocketServerBinding | None = Field(None)
    amqp: AmqpServerBinding | None = Field(None)
    amqp1: Amqp1ServerBinding | None = Field(None)
    aynpointmq: AnypointmqServerBinding | None = Field(None)
    nats: NatsServerBinding | None = Field(None)
    sns: SnsServerBinding | None = Field(None)
    sqs: SqsServerBinding | None = Field(None)
    stomp: StompServerBinding | None = Field(None)
    redis: RedisServerBinding | None = Field(None)
    mercuer: MercureServerBinding | None = Field(None)
    googlepubsub: GooglePubSubServerBinding | None = Field(None)
    mqtt: MqttServerBinding | None = Field(None)
    mqtt5: Mqtt5ServerBinding | None = Field(
        None, deprecated=True, deprecation="Deprecated in favor of MQTT Bindings."
    )
    kafka: KafkaServerBinding | None = Field(None)
    jms: JmsServerBinding | None = Field(None)
    ibmmq: IbmmqServerBinding | None = Field(None)
    solace: SolaceServerBinding | None = Field(None)
    pulsar: PulsarServerBinding | None = Field(None)


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
