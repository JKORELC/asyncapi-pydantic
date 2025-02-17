from asyncapi.messages import Message


message = Message.from_yaml("tests/messages/message.yaml")
print(message)
print(message.model_dump())
