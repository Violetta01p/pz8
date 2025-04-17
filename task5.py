composite_numbers = [x for x in range(2, 101) if len([d for d in range(1, x + 1) if x % d == 0]) > 2]
print("Складні числа від 1 до 100:")
print(composite_numbers)
