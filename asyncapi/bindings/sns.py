"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/sns/3.0.0
"""

from __future__ import annotations


from typing import Literal

from pydantic import (
    Field,
    PositiveInt,
)

from asyncapi.bindings.aws import (
    ARN,
    Identifier,
    Policy,
)
from asyncapi.bindings.base import Binding
from asyncapi.common import AsyncApiBase, AsyncApiExtendable


CURRENT_VERSION: str = "1.0.0"


class Consumer(AsyncApiBase):
    protocol: Literal[
        "http",
        "https",
        "email",
        "email-json",
        "sms",
        "sqs",
        "application",
        "lambda",
        "firehose",
    ]
    endpoint: Identifier
    raw_message_delivery: bool  # TODO: validation
    filter_policy: dict[str, Any] | None = Field(None)
    filter_policy_scope: str | None = Field(None)
    redrive_policy: RedrivePolicy | None = Field(None)
    delivery_policy: DeliveryPolicy | None = Field(None)
    display_name: str | None = Field(None)


class DeliveryPolicy(AsyncApiBase):
    min_delay_target: PositiveInt | None = Field(None)
    max_delay_target: PositiveInt | None = Field(None)
    num_retries: PositiveInt | None = Field(None)
    num_no_delay_retries: PositiveInt | None = Field(None)
    num_min_delay_retries: PositiveInt | None = Field(None)
    num_max_delay_retries: PositiveInt | None = Field(None)
    backoff_function: (
        Literal["arithmetic", "exponential", "geometric", "linear"] | None
    ) = Field(None)
    max_receives_per_second: PositiveInt | None = Field(None)


class Ordering(AsyncApiBase):
    type_: Literal["standar", "FIFO"]
    content_based_deduplication: bool | None = Field(False)


class ChannelBinding(Binding):
    name: str
    ordering: Ordering | None = Field(None)
    policy: Policy | None = Field(None)
    tags: Tags
    binding_version: str | None = Field(CURRENT_VERSION)


class MessageBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class OperationBinding(Binding):
    topic: Identifier
    consumers: list[Consumer]
    delivery_policy: DeliveryPolicy
    binding_version: str | None = Field(CURRENT_VERSION)


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class SnsBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
