#Add more pokemon --saturday
#Let user choose pokemon --sunday
#Allow team battles --monday


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



def teamBuilder():
    pokemons = [
    {
        'name': 'Pikachu',
        'attacks': {
            'thunderbolt': 30,
            'volt tackle': 20,
            'quick attack': 10,
            'shock': 15
        }
    },
    {
        'name': 'Bulbasaur',
        'attacks': {
            'vine whip': 35,
            'razor leaf': 25,
            'tackle': 15,
            'growl': 10
        }
    },
    {
        'name': 'Charmander',
        'attacks': {
            'flamethrower': 35,
            'ember': 25,
            'scratch': 15,
            'smokescreen': 10
        }
    },
    {
        'name': 'Squirtle',
        'attacks': {
            'water gun': 30,
            'bubble beam': 20,
            'tackle': 15,
            'withdraw': 10
        }
    },
    {
        'name': 'Jigglypuff',
        'attacks': {
            'sing': 10,
            'pound': 20,
            'double slap': 15,
            'body slam': 25
        }
    },
    {
        'name': 'Meowth',
        'attacks': {
            'scratch': 15,
            'bite': 20,
            'pay day': 25,
            'fury swipes': 30
        }
    },
    {
        'name': 'Psyduck',
        'attacks': {
            'water pulse': 30,
            'confusion': 25,
            'scratch': 15,
            'disable': 10
        }
    },
    {
        'name': 'Gengar',
        'attacks': {
            'shadow ball': 35,
            'lick': 20,
            'hypnosis': 10,
            'dark pulse': 30
        }
    },
    {
        'name': 'Machop',
        'attacks': {
            'karate chop': 30,
            'low kick': 25,
            'seismic toss': 35,
            'focus energy': 10
        }
    },
    {
        'name': 'Eevee',
        'attacks': {
            'quick attack': 20,
            'bite': 25,
            'tackle': 15,
            'sand attack': 10
        }
    },
    {
        'name': 'Snorlax',
        'attacks': {
            'body slam': 40,
            'hyper beam': 50,
            'headbutt': 25,
            'rest': 10
        }
    },
    {
        'name': 'Dragonite',
        'attacks': {
            'dragon claw': 40,
            'wing attack': 30,
            'thunder punch': 25,
            'hyper beam': 50
        }
    }
]
    
    for i in range(len(pokemons)):
        print(f"{i+1}: {pokemons[i]['name']}")
		
    
    team = []
	
    while len(team) < 6:
        pokemon = int(input("Enter the number of the pokemon you want to add to your team: /or enter '9999' to finish"))
        if pokemon == 9999:
            break
        
        team.append(pokemons[pokemon])
    return team


def main():
    userTeam = teamBuilder()
    for x in userTeam:
        print(x)



	#oppTeam = teamBuilder()
	#battle(userTeam, oppTeam)
	#for i in range(len(pokemons)):
	#	print(f"{i+1}: {pokemons[i]['name']}")
	#user = int(input("Enter the number of the pokemon you want to choose: "))
	#opp = int(input("Enter the number of the pokemon you want to battle: "))

	#if 1 <= user <= len(pokemons) and 1 <= opp <= len(pokemons):
	#	user_pokemon = Pokemon(pokemons[user-1]['name'], 100, pokemons[user-1]['attacks'])
	#	opp_pokemon = Pokemon(pokemons[opp-1]['name'], 100, pokemons[opp-1]['attacks'])


	#battle(user_pokemon, opp_pokemon)

if __name__ == "__main__":
	
    main()