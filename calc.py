class Calc:
	def add(self, x, y):
		self.x = x
		self.y = y
		return x+y

c = Calc()
print("x = " + c.x)
print("y = " + c.y)
print(c.add(5, 7))
