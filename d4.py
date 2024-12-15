import time

start = time.perf_counter()
for i in range(100):
    import task
end = time.perf_counter()
print(f"Обязательное: {end - start}")

start = time.perf_counter()
for i in range(100):
    import d1
end = time.perf_counter()
print(f"Доп 1: {end - start}")

start = time.perf_counter()
for i in range(100):
    import d2
end = time.perf_counter()
print(f"Доп 2: {end - start}")

start = time.perf_counter()
for i in range(100):
    import d3
end = time.perf_counter()
print(f"Доп 3: {end - start}")