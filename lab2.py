import random

def get_int_input(prompt):
    """Get integer input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

numLives = 10
mNumLives = 12

diceOptions = [1, 2, 3, 4, 5, 6]

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

combatStrength = get_int_input("Enter your combat Strength: ")
mCombatStrength = get_int_input("Enter the monster's combat Strength: ")

input("Roll the dice to select your weapon (Press enter)")
weaponRoll = random.choice(diceOptions) - 1
heroWeapon = weapons[weaponRoll]
combatStrength += weaponRoll + 1
print(f"You rolled a {weaponRoll + 1}, selecting the weapon: {heroWeapon}")

if weaponRoll <= 1:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 3:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if heroWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your weapon (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength

    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
