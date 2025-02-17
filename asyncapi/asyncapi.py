from pydantic import (
    Field,
    EmailStr,
    HttpUrl,
)


from asyncapi.common import (
    AsyncApiBase,
    AsyncApiExtendable,
    ExternalDocumentation,
    Reference,
    Tags,
)
from asyncapi.channels import Channels
from asyncapi.components import Components
from asyncapi.servers import Servers
from asyncapi.operations import Operations


class Contact(AsyncApiBase):
    name: str | None = Field(None)
    url: HttpUrl | None = Field(None)
    email: EmailStr | None = Field(None)


class License(AsyncApiExtendable):
    name: str
    url: HttpUrl


class Info(AsyncApiBase):
    title: str
    version: str
    description: str | None = Field(None)
    terms_of_service: str | None = Field(None)
    contact: Contact | None = Field(None)
    license: License | None = Field(None)
    tags: Tags | None = Field(None)
    external_docs: ExternalDocumentation | Reference | None = Field(None)


class AsyncApi(AsyncApiBase):
    asyncapi: str = Field("3.0.0")
    id_: str
    default_content_type: str
    components: Components
    servers: Servers
    channels: Channels
    operations: Operations
    info: Info
