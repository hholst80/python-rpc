import pickle
import zmq

def _callable(*args, **kwargs):
    raise NotImplementedError()

class Server(object):
    def __init__(self, proxy_object, *, address='tcp://0.0.0.0:4000'):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(address)
        self._context = context
        self._socket = socket
        self._proxy_object = proxy_object

    def run(self):
        socket = self._socket
        po = self._proxy_object
        while True:
            packed_msg = socket.recv()
            msg = pickle.loads(packed_msg)
            op, name = msg[0:2]
            if op == 'call':
                args, kwargs = msg[2:4]
            else:
                assert op == 'getattr'
            try:
                msg = getattr(po, name)
                if op == 'call':
                    msg = msg(*args, **kwargs)
            except Exception as e:
                msg = e
            if callable(msg):
                msg = _callable
            packed_msg = pickle.dumps(msg)
            socket.send(packed_msg)


class Client(object):
    def __init__(self, *, address='tcp://127.0.0.1:4000'):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(address)
        self._context = context
        self._socket = socket

    def __dir__(self):
        """
        __dir__ is not fetched via __getattribute__
        """
        socket = self._socket
        msg = ('getattr', '__dir__')
        packed_msg = pickle.dumps(msg)
        socket.send(packed_msg)
        packed_msg = socket.recv()
        msg = pickle.loads(packed_msg)
        if isinstance(msg, Exception):
            raise msg
        if callable(msg):
            def wrapper(*args, **kwargs):
                msg = ('call', '__dir__', (), {})
                packed_msg = pickle.dumps(msg)
                socket.send(packed_msg)
                packed_msg = socket.recv()
                msg = pickle.loads(packed_msg)
                if isinstance(msg, Exception):
                    raise msg
                return msg
            return wrapper()
        return msg

    def __getattribute__(self, name):
        if name == '_socket':
            return super().__getattribute__(name)
        socket = self._socket
        msg = ('getattr', name)
        packed_msg = pickle.dumps(msg)
        socket.send(packed_msg)
        packed_msg = socket.recv()
        msg = pickle.loads(packed_msg)
        if isinstance(msg, Exception):
            raise msg
        if callable(msg):
            def wrapper(*args, **kwargs):
                msg = ('call', name, args, kwargs)
                packed_msg = pickle.dumps(msg)
                socket.send(packed_msg)
                packed_msg = socket.recv()
                msg = pickle.loads(packed_msg)
                if isinstance(msg, Exception):
                    raise msg
                return msg
            return wrapper
        return msg
