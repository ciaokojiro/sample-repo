def power(exponent):

	def inner_power(num):
		print(num ** exponent)

	return inner_power

f = power(5)
print(f(4))


