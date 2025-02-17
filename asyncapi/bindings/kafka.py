"""
This document defines how to describe Kafka-specific information on AsyncAPI.

Reference:
    https://github.com/asyncapi/bindings/tree/master/kafka
"""

from enum import Enum
from typing_extensions import Self

from pydantic import (
    ConfigDict,
    Field,
    PositiveInt,
    field_validator,
    model_validator,
    ValidationInfo,
)


from asyncapi.base import (
    AsyncApiBase,
    AsyncApiExtendable,
)
from asyncapi.bindings.base import Binding
from asyncapi.common import (
    Schema,
    MultiFormatSchema,
    Reference,
    Tags,
)


CURRENT_VERSION: str = "0.5.0"


def snake_to_dot_case(value: str) -> str:
    return value.replace("_", ".")


class AVROSchema(AsyncApiBase):
    name: str
    title: str
    summary: str | None = Field(None)
    description: str | None = Field(None)
    tags: Tags | None = Field(None)
    payload: MultiFormatSchema | Schema | Reference | None = Field(None)


class SchemaRegistryVendor(str, Enum):
    APICURIO: str = "apicurio"
    CONFLUENT: str = "confluent"
    IBM: str = "ibm"
    KARAPACE: str = "karapace"


class SchemaSubject(AsyncApiBase):
    schema_validation: str = Field(alias="schema.validation")
    subject_name_strategy: str = Field(alias="subject.name.strategy")


class Confluent(AsyncApiBase):
    key: SchemaSubject
    value: SchemaSubject


class TopicConfiguration(AsyncApiBase):
    # TODO: lock clean-up policy to kafka values
    cleanup_policy: list[str] | None = Field(["delete", "compact"])
    retention_ms: int | None = Field(1)
    retention_bytes: int | None = Field(1)
    delete_retention_ms: int | None = Field(1)
    max_message_bytes: int | None = Field(None)
    confluent: Confluent | None = Field(None)

    model_config: ConfigDict = ConfigDict(
        alias_generator=snake_to_dot_case,
    )


class ChannelBinding(Binding):
    """
    This object contains information about the channel representation in Kafka
    (eg. a Kafka topic).
    """

    topic: str | None = Field(None)
    partitions: PositiveInt | None = Field(1)
    replicas: PositiveInt | None = Field(1)
    topic_configuration: TopicConfiguration | None = Field(None)
    binding_version: str = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object contains information about the message representation in Kafka.
    """

    key: Schema | Reference | AVROSchema | None = Field(None)
    schema_id_location: str | None = Field(None)
    schema_id_payload_encoding: str | None = Field(None)
    schema_lookup_strategy: str | None = Field(None)
    binding_version: str | None = Field(None)


class OperationBinding(Binding):
    """
    This object contains information about the operation representation in
    Kafka (eg. the way to consume messages).
    """

    group_id: Schema | Reference | None = Field(None)
    client_id: Schema | Reference | None = Field(None)
    binding_version: str = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    """
    This object contains information about the server representation in Kafka.
    """

    schema_registry_url: str | None = Field(None)
    schema_registry_vendor: SchemaRegistryVendor | None = Field(
        SchemaRegistryVendor.CONFLUENT
    )
    binding_version: str | None = Field(CURRENT_VERSION)

    @field_validator("schema_registry_vendor", mode="after")
    @classmethod
    def check_schema_registry_rules(
        cls, value: str | None, info: ValidationInfo
    ) -> str:
        schema_registry_url = info.data["schema_registry_url"]
        if bool(value) and not bool(schema_registry_url):
            raise ValueError(
                f"Cannot specify schemaRegistryVendor without schemaRegistryUrl"
            )
        return value


class KafkaBinding(AsyncApiExtendable):
    channel: ChannelBinding = Field(ChannelBinding)
    message: MessageBinding = Field(MessageBinding)
    operation: OperationBinding = Field(OperationBinding)
    server: ServerBinding = Field(ServerBinding)
    binding_version: str | None = Field(CURRENT_VERSION)

    @model_validator(mode="after")
    def validate_rules(self) -> Self:
        if not self.server.schema_registry_url:
            msg = self.message
            if any(
                [
                    msg.schema_id_location,
                    msg.schema_id_payload_location,
                    msg.schema_lookup_strategy,
                ]
            ):
                raise ValueError(
                    "Cannot specify schema properties without schemaRegistryUrl"
                )
        return self
