from setuptools import find_packages, setup

setup(
    author='Maksymilian Sawicz',
    name='flask_redis_caching',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'flask-redis'
    ]
)