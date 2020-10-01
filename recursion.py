def sum_positive_numbers(n):
	if n<1:
		return n
	else:
		return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3))
print(sum_positive_numbers(5))
