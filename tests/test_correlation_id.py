from asyncapi.common import CorrelationID


correlation = CorrelationID.from_yaml("tests/correlation_id.yaml")
print(correlation)
print(correlation.model_dump_yaml())
