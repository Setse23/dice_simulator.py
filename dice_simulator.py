from random import randint 

class Dice():
	def __init__(self, rolls, sides=6):
		self.num_of_rolls = rolls
		self.sides = sides
		self.rolls = []

	def roll(self):
		self.rolls.append(randint(1,self.sides))

	def repeat(self):
		for n in range(self.num_of_rolls):
			self.roll()

	def roll_summary(self):
		print('Rolls\n')
		for num in range(1, self.sides + 1):
			print(f'{num} --> {self.rolls.count(num)}\n')

d1 = Dice(100)
d1.repeat()
d1.roll_summary()