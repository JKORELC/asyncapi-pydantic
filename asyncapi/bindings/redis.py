"""
Reference:
    https://github.com/asyncapi/bindings/tree/master/redis
"""

from asyncapi.bindings.base import Binding
from asyncapi.common import AsyncApiBase


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


class RedisBindings(AsyncApiBase):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
