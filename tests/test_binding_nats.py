from pydantic import ValidationError

from asyncapi.bindings.nats import *


data = {
    "bogus": "field"
}


try:
    binding = ChannelBinding.model_validate(data)
except ValidationError:
    pass


try:
    binding = MessageBinding.model_validate(data)
except ValidationError:
    pass


try:
    binding = OperationBinding.model_validate(data)
except ValidationError:
    pass


try:
    binding = ServerBinding.model_validate(data)
except ValidationError:
    pass
