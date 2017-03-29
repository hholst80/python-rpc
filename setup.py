from setuptools import find_packages, setup

setup(
    name='python-rpc',
    version='0.329.2',
    description='Python only RPC library based on ZeroMQ and Pickle',
    url='https://github.com/hholst80/python-rpc',
    author='Henrik Holst',
    author_email='hholst80@gmail.com',
    license='The Unlicense',
    packages=find_packages(),
    install_requires=['pyzmq']
)
