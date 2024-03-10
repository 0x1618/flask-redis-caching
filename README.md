# Flask Redis Caching

## Overwiew
Flask Redis Caching is a Python library that provides caching functionalities using Redis for storing and retrieving cached values in Flask applications. This library aims to simplify caching operations and improve application performance by reducing database queries and computation time through caching.

## Installation
You can install Flask Redis Caching via pip:

``` python
pip install flask-redis-caching
```

## Features
- ***Dynamic Cache Key Generation***: Can generate cache keys dynamically based on input parameters or custom logic, enabling flexible caching strategies (cache_key_getter param).
- Redis Integration: Seamless integration with Redis for efficient storage and retrieval of cached values.
- Decorator-based Caching: Easily cache the results of functions and methods using decorator syntax, reducing boilerplate code.
- Automatic Cache Expiration: Set expiration times for cached values, ensuring data remains fresh and relevant.

## Usage
### Initialization
Initialize Flask Redis Caching in your Flask application by passing the Flask app instance to the `RedisCaching` constructor:

``` python
from flask import Flask
from flask_redis_caching import RedisCaching

app = Flask(__name__)
app.config['CACHING_REDIS_URL'] = "redis://:@localhost:6379/0"
redis_caching = RedisCaching(app)
```
Or you can do it later by `redis_caching.init_app(app)` function.
``` python
redis_caching = RedisCaching()
redis_caching.init_app(app)
```

### Caching Decorators
Class Method Caching
You can cache the result of a class method using the cached_result decorator. Example:

``` python
class DynamicValues:
    def __init__(self, uuid: str) -> None:
        self.uuid = uuid

    @redis_caching.cached_result(
        cache_key_getter=lambda self: self.uuid + '-long_function', # Dynamic cache_key, for e.g you can access here the class object.
        expires_in=60,
        is_class_function=True
    )
    def long_function(self):
        # Your expensive computation here
```

Function Caching
Similarly, you can cache the result of a function using the cached_result decorator. Example:

```python
@redis_caching.cached_result(cache_key="long_function", is_class_function=False, expires_in=30) # cache_key_getter can be used aswell.
def long_function():
    # Your expensive computation here
```

### Cache Management
You can manually expire a cached value using the make_cache_expired method:

```python
def function_that_expires_the_cache():
    redis_caching.make_cache_expired('long_function')
```

### Integration with Flask Routes
Integrate Flask Redis Caching with your Flask routes to cache the results of route handlers:
```python
from time import sleep

from flask import Flask
from flask_redis_caching import RedisCaching

app = Flask(__name__)
app.config['CACHING_REDIS_URL'] = "redis://:@localhost:6379/0"
redis_caching = RedisCaching(app)

@redis_caching.cached_result(cache_key="long_function", is_class_function=False, expires_in=30)
def long_function():
    sleep(5)

    return "Lemme cache this"

@app.route('/')
def route():
    result = long_function()  # If the cached value is present, it will be returned; otherwise, the function will be executed.
    return result

```

### Configuration

RedisCaching allows you to configure Redis connection settings using Flask application configuration. By default, it looks for configuration variables prefixed with `CACHING_REDIS_URL`. You can customize the configuration prefix by passing the `config_prefix` parameter during initialization.

### Logging
RedisCaching provides optional logging to track caching operations. Logging is enabled by default, but you can disable it by passing `log=False` during initialization.

### Contributing
If you have any suggestions, bug reports, or contributions, feel free to open an issue or create a pull request on GitHub.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
