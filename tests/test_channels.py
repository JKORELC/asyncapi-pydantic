from asyncapi.channels import Channel


channel = Channel.from_yaml("tests/channels.yaml")
print(channel)
