import random # import the random module to select loot randomly
name = "player"
health=100
inventory = []
Locations = ["town","shop","gas station"]
gastank = 20
# base item class for all inventory objects 

class Item: 
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
class Weapon(Item):
    def __init__(self, name, damage, ammo):
        super().__init__(name)
        self.damage = damage
        self.ammo = ammo
    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Ammo: {self.ammo})"
class Drink(Item): 
    def __init__(self,name,health):
        super().__init__(name)
        self.health=health
    def __str__(self):
        return f"{self.name} heals {health}%"
class Food(Item):
    def __init__(self,name,health):
        super().__init__(name)
        self.health=health
    def __str__(self):
        return f"{self.name} heals {health}%"
class GasTank(Item):
    def __init__(self, amount):
        super().__init__("gas tank")
        self.amount = amount
    def __str__(self):
        return f"{self.name} ({self.amount}%full)"
    
gasStationLoot = [
    GasTank(40), # a gas tank with 40% of gas
    Food("choclate bar",20),
    Item("lighter"),
    Item("first aid kit"),
    Item("water"),
    Item("duct tape roll")

]
pistol=Weapon("m1911",15,6)
juice=Drink("juicebox",15)
chocolate=Food("choclate bar",20)
inventory.append(pistol)
inventory.append(juice)
location="home"
def welcome():
    print("welcome player, What shall we call you?")
    name = input()
    print(f"hello {name}!")
    playerinput()
def add__to__inventory(item):
    inventory.append(Item)
    print(f"{item} has been added to your inventory!")
# Fuction to offer the player 3 random loot items and let them choose which one to do
def offer_loot(loot_list): 
# Randomly choose 3 diffrent items from the loot list
    options = random.sample(loot_list,3)
    
    # Show the player what they looked for
    print("you rummage through shelves and find:")
    # Enumerate start at one instead of zero of for player-freindly numbering 
    for i, item in enumerate(options,1):
        print(f"{i}.{item}") # display options: 1. item, 2. item, etc.

    # Ask the player which items they want to tale (they can choose muliple)
    choice = input ("choose the items you want(e.g. 1, 3 for multiple items selections): ")
    # Process the player's input: 
    # - split the input string by spaces (e.g. "1 3 ["1, "3"])
    # - strip whitespace and check if each part is a digit
    # = convert it to an integer, subtract 1 (to match python code indexing:) 0 - based)
    # - onley keep valid selections (1 to 3) 
    selected_indices = [int(num.strip()) - 1 for num in choice.split() if num.strip().isdigit() and 1 <= int(num.strip())<= 3]
    chosen_items = [options[i] for i in selected_indices]
    print("\nYou Picked up:")
    for item in chosen_items: 
        print(f"- {item}")
        add__to__inventory(item)
def playerinput():
    global location 
    prompt = input()
    if prompt == "stats":
        print(f"Name: {name}")
        print(f"Health: {health}")
        for i in inventory:
            print(i)
        print(f"gas: {gastank}%")
    if prompt == "map":
        print(f"you at {location}")
        print(f"all Locations:{Locations}")
    if prompt=="gas station":
      
        location = "gas station"
        print("you are in a gas station")
    if prompt=="loot" and location != "home":
        print("looting")
        offer_loot(gasStationLoot)
    playerinput()
welcome()
