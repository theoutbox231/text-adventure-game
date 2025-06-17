import random
name = "player"
health=100
inventory = []
gasStationLoot=["gas tank", "chocolate bar", "lighter", "first aid kit", "water","ducttape"]
Locations = ["town","shop","gas station"]
gastank = 20
class Weapon:
    def __init__(self, name, damage, ammo):
        self.name = name
        self.damage = damage
        self.ammo = ammo
    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Ammo: {self.ammo})"
class Drink:
    def __init__(self,name,health):
        self.health=health
        self.name=name
    def __str__(self):
        return f"{self.name} heals {health}%"
class Food:
    def __init__(self,name,health):
        self.health=health
        self.name=name
    def __str__(self):
        return f"{self.name} heals {health}%"
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
def offer_loot(loot_list):
    options = random.sample(loot_list,3)
    print("you rummage through shelves and find:")
    for i, item in enumerate(options,1):
        print(f"{i}.{item}")

    choice = input ("choose the items you want(e.g. 1, 3 for multiple items selections): ")
    selected_indices = [int(num.strip()) - 1 for num in choice.split() if num.strip().isdigit() and 1 <= int(num.strip())<= 3]
    chosen_items = [options[i] for i in selected_indices]
    print("\nYou Picked up:")
    for item in chosen_items: 
        print(f"- {item}")
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
    else:
        playerinput()
welcome()
