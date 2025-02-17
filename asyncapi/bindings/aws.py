from __future__ import annotations

from typing import Literal


from pydantic import (
    BaseModel,
    Field,
    PrivateAttr,
)


from asyncapi.common import AsyncApiBase


class ARN(BaseModel):
    arn: str
    _arn_parts: list[str] = PrivateAttr(default_factory=list)

    def __init__(self, arn: str) -> None:
        super().__init__(arn=arn)
        self._arn_parts = arn.split(":")

    @property
    def partition(self) -> str:
        return self._arn_parts[1]

    @property
    def service(self) -> str:
        return self._arn_parts[2]

    @property
    def region(self) -> str:
        return self._arn_parts[3]

    @property
    def account_id(self) -> str:
        return self._arn_parts[4]

    @property
    def resource_id(self) -> str:
        if len(self._arn_parts) < 5:
            return None

        return self._arn_parts[-1]

    @property
    def resource_type(self) -> str | None:
        if len(self._arn_parts) >= 6:
            if "/" in self._arn_parts[-1]:
                return self._arn_parts[-1].split("/")[0]
            else:
                return self._arn_parts[5]
        return None


class Identifier(AsyncApiBase):
    arn: ARN | None = Field(None)
    name: str | None = Field(None)


class Policy(AsyncApiBase):
    statements: Statement | list[Statement]


class RedrivePolicy(AsyncApiBase):
    dead_letter_queue: Identifier
    max_receive_count: int | None = Field(None)


class Statement(AsyncApiBase):
    effect: Literal["Allow", "Deny"]
    principal: str
    action: str
    resource: str | list[str] | None = Field(None)
    condition: str | list[str] | None = Field(None)
