from asyncapi.bindings import (
    AmqpChannelBinding,
    AmqpMessageBinding,
    AmqpOperationBinding,
    AmqpServerBinding,
)


binding = AmqpChannelBinding()
print(binding)

binding = AmqpMessageBinding()
print(binding)

binding = AmqpOperationBinding()
print(binding)

binding = AmqpServerBinding()
print(binding)
