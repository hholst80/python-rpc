# python-rpc

Python only RPC library based on ZeroMQ and Pickle

## Install

    pip install python-rpc

## Example session

Here is a use-case showing how to use the server as a compute node:
Typically we would expose an object and not a package.

Server ipython session:

    In [1]: import numpy as np
    In [2]: from pyrpc import Server
    In [3]: server = Server(np)
    In [4]: server.run()

Client `ipython` session:

    In [1]: from pyrpc import Client
    In [2]: client = Client()
    In [3]: client.ones((3, 3))
    Out[3]:
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.],
           [ 1.,  1.,  1.]])
    In [4]: client.add(Out[3], Out[3])
    Out[4]:
    array([[ 2.,  2.,  2.],
           [ 2.,  2.,  2.],
           [ 2.,  2.,  2.]])

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
