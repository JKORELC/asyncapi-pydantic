from typing import Union


from pydantic import Field


from asyncapi.base import AsyncApiExtendable
from asyncapi.common import (
    CorrelationID,
    ExternalDocumentation,
    Parameter,
    Reference,
    ServerVariable,
    Tag,
)
from asyncapi.channels import (
    Channel,
    ChannelBindings,
)
from asyncapi.operations import (
    Operation,
    OperationBindings,
    OperationReply,
    OperationReplyAddress,
    OperationTrait,
)
from asyncapi.messages import (
    Message,
    MessageBindings,
    MessageTrait,
)
from asyncapi.servers import (
    Server,
    ServerBindings,
)
from asyncapi.security import SecurityScheme


class Components(AsyncApiExtendable):
    schemas: str = Field(pattern="^[\w\d\.\-_]+$")
    servers: dict[str, Union[Server, Reference]]
    channels: dict[str, Union[Channel, Reference]]
    operations: dict[str, Union[Operation, Reference]]
    messages: dict[str, Union[Message, Reference]]
    security_schemes: dict[str, Union[SecurityScheme, Reference]]
    server_variables: dict[str, Union[ServerVariable, Reference]]
    parameters: dict[str, Union[Parameter, Reference]]
    correlation_ids: dict[str, Union[CorrelationID, Reference]]
    replies: dict[str, Union[OperationReply, Reference]]
    reply_addresses: dict[str, Union[OperationReplyAddress, Reference]]
    external_docs: dict[str, ExternalDocumentation]
    tags: dict[str, Tag]
    operation_traits: dict[str, Union[OperationTrait, Reference]]
    message_traits: dict[str, Union[MessageTrait, Reference]]
    channel_bindings: dict[str, Union[ChannelBindings, Reference]]
    message_bindings: dict[str, Union[MessageBindings, Reference]]
    operation_bindings: dict[str, Union[OperationBindings, Reference]]
    server_bindings: dict[str, Union[ServerBindings, Reference]]
