"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/pulsar
"""

from __future__ import annotations

from typing import Literal


from pydantic import Field


from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiExtendable,
)


CURRENT_VERSION: str = "0.1.0"


class ChannelBinding(Binding):
    namespace: str
    persistence: Literal["persistent", "non-persistent"]
    compaction: int | None = Field(None)
    geo_replication: list[str] | None = Field(alias="geo-replication", alias_priority=2)
    retention: RetentionDefinition | None = Field(None)
    ttl: int | None = Field(None)
    deduplication: bool | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class OperationBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class ServerBinding(Binding):
    tenant: str | None = Field("public")
    binding_version: str | None = Field(CURRENT_VERSION)


class RetentionDefinition(Binding):
    time: int | None = Field(0)
    size: int | None = Field(0)


class PulsarBinding(AsyncApiExtendable):
    channel: ChannelBinding
    message: MessageBinding
    operation: OperationBinding
    server: ServerBinding
