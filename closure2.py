def outer_average():
	nums = []
	def inner_average(num):
		nums.append(num)
		return sum(nums) / len(nums)

	return inner_average

def_inner = outer_average()
print(def_inner(5))
print(def_inner(10))