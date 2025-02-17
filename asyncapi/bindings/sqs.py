"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/sqs
"""

from typing import Literal


from pydantic import Field


from asyncapi.bindings.aws import (
    ARN,
    Policy,
    RedrivePolicy,
)
from asyncapi.bindings.base import Binding
from asyncapi.common import (
    AsyncApiBase,
    AsyncApiExtendable,
    Tags,
)


CURRENT_VERSION: str = "0.3.0"


class SqsQueue(AsyncApiBase):
    name: str
    fifo_queue: bool
    deduplication_scope: Literal["messageGroup", "queue"]
    fifo_throughput_limit: Literal["perQueue", "perMessageGroupId"]
    delivery_delay: int | None = Field(0, ge=0, le=15)
    visibility_timeout: int | None = Field(30, ge=0, le=43_200)
    receive_message_wait_time: int | None = Field(None)
    message_retention_period: int | None = Field(345_600, ge=60, le=1_209_600)
    redrive_policy: RedrivePolicy | None = Field(None)
    policy: Policy | None = Field(None)
    tags: Tags | None = Field(None)


class ChannelBinding(Binding):
    queue: SqsQueue
    dead_letter_queue: SqsQueue | None = Field(None)
    binding_version: str | None = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class OperationBinding(Binding):
    queues: list[SqsQueue]
    binding_version: str | None = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class SqsBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
