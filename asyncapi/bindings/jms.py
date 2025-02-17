"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/jms

"""

from typing import (
    Literal,
)


from pydantic import (
    Field,
    field_validator,
    AnyUrl,
)

from asyncapi.base import (
    AsyncApiBase,
)

from asyncapi.bindings.base import (
    Binding,
)

from asyncapi.common import (
    Schema,
)


CURRENT_VERSION: str = "3.1"

JMS_VERSIONS = Literal[
    "1.0",
    "1.0.1",
    "1.0.1a",
    "1.0.2",
    "1.0.2a",
    "1.0.2b",
    "1.1",
    "2.0",
    "2.0a",
    "2.1",
    "3.0",
    "3.1",
]


class Server(AsyncApiBase):
    protocol: Literal["jms"]
    url: str
    protocol_version: str | None = Field(CURRENT_VERSION)

    @field_validator("protocol_version", mode="after")
    def check_protocol_version(cls, value: str) -> str:
        if value not in JMS_VERSIONS:
            raise ValueError(f"Not a valid JMS version: {value}")
        return value


class ChannelBinding(Binding):
    """ """

    destination: str | None = Field(None)
    destination_type: Literal["queue", "fifo-queue"] | None = Field("queue")
    binding_version: str | None = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """ """

    headers: Schema | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class OperationBinding(Binding): ...


class ServerBinding(Binding):
    jms_connection_factory: str
    properties: list[Schema] | None = Field(None)
    client_id: str | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class Server(AsyncApiBase):
    protocol: Literal["jms"]
    url: AnyUrl
    protocol_version: str | None = Field(CURRENT_VERSION)

    @field_validator("url", mode="after")
    @classmethod
    def validate_url(cls, value: str) -> str:
        if not value.startswith("jms://"):
            raise ValueError(f"Not a valid JMS path: {value}")
        return value


class JmsBinding(Binding, extra="allow"):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
