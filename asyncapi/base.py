"""
AsyncAPI base classes.
"""

from __future__ import annotations

from json import loads as json_loads
from pathlib import Path
from typing import (
    Any,
    ParamSpec,
)
from typing_extensions import (
    Self,
)
from yaml import (
    safe_load as yaml_loads,
    dump as yaml_dumps,
)


from pydantic import (
    BaseModel,
    ConfigDict,
)
from pydantic.alias_generators import to_camel


P = ParamSpec("P")


class AsyncApiBase(BaseModel):
    """
    AsyncAPI Base class.
    """

    model_config: ConfigDict = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
        use_enum_values=True,
        extra="ignore",
    )

    @classmethod
    def from_json(cls, pathname: str | Path) -> Self:
        """
        Load AsyncAPI specification from JSON.
        """

        config = Path(pathname).read_text(encoding="utf8")
        config = json_loads(config)
        if isinstance(config, list):
            return [cls(**entry) for entry in config]
        return cls(**config)

    @classmethod
    def from_yaml(cls, pathname: str | Path) -> Self:
        """
        Load AsyncAPI specification from YAML.
        """

        config = Path(pathname).read_text(encoding="utf8")
        config = yaml_loads(config)
        if isinstance(config, list):
            return [cls(**entry) for entry in config]
        return cls(**config)

    def _default_params(self, **kwargs: P.kwargs) -> P.kwargs:  # type: ignore
        """
        Default serialization parameters.
        """

        kwargs["by_alias"] = kwargs.get("by_alias", True)
        kwargs["exclude_none"] = kwargs.get("exclude_none", True)
        kwargs["exclude_unset"] = kwargs.get("exclude_unset", True)
        return kwargs

    def model_dump(self, **kwargs: P.kwargs) -> dict[str, Any]:  # type: ignore
        """
        Model dump override.
        """

        kwargs = self._default_params(**kwargs)
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs: P.kwargs) -> str:  # type:ignore
        """
        Model dump JSON override.
        """

        kwargs = self._default_params(**kwargs)
        kwargs["indent"] = kwargs.get("indent", 4)
        return super().model_dump_json(**kwargs)

    def model_dump_yaml(self, **kwargs: P.kwargs) -> str:  # type: ignore
        """
        Model dump YAML.
        """

        kwargs = self._default_params(**kwargs)
        data = self.model_dump(**kwargs)
        return yaml_dumps(data, sort_keys=False)


class AsyncApiExtendable(AsyncApiBase):
    """
    AsyncAPI Extendable base model.
    """

    model_config: ConfigDict = ConfigDict(extra="allow")  # type: ignore
