import functools
import random
import time


def retry(times=3, delay=1):
    """Decorator that retries a function if it raises an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)  # optional delay between retries
                    else:
                        raise  # re-raise after last attempt
        return wrapper
    return decorator

@retry(times=3, delay=0.5)
def risky_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

print(risky_function())
