"""
This document defines how to describe IBM MQ specific information with AsyncAPI.

Reference:
    https://github.com/asyncapi/bindings/tree/master/ibmmq
"""

# TODO: top-down validations, example YAML tests, etc.


from typing import Literal


from pydantic import (
    Field,
    field_validator,
    ValidationInfo,
)

from pydantic.networks import (
    AnyUrl,
    UrlConstraints,
)


from asyncapi.bindings.base import Binding
from asyncapi.common import AsyncApiBase


CURRENT_VERSION: str = "0.1.0"


class IbmmqDsn(AnyUrl):
    _constraints = UrlConstraints(
        host_required=False,
        allowed_schemes=[
            "ibmmq",
            "http",
            "file",
        ],
    )

    @property
    def authority(self) -> str:
        """The required URL host."""
        return self._url.host

    @property
    def scheme(self) -> str:
        """The required URL scheme."""
        return self._url.scheme

    @property
    def queue_manager(self) -> str | None:
        if not self.scheme == "ibmmq":
            return None

        parts = list(filter(lambda x: x != "", self._url.path.split("/")))
        if len(parts) > 1:
            return parts[0]
        return None

    @property
    def mq_channel_name(self) -> str | None:
        if not self.scheme == "ibmmq":
            return None

        parts = list(filter(lambda x: x != "", self._url.path.split("/")))
        return parts[1]


class ChannelTopic(Binding, extra="forbid"):
    string: str | None = Field(None, max_length=10_240)
    object_name: str
    durable_permitted: bool | None = Field(True)
    last_msg_retained: bool | None = Field(False)
    max_msg_length: int | None = Field(ge=0, le=104_857_600)
    binding_version: str | None = Field(
        CURRENT_VERSION, description="The version of this binding."
    )


class ChannelQueue(Binding):
    object_name: str = Field(min_length=1, max_length=255)
    is_partitioned: bool | None = Field(False)
    exclusive: bool | None = Field(False)


class ChannelBinding(Binding):
    destionation_type: Literal["topic", "queue"] | None = Field("topic")
    queue: ChannelQueue
    topic: ChannelTopic


class MessageBinding(Binding):
    type_: Literal["string", "jms", "binary"] | None = Field("[string]")
    headers: str | None = Field(None)
    description: str | None = Field(None)
    expiry: int | None = Field(0, ge=0)
    binding_version: str | None = Field(CURRENT_VERSION)

    @field_validator("headers")
    def check_headers(cls, value: str, info: ValidationInfo) -> str:
        """
        Headers MUST NOT be specified if type is string or jms.
        """

        if value and self.type_ in ["string", "jms"]:
            raise ValueError(f"Headers must not be specified for type: {self.type_}")

        return value


class OperationBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class ServerBinding(Binding):
    group_id: str
    ccdt_queue_manager: str | None = Field("[*]")
    cipher_spec: str | None = Field("[ANY]")
    multi_endpoint_server: bool | None = Field(False)
    heart_beat_interval: int | None = Field(300, ge=0, le=999_999)
    binding_version: str | None = Field(CURRENT_VERSION)


class Server(AsyncApiBase):
    scheme: str
    authority: str
    mq_channel_name: str
    queue_manager: str | None = Field(None)


class JmsBinding(Binding, extra="allow"):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding

    # TODO: server object validations
    # https://github.com/asyncapi/bindings/tree/master/ibmmq#server-binding-object
