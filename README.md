# python-rpc

Python only RPC library based on ZeroMQ and Pickle

## Install

    pip install python-rpc

## TODO

* Stack trace on client side.
* Factory function for servers.
* GC client objects -> GC on server.
* isinstance compatibility with server object.

## Known limitations

* Does not work with:
  - generators
  - async
  - dictionaries.
  - anything else Pickle cannot serialize.
