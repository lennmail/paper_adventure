# this is the main file. we will start coding shortly

# what is your name
# choose your character

# Initial Plot
# stolen holocron, hidden on junk planet "9-NR3W".
        # jedi: sent by the council to retrieve the artifact
        # bounty hunter: mission from the huts
        # smuggler: his comrade stole the artifact, came to retrieve it
    # every character has the following stats:
        # Karma
    #certain choices are only possible with certain characters

# maybe implement input function here

def choose_character():
    #define a function which facilitates character choice
    print("Welcome to our text adventure!")
    print("The game is contained to your terminal. Enlarge it and enjoy!")
    print("The following story takes place in the STAR WARS universe.")
    print()
    print()
    name = input("What is your name?: ")
    print("Hello, {}. Before your adventure starts, choose your character:".format(name))
    print()
    print("Option 1: Jedi.")
    print("This Jedi's agility, wisdom, and control of the force is unmatched. He is quite popular with upright citizens.")
    print()
    print("Option 2: Bounty Hunter.")
    print("Bounty Hunters are known to be strong and intimidating individuals. He isn't the smartest but his gadgets are helpful.")
    print()
    print("Option 3: Smuggler")
    print("The smuggler is scrawny and weak. He wields a blaster and is highly charismatic. He has an affinity for technology.")
    print()
    #check if input is okay
    while True:
        try: 
            choice = int(input("Please type 1, 2, or 3 to denote your choice: "))
            if choice in (1, 2, 3):
                if choice == 1:
                    character = "Jedi"
                elif choice == 2:
                    character = "Bounty Hunter"
                elif choice == 3:
                    character = "Smuggler"
            else:
                print("Please input only integers between 1 and 3.")
        except ValueError:
            print("Please do not break our game. Input only integers.")
        else:
            break
    print()
    print("Good luck, {}, the {}. And remember: your choices matter!".format(name, character))
    print()
    print()
    print()  
    return character

def intro_sequence(character):
    #define a function that prints the intro sequence depending on character choice
    print("2 weeks ago, a Holocron - a Jedi artifact containing immense knowledge - was stolen from the Jedi temple.")
    print("Word is that the Holocron is being stored on a junk planet called 9-NR3W.")
    print()
    print()
    if character == "Jedi":
        print("The Jedi council has tasked you to retrieve the artifact, since it contains valuable wisdom about the force.")
        print("Make sure that the artifact does not stay in the hands of crooks and bring it back to the Jedi council!")
    if character == "Bounty Hunter":
        print("You are a bounty hunter. The Huts, a powerful clan, have tasked you with retrieving a valuable artifact.")
        print("You don't know what a Holocron even is but you are in it for the money.")
        print("You are determined to get your reward, whatever it takes!")
    if character == "Smuggler":
        print("Your brother, the thief of the Holocron has tasked you with retrieving the artifact.")
        print("You don't know what to expect on the dangerous planet but you are determined to find the Holocron.")
        print("Due to its high value, you hope that your family may finally be free of their debt.")
    print()
    print()
    print("You are approaching 9-NR3W and decide to land your ship on a nearby mining village, located at the edge of a huge junk field.")
    print("There is garbage everywhere but it seems that the local people have managed to adapt to their environment.")
    print()
    print("A shady alien approaches you, asking for 5 credits due to you parking your ship in his backyard.")
    print()
    print()
    print("You argue with him but ultimately decide to pay. He's not worth the effort. You don't have many credits left. The journey was long.")


def main():
    karma = 0
    intro_sequence(choose_character())


main()