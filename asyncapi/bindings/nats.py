from asyncapi.bindings.base import (
    Field,
    Binding,
)


from asyncapi.common import (
    AsyncApiExtendable,
)


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


class OperationBinding(Binding, extra="allow"):
    queue: str = Field(min_length=1, max_length=255)
    binding_version: str = Field("0.1.0")


class ServerBinding(Binding):
    """
    This object MUST NOT contain any properties.
    Its name is reserved for future use.
    """

    ...


class NatsBinding(AsyncApiExtendable):
    channels: ChannelBinding
    messages: MessageBinding
    operations: OperationBinding
    servers: ServerBinding
