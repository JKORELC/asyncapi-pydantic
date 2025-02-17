from asyncapi.common import (
    AsyncApiBase,
    Tag,
)


class Tags(AsyncApiBase):
    tags: list[Tag]


tags = Tags.from_yaml("tests/tags.yaml")
print(tags)
print(tags.model_dump_json())
print(tags.model_dump_yaml())
