from __future__ import annotations

from annotated_types import MinLen
from json import loads as json_loads
from pathlib import Path
from typing import (
    Annotated,
    Any,
    ParamSpec,
    TypeVar,
)
from typing_extensions import (
    Self,
    override,
)
from yaml import (
    safe_load as yaml_loads,
    dump as yaml_dumps,
)


from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from pydantic.alias_generators import to_camel


from asyncapi.constants import (
    SchemaFormat,
    SimpleTypes,
)


class AsyncApiBase(BaseModel):
    model_config: ConfigDict = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
        use_enum_values=True,
        extra="ignore",
    )

    @classmethod
    def from_json(cls, pathname: str | Path) -> Self:
        config = Path(pathname).read_text(encoding="utf8")
        config = json_loads(config)
        if type(config) is list:
            return [cls(**entry) for entry in config]
        return cls(**config)

    @classmethod
    def from_yaml(cls, pathname: str | Path) -> Self:
        config = Path(pathname).read_text(encoding="utf8")
        config = yaml_loads(config)
        if type(config) is list:
            return [cls(**entry) for entry in config]
        return cls(**config)

    def _default_params(self, **kwargs: P.kwargs) -> P.kwargs:  # type: ignore
        kwargs["by_alias"] = kwargs.get("by_alias", True)
        kwargs["exclude_none"] = kwargs.get("exclude_none", True)
        kwargs["exclude_unset"] = kwargs.get("exclude_unset", True)
        return kwargs

    def model_dump(self, **kwargs: P.kwargs) -> dict[str, Any]:  # type: ignore
        kwargs = self._default_params(**kwargs)
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs: P.kwargs) -> str:  # type:ignore
        kwargs = self._default_params(**kwargs)
        kwargs["indent"] = kwargs.get("indent", 4)
        return super().model_dump_json(**kwargs)

    def model_dump_yaml(self, **kwargs: P.kwargs) -> str:  # type: ignore
        kwargs = self._default_params(**kwargs)
        data = self.model_dump(**kwargs)
        return yaml_dumps(data, sort_keys=False)


class AsyncApiExtendable(AsyncApiBase):
    model_config: ConfigDict = ConfigDict(extra="allow")  # type: ignore
