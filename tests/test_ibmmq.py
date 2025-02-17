from asyncapi.bindings.ibmmq import IbmmqDsn


values = [
    'http://my-ccdt-json-file',
    'file://myccdt.json',
    'ibmmq://qmgr1host:1414//DEV.APP.SVRCONN',
    'ibmmq://qmgr2host:1414/qm2/DEV.APP.SVRCONN'
]


for value in values:
    dsn = IbmmqDsn(value)
    print(dsn, 'authority:', dsn.authority, 'scheme:', dsn.scheme)


print(dir(dsn))
print(dsn.fragment)
print(dsn.path)
print(dsn.queue_manager)
print(dsn.mq_channel_name)
