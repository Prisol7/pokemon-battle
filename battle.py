class Pokemon:
	#a class for pokemon
	def __init__(self, name, health, attacks):
		self.name = name
		self.health = health
		self.attacks = attacks

	def getName(self):
		return self.name

	def getAttacks(self):
		return self.attacks

	def attack(self, target, attack_name):
		attack_power = self.attacks.get(attack_name)
		if attack_power:
			#add damage calculations later
			damage = attack_power
			target.health -= damage
			print(f"{self.name} used {attack_name} and daelt {damage} to {target.name}")
			if target.health <= 0:
				print(f"{target.name} fainted!")
			else:
				print(f"{target.name} powers on!")


	
def battle(pokemon1, pokemon2):
	print(f'{pokemon1.name} vs {pokemon2.name}')
	turn = 1

	while pokemon1.health > 0 and pokemon2.health > 0:
		if turn%2 != 0:
			print(f"{pokemon1.name}'s turn")
			attack = choose_attack(pokemon1)
			pokemon1.attack(pokemon2, attack)
			display_health(pokemon1, pokemon2)
			if pokemon2.health <= 0:
				break
			turn += 1
		else:
			print(f"{pokemon2.name}'s turn")
			attack = choose_attack(pokemon2)
			pokemon2.attack(pokemon1, attack)
			display_health(pokemon1, pokemon2)
			if pokemon1.health <= 0:
				break
			turn += 1
	if pokemon1.health <= 0:
		print(f"{pokemon1.name} wins")
	else:
		print(f"{pokemon1.name} wins")


def choose_attack(pokemon):
	available_attacks = list(pokemon.getAttacks().keys())
	if len(available_attacks) == 9:
		print(f'{pokemon.name} has no moves')
		return None
	while True:
		print('available_attacks: ')
		for i, attack in enumerate(available_attacks):
			print(f'{i+1}: {attack}')
		try:
			attack_chosen = int(input(f"Enter the number of the attack you want to choose:"))
			if 1 <= attack_chosen <= len(available_attacks):
				print(f"{available_attacks[attack_chosen - 1]} pickde")
				return available_attacks[attack_chosen -1]
			else:
				print("Invalid choice. Try again")
		except ValueError:
			print("Invalid input. Enter a valid number")

def display_health(pokemon1, pokemon2):
	print(f"{pokemon1.name}: health: {pokemon1.health}")
	print(f"{pokemon2.name}: health: {pokemon2.health}")



def main():
	pikachu_attacks = {
	'thunderbolt': 30,
	'volt tackle': 20,
	'quick attack': 10,
	'shock': 15
	} 

	bulbasuar_attacks = {
	'vine whip': 35,
    'razor leaf': 25,
    'tackle': 15,
    'growl': 10,
	}
	pikachu = Pokemon('pikachu', 100, pikachu_attacks)
	bulbasuar = Pokemon('bulbasuar', 120, bulbasuar_attacks)
	battle(pikachu, bulbasuar)

if __name__ == "__main__":
    main()