from setuptools import find_packages, setup

setup(
    author='Maksymilian Sawicz',
    name='flask_redis_caching',
    description='Flask Redis Caching is a Python library that provides caching functionalities using Redis for storing and retrieving cached values in Flask applications.',
    long_description='See https://github.com/0x1618/flask-redis-caching',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'flask-redis'
    ]
)