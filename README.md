# PyTime
A Github repository testing just how fast different Python functions are!

## Testing Methodology

This is a minimal example of the testing methodology.

```
import time

total_execution_time = 0
for _ in range(10_000_000):
  start = time.perf_counter()

  function_to_benchmark()

  end = time.perf_counter()
  total_execution_time += end-start

print(total_execution_time/10_000_000)
```

Gives an uncertainty of ±0.0000000005 seconds
