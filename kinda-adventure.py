import random
import time

def combat(hp, ehp, s1damage, s2damage):
    while hp > 0 and ehp > 0:
        print(f"Your HP: {hp}, Enemy HP: {ehp}")
        skil = input ("Press 1 or 2 to use your respective skills: ")
        if skil == "1":
            ehp -= s1damage
            print(f"You used Skill 1 and dealt {s1damage} damage.")
        elif skil == "2":
            ehp -= s2damage
            print(f"You used Skill 2 and dealt {s2damage} damage.")

def slow(text, delay = 0.1):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()   

class hero:
    def __init__(self, title, s1, s2, s3):
        self.title = title
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

#Assign instances
mage1 = hero("Ardent Warden","Flame Lash", "Ember Ring", "Infernal Crown")
fighter = hero("Dreadbreaker", "Breakers's Rush", "Echo Strike", "Ruinwheel")
ranged = hero("Zephyrborn", "Gale Shot", "Cyclone Step", "Eye of the Storm")
assasin = hero("Nightshade", "Twinfang", "Shroudwalk", "Eclipse Cleave")

lore = "Centuries ago, the world of Elarion was united under the radiant light of the Celestial Flame, a divine force that balanced magic, might, and shadow. But when the Flame was shattered in a cataclysmic betrayal, the realms split, and chaos reigned."
slow(lore)
print("\n")
name = input("Enter your name: ")
slow(f"Hello, {name}. Welcome to the game.")
print("\n")
slow("From the tragedy that happened, classes were born in order to make the world of Elarion united again. Mage, Fighter, Front, Ranged, Assasin, and Support people belonging to these classes are the people working towards that goal.")
print("\n")
#ask for input
cla = input("Please select your class. : ").capitalize()

#store choices
character = []

if cla == "Mage":
    slow(f"{mage1.title} wielding Fire Magic has the folowing skills:")
    print(mage1.s1, "a powerful single-target spell that scorches enemies with a fiery lash.")
    print(mage1.s2, "a defensive spell that creates a barrier of flames.")
    print(mage1.s3, "an ultimate spell that engulfs the battlefield in a firestorm.")
    character.extend([mage1.title, mage1.s1, mage1.s2, mage1.s3])
        
elif cla == "Fighter":
    slow(f"{fighter.title} a Melee DPS has the folowing skills:")
    print(fighter.s1, "a swift strike that deals damage to a single foe.")
    print(fighter.s2, "a powerful blow that damages all enemies in front.")
    print(fighter.s3, "an unstoppable charge that knocks down all in your path.")
    character.extend([fighter.title, fighter.s1, fighter.s2, fighter.s3])

elif cla == "Ranged":
    slow(f"{ranged.title}, the Wind Archer has the folowing skills:")
    print(ranged.s1, "a precise shot that deals damage from afar.")
    print(ranged.s2, "a quick dash that increases evasion.")
    print(ranged.s3, "a storm of arrows that rains down on enemies.")
    character.extend([ranged.title, ranged.s1, ranged.s2, ranged.s3])
   
elif cla == "Assasin":
    slow(f"{assasin.title}, the Umbral Assasin has the folowing skills:")
    print(assasin.s1, "a deadly strike that deals massive damage to a single target.")
    print(assasin.s2, "a stealthy movement that increases evasion.")
    print(assasin.s3, "an ultimate ability that unleashes a flurry of strikes.")
    character.extend([assasin.title, assasin.s1, assasin.s2, assasin.s3])

else:
    print("Class not available")
    print("Please restart the game and select a valid class. Don't joke around this time!")
print("\n")
slow("Congratulations. Let's head out to the world!")
print("\n")

#initialize stats
life = 100
goblin = 25
wolf = 50
damage = 10

slow("Heading to the town, you went through a forest and found a chest. Test your luck!")
chest = ["Stone", "Orb", "Robe"]
slow(input("The chest contains the following: Stone, Orb, and Robe. Press Enter to get an item!"))
item = random.choice(chest)
if item == "Stone":
    slow("Ooof! Bad luck, you got Stone, which does nothing.")
elif item == "Orb":
    damage *= 2
    slow("You got Orb, your damage has been doubled.")
elif item == "Robe":
    life += 50
    slow("You got Robe, your HP has been increased by 50 ")

slow(f"You encountered a Goblin! Prepare for combat, {name}!")
combat(life, goblin, damage, damage * 2)
slow("You defeated the Goblin! You found a healing potion and restored 20 HP.")