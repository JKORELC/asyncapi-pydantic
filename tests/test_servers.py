from asyncapi.common import AsyncApiBase
from asyncapi.servers import Servers


servers = Servers.from_yaml("tests/servers.yaml")
print(servers)
print(servers.model_dump_json())

print(servers.production.host, servers.production.protocol)
