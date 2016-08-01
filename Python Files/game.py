from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game:

	def setup(self):
		self.player = Character()
		self.monsters = [

			Goblin(),
			Troll(),
			Dragon()

		  ]

		self.monster = self.get_next_monster()


	def get_next_monster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None 


	def monster_turn(self):
		# Check to see if the monster attacks
		#If, so tell the plater
		# Check if the player wants to dodge
		# If so, see if the dodge was successful
		# If so, continue to move on
		# if it's not, remove one player hit point 
		# if the monster isn't attacking tell that to the player too.

	def player_turn(self):
		# Le tthe player attack, rest, or quit
		# If they attack:
		# See if the attack is successful
		# If so, see if the monster dodges
		# If dodged, print that
		# if not dodged, subtract the right number of hitpoints from said monster
		# If not a good attack, tell the player
		# If they rest:
		# Call THe player .rest() method 
		# If They quit, exit the game 
		#If anything else re-run this method

	def cleanup(self):
		# if the monster has no more hp:
		# up the players xp
		# print a message 
		# get a new monster

	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters):

			print(self.player)
			self.monster_turn()
			self.player_turn()
			self.cleanup()

		if self.player.hit_points:
			print("You Win!")
		elif self.monsters or self.monster:
			print("You Lose...")
			



