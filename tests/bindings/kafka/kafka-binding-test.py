from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator, ValidationInfo
from pydantic.alias_generators import to_camel


_model_config: ConfigDict = ConfigDict(
    alias_generator=to_camel,
    validation_serializer=to_camel,
    populate_by_name=True,
    from_attributes=True,
)


class MessageBinding(BaseModel):
    schema_id_location: str | None = Field(None)
    schema_id_payload_location: str | None = Field(None)
    schema_lookup_strategy: str | None = Field(None)

    model_config: ConfigDict = _model_config


class ServerBinding(BaseModel):
    schema_registry_url: str | None = Field(None)
    schema_registry_vendor: str | None = Field(None)

    model_config: ConfigDict = _model_config
    
    @field_validator("schema_registry_vendor", mode="after")
    @classmethod
    def check_schema_registry_rules(cls, value: str | None, info: ValidationInfo) -> str:
        schema_registry_url = info.data["schema_registry_url"]
        if bool(value) and not bool(schema_registry_url):
            raise ValueError(f"Cannot specify schemaRegistryVendor without schemaRegistryUrl")
        return value


class KafkaBinding(BaseModel):
    message: MessageBinding
    server: ServerBinding

    model_config: ConfigDict = _model_config

    @model_validator(mode="after")
    def validate_rules(self) -> Self:
        if not self.server.schema_registry_url:
            msg = self.message
            if any(
                [
                    msg.schema_id_location,
                    msg.schema_id_payload_location,
                    msg.schema_lookup_strategy
                ]
            ):
                raise ValueError("Cannot specify schema properties without schemaRegistryUrl")
        return self


use_case_1 = {
    "server": {
        "schemaRegistryUrl": "https://...",
        "schemaRegistryVendor": "confluent"
    },
    "message": {
        "schemaIdLocation": "someplace",
        "schemaIdPayloadLocation": "someplace.else",
        "schemaLookupStrategy": "TopicNameStrategy"
    }
}

print("Success Mode")
binding = KafkaBinding.model_validate(use_case_1)
print(binding)
print(binding.model_dump_json(indent=4, by_alias=True))


from pydantic_core import ValidationError

use_case_2 = use_case_1.copy()
use_case_2["server"]["schemaRegistryUrl"] = ""

print("Failure Mode")
try:
    binding = KafkaBinding.model_validate(use_case_2)
except ValidationError:
    print("Failed to parse data")
