#Add more pokemon --saturday
#Let user choose pokemon --sunday
#Allow team battles --monday


class Pokemon:
    def __init__(self, name, health, attacks, max_health=100):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attacks = attacks

    def getName(self):
        return self.name

    def getAttacks(self):
        return self.attacks

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def attack(self, target, attack_name):
        attack_power = self.attacks.get(attack_name)
        if attack_power:
            damage = attack_power
            target.health -= damage
            print(f"{self.name} used {attack_name} and dealt {damage} to {target.name}")
            if target.health <= 0:
                print(f"{target.name} fainted!")
            else:
                print(f"{target.name} has {target.health} HP left!")
def battle_menu(current_pokemon, team, items):
    while True:
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Switch Pokemon")
        print("3. Use Item")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return ("attack", None)
            elif choice == 2:
                new_pokemon = choose_next_pokemon(team, current_pokemon, switching=True)
                if new_pokemon:
                    return ("switch", new_pokemon)
                # If no switch was made, loop back to menu
            elif choice == 3:
                item = use_item_menu(items, current_pokemon)
                if item:
                    return ("item", item)
            else:
                print("Invalid choice. Please choose 1-3.")
        except ValueError:
            print("Please enter a valid number.")

def use_item_menu(items, pokemon):
    if not items:
        print("No items available!")
        return None
    
    while True:
        print("\nAvailable Items:")
        for i, (item, quantity) in enumerate(items.items()):
            print(f"{i+1}. {item} (x{quantity})")
        print("0. Back")
        
        try:
            choice = int(input("Choose an item to use (0 to go back): "))
            if choice == 0:
                return None
            
            if 1 <= choice <= len(items):
                item_name = list(items.keys())[choice-1]
                if items[item_name] > 0:
                    items[item_name] -= 1  # Use one item
                    if items[item_name] == 0:  # Remove if no more left
                        del items[item_name]
                    return item_name
                else:
                    print("No more of this item left!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")

def apply_item(item_name, pokemon):
    effects = {
        "Potion": 20,
        "Super Potion": 50,
        "Hyper Potion": 100,
        "Max Potion": 999
    }
    
    if item_name in effects:
        old_health = pokemon.health
        pokemon.heal(effects[item_name])
        healed = pokemon.health - old_health
        print(f"Used {item_name} on {pokemon.name}! Restored {healed} HP!")
        return True
    return False            

def choose_next_pokemon(team, current_pokemon, switching=False):
    """Choose next Pokemon after one has fainted or for switching"""
    if switching:
        print(f"\nChoose a Pokemon to switch to:")
    else:
        print(f"\n{current_pokemon.name} has fainted! Choose your next Pokemon:")
    
    active_pokemon = []
    
    # Filter out fainted Pokemon and current Pokemon
    for pokemon in team:
        if pokemon['name'] != current_pokemon.name:
            active_pokemon.append(pokemon)
    
    if not active_pokemon:
        if switching:
            print("No other Pokemon available to switch to!")
        return None
        
    while True:
        for i, pokemon in enumerate(active_pokemon):
            print(f"{i}: {pokemon['name']}")
        print("Enter 9999 to cancel switch") if switching else None
        try:
            choice = int(input("Choose your Pokemon: "))
            if switching and choice == 9999:
                return None
            if 0 <= choice < len(active_pokemon):
                return Pokemon(active_pokemon[choice]['name'], 100, active_pokemon[choice]['attacks'])
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def choose_first_pokemon(team):
    """Let user choose their first Pokemon from their team"""
    while True:
        for i, pokemon in enumerate(team):
            print(f"{i}: {pokemon['name']}")
        try:
            print("Choose your Pokemon:")
            choice = int(input())
            if 0 <= choice < len(team):
                return Pokemon(team[choice]['name'], 100, team[choice]['attacks'])  # Create Pokemon instance
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

	

	
def battle(user_team, opp_team):
    # Initialize items
    user_items = {
        "Potion": 3,
        "Super Potion": 2,
        "Hyper Potion": 1,
        "Max Potion": 1
    }
    opp_items = user_items.copy()  # Give opponent same items
    
    print("\nPlayer 1: Choose your starting Pokemon!")
    pokemon1 = choose_first_pokemon(user_team)
    print("\nPlayer 2: Choose your starting Pokemon!")
    pokemon2 = choose_first_pokemon(opp_team)
    
    user_active = [p for p in user_team if p['name'] != pokemon1.name]
    opp_active = [p for p in opp_team if p['name'] != pokemon2.name]
    
    print(f'\n{pokemon1.name} vs {pokemon2.name}')
    turn = 1

    while True:
        display_health(pokemon1, pokemon2)
        
        if turn % 2 != 0:
            print(f"\n{pokemon1.name}'s turn")
            action, result = battle_menu(pokemon1, user_active, user_items)
            
            if action == "attack":
                attack = choose_attack(pokemon1)
                pokemon1.attack(pokemon2, attack)
            elif action == "switch":
                pokemon1 = result
                print(f"Switched to {pokemon1.name}!")
            elif action == "item":
                if apply_item(result, pokemon1):
                    print(f"{pokemon1.name} now has {pokemon1.health} HP!")
                else:
                    continue  # Invalid item, don't end turn
            
            if pokemon2.health <= 0:
                print(f"{pokemon2.name} has fainted!")
                pokemon2 = choose_next_pokemon(opp_active, pokemon2)
                if not pokemon2:
                    print("Player 1 wins! All opponent's Pokemon have fainted!")
                    break
                opp_active = [p for p in opp_active if p['name'] != pokemon2.name]
                
        else:
            print(f"\n{pokemon2.name}'s turn")
            # Simple AI for opponent: prefer healing at low HP, otherwise attack
            if pokemon2.health < 30 and opp_items:
                for potion in ["Max Potion", "Hyper Potion", "Super Potion", "Potion"]:
                    if potion in opp_items:
                        apply_item(potion, pokemon2)
                        opp_items[potion] -= 1
                        if opp_items[potion] == 0:
                            del opp_items[potion]
                        break
            else:
                attack = choose_attack(pokemon2)
                pokemon2.attack(pokemon1, attack)
            
            if pokemon1.health <= 0:
                print(f"{pokemon1.name} has fainted!")
                pokemon1 = choose_next_pokemon(user_active, pokemon1)
                if not pokemon1:
                    print("Player 2 wins! All your Pokemon have fainted!")
                    break
                user_active = [p for p in user_active if p['name'] != pokemon1.name]
        
        turn += 1


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
    oppTeam = teamBuilder()
	
    battle(userTeam, oppTeam)
    

	

if __name__ == "__main__":
	
    main()