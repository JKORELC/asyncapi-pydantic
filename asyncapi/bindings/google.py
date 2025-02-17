"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/googlepubsub
"""

from typing import (
    Any,
    Final,
    Literal,
)

from pydantic import (
    BaseModel,
    Field,
)

from asyncapi.common import (
    Binding,
    Schema,
)


CURRENT_VERSION: str = "0.2.0"


class MessageStoragePolicy(BaseModel):
    allowed_persistence_regions: list[str]


class SchemaSettings(BaseModel):
    encoding: Literal["encoding_unspecified", "json", "binary"]
    first_revision_id: str
    last_revision_id: str
    name: str


class Schema(BaseModel):
    name: str


class ChannelBinding(Binding):
    labels: dict[str, Any] | None = Field(None)
    message_retention_duration: str | None = Field(
        None
    )  # TODO: validate proper duration
    message_storage_policy: MessageStoragePolicy | None = Field(None)
    schema_settings: SchemaSettings | None = Field(None)
    binding_version: str = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    attributes: dict[str, Any]
    ordering_key: str | None = Field(None)
    schema_: Schema | None = Field(None)
    binding_version: str = Field(CURRENT_VERSION)


class OperationBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class GooglePubSubBinding(Binding):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
