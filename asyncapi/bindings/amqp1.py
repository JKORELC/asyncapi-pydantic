"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/amqp1
"""

from asyncapi.bindings.base import Binding
from asyncapi.common import AsyncApiExtendable


CURRENT_VERSION: str = "0.1.0"


__all__ = ["ChannelBinding", "MessageBinding", "OperationBinding", "ServerBinding"]


class ChannelBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


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
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class Amqp1Binding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
