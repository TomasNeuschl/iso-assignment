import pickle
from functools import wraps


def cache_result(redis_client, ttl=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate a cache key based on function arguments
            cache_key = f"{func.__name__}:{args}:{kwargs}"

            # Check if the result is cached
            cached_result = redis_client.get(cache_key)
            if cached_result is not None:
                # Deserialize the cached result from bytes to the original data type
                return pickle.loads(cached_result)

            # Calculate the result if not cached
            result = func(*args, **kwargs)

            # Serialize the result to bytes before caching
            serialized_result = pickle.dumps(result)

            # Cache the result with the specified TTL (time to live)
            redis_client.setex(cache_key, ttl, serialized_result)

            return result

        return wrapper

    return decorator
