import webbrowser


class UnknownProtocol(RuntimeError):
    def __init__(self, protocol_name):
        super().__init__(f'Unknown protocol {protocol_name}')


class Protocol:
    table = {}

    def __init_subclass__(cls, *, protocol_name, **kwargs) -> None:
        super.__init_subclass__(**kwargs)
        cls.protocol_name = protocol_name
        Protocol.table[protocol_name] = cls

    @staticmethod
    def find_protocol(protocol_name):
        table = Protocol.table
        if protocol_name not in table:
            raise UnknownProtocol(protocol_name)
        return Protocol.table[protocol_name]()


class _UrlProtocol(Protocol, protocol_name='url'):
    def fetch(self, node):
        url = node.url
        webbrowser.open(url)


def apply_protocol(node):
    if not hasattr(node, 'protocol'):
        print(f'Node has no protocol :-(')
    else:
        protocol_name = node.protocol
        protocol = Protocol.find_protocol(protocol_name)
        protocol.fetch(node)
