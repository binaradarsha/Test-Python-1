class Calc:

	def add(self, x, y):
		self.x = x
		self.y = y
		return x+y

c = Calc()
print("x+y = " + str(c.add(5, 7)))
print("x = " + str(c.x))
print("y = " + str(c.y))
