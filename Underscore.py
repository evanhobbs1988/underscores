# class Underscore:
#     def map(self):
#         # your code here
#     def reduce(self):
#         # your code here
#     def find(self):
#         # your code here
#     def filter(self):
#         # your code
#     def reject(self):
#         # your code
# you just created a library with 5 methods!
# let's create an instance of our class_ = Underscore() 
# yes we are setting our instance to a variable that is an underscoreevens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

# Your assignment is to implement the 5 methods above using delegating callbacks. You will have to modify the 5 methods to take in an array and a callback. Use what you learned in the previous chapter about callbacks to complete the assignment.

# One important concept that we want you to learn through this assignment is how to pass data to and from callbacks. You pass data to a callback with a parameter and you pass data from the callback back to the parent function with a return. While you are going through this assignment pay close attention to this relationship.

# To understand what each method does, please refer to the underscore library. Note that your method does not have to be as robust as underscore's
# you just need to get the base functionality working. Therefore for most methods you will only have the list and a lambda as parameters, and for the lambda you will pass in each element and potentially a "memo" also known as a "collector".

# Note that some of these functions already exist in Python. We want you to explore how you might implement these yourself. Be aware that these tools exist to help work in a design idiom known as "functional programming". It's not something that we cover here, but is a topic you may want to explore on your own. It is mainly used in data science in recent years.


class Underscore(object):
	def map(self, list, callback):
		new_list = []
		for i in list:
			new_list.append(callback(i))
		print new_list

	def reduce(self, list, callback):
		new_list = []
		total = 0
		for i in list:
			new_list.append(callback(i))
		for j in new_list:
			total += j
		print total

	def find(self, list, callback):
		for i in range(0, len(list)):
			if callback(list[i]) == True:
				print list[i]
				break
			else:
				return False

	def filter(self, list, callback):
		result = []
		for i in range(0, len(list)):
			if callback(list[i]) == True:
				result.append(list[i])
		print result

	def reject(self, list, callback):
		result = []
		for i in range(0, len(list)):
			if callback(list[i]) != True:
				result.append(list[i])
		print result



maps = _.map([1, 2, 4, 8, 6], lambda x: x % 2 == 0)
evens = _.filter([1, 2, 4, 8, 6], lambda x: x % 2 == 0)
odds = _.reject([1, 2, 4, 3, 8, 6], lambda x: x % 2 == 0)
findItem = _.find([2, 4, 8, 6, 7], lambda x: x % 2 == 0)
reduceItem = _.reduce([47, 11, 42, 13], lambda x: x**2)
