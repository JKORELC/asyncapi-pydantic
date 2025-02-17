from __future__ import annotations

from annotated_types import MinLen
from json import loads as json_loads
from pathlib import Path
from typing import (
    Annotated,
    Any,
    Generic,
    ParamSpec,
    TypeVar,
    Union,
)
from typing_extensions import (
    Self,
    override,
)
from yaml import (
    safe_load as yaml_loads,
    dump as yaml_dumps,
)


from pydantic import (
    Field,
    AnyUrl,
    NonNegativeInt,
    PositiveFloat,
)
from pydantic.alias_generators import to_camel


from asyncapi.base import (
    AsyncApiBase,
    AsyncApiExtendable,
)
from asyncapi.constants import (
    SchemaFormat,
    SimpleTypes,
)


P = ParamSpec("P")
T = TypeVar("T")


NonEmptyList = Annotated[list[T], MinLen(1)]
StrEnum = NonEmptyList[str]

# TODO: copy CloudEvents URI validation here.
Uri = Annotated[str, ...]


class DynamicField(AsyncApiExtendable, Generic[T]):
    def __init__(self, **kwargs: P.kwargs) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, T.model_validate(val))


class Binding(AsyncApiExtendable):
    binding_version: str | None = Field("latest")


class Bindings(AsyncApiExtendable):
    amqp: AmqpBinding | None = Field(None)
    amqp1: Amqp1Binding | None = Field(None)
    anypointmq: AnypointmqBinding | None = Field(None)
    jms: JmsBinding | None = Field(None)
    kafka: KafkaBinding | None = Field(None)
    mqtt: MqttBinding | None = Field(None)
    mqtt5: Mqtt1Binding | None = Field(
        None, deprecated="Deprecated in favor of MQTT bindings"
    )  # TODO: set deprecated flag
    nats: NatsBinding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)
    ws: Binding | None = Field(None)


class CorrelationID(AsyncApiExtendable):
    """
    An object that specifies an identifier at design time that can
    be used for message tracing and correlation.
    """

    location: str  # TODO: validate runtime expression?
    description: str | None = Field(None)


class ExternalDocumentation(AsyncApiExtendable):
    description: str
    url: str


class MultiFormatSchema(AsyncApiExtendable):
    # TODO: cross-validate schema_format X schema
    # See: https://www.asyncapi.com/docs/reference/specification/v3.0.0#multiFormatSchemaObject
    schema_format: str = Field("application/vnd.aai.asyncapi+json;version=3.0.0")
    schema_: Any = Field(alias="schema")  # TODO: fix this data type


def Parameter(AsyncApiBase):
    enum: list[str] | None = Field(None)
    default: str | None = Field(None)
    description: str | None = Field(None)  # TODO: validate CommonMark expression?
    examples: list[str] | None = Field(None)
    location: str | None = Field(None)  # TODO: validate runtime expression format?


class Parameters(AsyncApiExtendable):
    def __init__(self, **kwargs: P.kwargs) -> None:
        super().__init__(**kwargs)
        for key, val in kwargs.items():
            setattr(self, key, Parameter.model_validate(val))


class Reference(AsyncApiBase):
    ref: str = Field(alias="$ref")


class Schema(AsyncApiBase):

    # Fixed fields
    discriminator: str | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)
    deprecated: bool = Field(False)

    # Variable fields
    id_: str | None = Field(None, alias="$id")
    schema_: AnyUrl | None = Field(None, alias="$schema")
    ref: str | None = Field(None, alias="$ref")
    comment: str | None = Field(None, alias="$comment")
    title: str | None = Field(None)
    description: str | None = Field(None)
    default: Any | None = Field(None)  # TODO: fix this Any
    read_only: bool = Field(False)
    write_only: bool = Field(False)
    examples: list[Any] = Field(None)  # TODO: fix this Any
    multiple_of: PositiveFloat | None = Field(None)
    maximum: float | None = Field(None)
    exclusive_maximum: float | None = Field(None)
    minimum: float | None = Field(None)
    exclusive_minimum: float | None = Field(None)
    max_length: NonNegativeInt | None = Field(None)
    min_length: NonNegativeInt | None = Field(None)
    pattern: str | None = Field(None)
    additional_items: Schema | None = Field(None)
    items: Union[Schema, list[Schema]] | None = Field(None)
    max_items: NonNegativeInt | None = Field(None)
    min_items: NonNegativeInt | None = Field(None)
    unique_items: bool = Field(False)
    contains: Schema | None = Field(None)
    max_properties: NonNegativeInt | None = Field(None)
    min_properties: NonNegativeInt | None = Field(None)
    required: list[str] | None = Field(None)
    additional_properties: Union[Schema, bool] | None = Field(None)
    definitions: dict[str, Schema] = Field(default_factory=dict)  # TODO: fix this
    properties: dict[str, Schema] = Field(default_factory=dict)  # TODO: fix this
    dependencies: dict[str, Union[Schema, list[str]]] | None = Field(None)
    property_names: Schema | None = Field(None)
    const: Any = None  # TODO: fix this ANy
    enum_: StrEnum | None = Field(None, alias="enum")
    type_: Union[SimpleTypes, list[SimpleTypes]] | None = Field(None, alias="type")
    format_: str | None = Field(None, alias="format")
    content_media_type: str | None = Field(None)
    content_encoding: str | None = Field(None)
    if_: Schema | None = Field(None, alias="if")
    then: Schema | None = Field(None)
    else_: Schema | None = Field(None, alias="else")
    all_of: list[Schema] | None = Field(None)
    any_of: list[Schema] | None = Field(None)
    one_of: list[Schema] | None = Field(None)
    not_: Schema | None = Field(None, alias="not")


class ServerVariable(AsyncApiExtendable):
    enum: list[str] | None = Field(None)
    default: str | None = Field(None)
    description: str | None = Field(None)
    examples: list[str] | None = Field(None)


class Tag(AsyncApiExtendable):
    name: str
    description: str | None = Field(None)  # TODO: validate CommonMark
    external_docs: ExternalDocumentation | Reference | None = Field(None)


Tags = Annotated[list[Tag], ...]
