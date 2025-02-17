
from asyncapi.asyncapi import Info


info = Info.from_yaml("tests/info.yaml")
print(info)
print(info.model_dump_json())
