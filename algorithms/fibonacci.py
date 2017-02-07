


memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if n not in memory:
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]

print fibonacci(50)

print memory