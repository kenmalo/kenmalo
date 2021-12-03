wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50

while True:
    print("1) wizard")
    print("2) elf")
    print("3) human")
    character = input("Choose your character: ")
    if character == "1":
        print("health:", wizard_hp)
        print("damage:", wizard_damage)
        print("You have chosen:" + wizard)
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        print("health:", elf_hp)
        print("damage:", elf_damage)
        print("You have chosen:" + elf)
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        print("health:", human_hp)
        print("damage:", human_damage)
        print("You have chosen:" + human)
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("unknown character")
while True:
    dragon_hp = dragon_hp - my_damage
    human_hp = human_hp - dragon_hp
    print("The", character, "damaged the Dragon!")
    print("The dragon hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The dragon has lost the battle")
        print("The dragon strikes back at the wizard")
        break
    if human_hp <= 0:
        print("The human has lost the battle")
        print("The human hitpoints are now:", human_hp)
    break
