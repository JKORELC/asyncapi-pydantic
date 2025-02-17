from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from pydantic.alias_generators import to_camel


def to_camel_custom(name: str) -> str:
    return to_camel(name.rstrip("_"))


class Binding(BaseModel, extra="forbid"):
    model_config: ConfigDict = ConfigDict(
        alias_generator=to_camel_custom,
    )

    @property
    def major_version(self) -> str:
        if self.binding_version and "." in self.binding_version:
            return self.binding_version.split(".")[0]
        return ""

    @property
    def minor_version(self) -> str:
        if self.binding_version and "." in self.binding_version:
            return self.binding_version.split(".")[1]
        return ""

    @property
    def patch_level(self) -> str:
        if self.binding_version and "." in self.binding_version:
            return self.binding_version.split(".")[2]
        return ""
