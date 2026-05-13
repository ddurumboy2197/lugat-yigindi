def fibonacci(n):
    if n <= 0:
        return "Fibonacci soni 0 dan katta bo'lishi kerak"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

```python
def fibonacci_optimal(n, cache = {}):
    if n <= 0:
        return "Fibonacci soni 0 dan katta bo'lishi kerak"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        result = fibonacci_optimal(n-1, cache) + fibonacci_optimal(n-2, cache)
        cache[n] = result
        return result
```

```python
def fibonacci_iterativ(n):
    if n <= 0:
        return "Fibonacci soni 0 dan katta bo'lishi kerak"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
