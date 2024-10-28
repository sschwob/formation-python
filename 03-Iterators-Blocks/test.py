numbers = [1, 2, 3]
print(numbers)

def multiply_by_2(x):
  return x * 2

result = list(map(multiply_by_2, numbers))
print(result)
