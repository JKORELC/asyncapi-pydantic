from typing import Literal


SchemaFormat = Literal[
    "application/vnd.aai.asyncapi+json;version=3.0.0",
    "application/schema+json;version=draft-07",
    "application/vnd.aai.asyncapi+yaml;version=3.0.0",
    "application/schema+yaml;version=draft-07",
    "application/vnd.apache.avro;version=1.9.0",
    "application/vnd.apache.avro+json;version=1.9.0",
    "application/vnd.apache.avro+yaml;version=1.9.0",
    "application/vnd.oai.openapi;version=3.0.0",
    "application/vnd.oai.openapi+json;version=3.0.0",
    "application/vnd.oai.openapi+yaml;version=3.0.0",
    "application/raml+yaml;version=1.0",
    "application/vnd.google.protobuf;version=2",
    "application/vnd.google.protobuf;version=3",
]


SimpleTypes = Literal[
    "array",
    "bool",
    "integer",
    "null",
    "number",
    "object",
    "string"
]
