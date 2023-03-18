
    # every character has the following stats:
        # Karma
    #certain choices are only possible with certain characters

from time import sleep

sl = 5

def clean_input(prompt, length):
    # define recursive function to get clean player input
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("Please do not break our game. Input only integers.")
            return clean_input(prompt, length)
        if choice in range(1, length + 1):
            return choice
        else:
            print("Please input only integers between 1 and {}.".format(length))
            return clean_input(prompt, length)


def choose_character():
    #define a function which facilitates character choice
    print("Welcome to our text adventure!")
    print("The game is contained to your terminal. Enlarge it and enjoy!")
    print("The following story takes place in the STAR WARS universe.")
    print()
    sleep(sl)
    name = input("What is your name?: ")
    print()
    print("Hello, {}. Before your adventure starts, choose your character:".format(name))
    print()
    sleep(sl)
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
    prompt = "Please type 1, 2, or 3 to denote your choice: "
    length = 3
    choice = clean_input(prompt, length)
    if choice == 1:
        character = "Jedi"
    elif choice == 2:
        character = "Bounty Hunter"
    else:
        character = "Smuggler"
    print()
    print("Good luck, {} the {}. And remember: your choices matter!".format(name, character))
    print()
    return character

def intro_sequence(character):
    #define a function that prints the intro sequence depending on character choice
    sleep(sl)
    print("2 weeks ago, a Holocron - a Jedi artifact containing immense knowledge - was stolen from the Jedi temple.")
    print("Word is that the Holocron is being stored on a junk planet called 9-NR3W.")
    print()
    sleep(5)
    print()
    if character == "Jedi":
        print("The Jedi council has tasked you to retrieve the artifact, since it contains valuable wisdom about the force.")
        print("Make sure that the artifact does not stay in the hands of crooks and bring it back to the Jedi council!")
        sleep(5)
    if character == "Bounty Hunter":
        print("You are a bounty hunter. The Huts, a powerful clan, have tasked you with retrieving a valuable artifact.")
        print("You don't know what a Holocron even is but you are in it for the money.")
        print("You are determined to get your reward, whatever it takes!")
        sleep(5)
    if character == "Smuggler":
        print("Your brother, the thief of the Holocron has tasked you with retrieving the artifact.")
        print("You don't know what to expect on the dangerous planet but you are determined to find the Holocron.")
        print("Due to its high value, you hope that your family may finally be free of their debt.")
        sleep(5)
    print()
    print()
    print("You are approaching 9-NR3W and decide to land your ship on a nearby mining village, located at the edge of a huge junk field.")
    print("There is garbage everywhere but it seems that the local people have managed to adapt to their environment.")
    print()
    sleep(10)
    print("A shady alien approaches you, asking for 5 credits due to you parking your ship in his backyard.")
    print()
    sleep(sl)
    print("You argue with him but ultimately decide to pay. He's not worth the effort. You don't have many credits left. The journey was long.")
    print()

def bar(character, karma):
    # function that handles the bar scene
    print("You decide to head to the local bar as a starting point for your investigation.")
    sleep(5)
    print()
    print("The air is thick, it smells like alcohol. Where could you find information about the Holocron?")
    sleep(sl)
    print()
    print("You look around and spot the following opportunities:")
    print()
    print("Option 1:")
    print("Approach the Barkeeper and ask for information.")
    print()
    print("Option 2:")
    print("Try to intimidate the guests into telling you whether they saw something recently.")
    print()
    print("Option 3:")
    print("Ask a hostess whether she saw something.")
    print()
    print("Option 4: ")
    print("Approach a shady gambling table. Maybe you can gather the information by winning a game of cards?")
    print()
    prompt = "Please type 1, 2, 3, or 4 to make a choice: "
    length = 4
    while True:
        choice = clean_input(prompt, length)
        if choice == 1:
            sleep(sl)
            print("You approach the barkeeper and ask for information about any recent uncommon occurrances.")
            print()
            sleep(sl)
            print("The barkeeper grunts. No payment, no information he says.")
            print("Considering your bleak finances you decide to try talking to somebody else.")
            print()
        elif choice == 2:
            if character == "Bounty Hunter":
                print("Using your large stature and weapons you intimidate the guests.")
                print()
                sleep(sl)
                print("One patron in particular is so afraid of you, he wimpers something about a junk dealer named Arne who usually knows about valuable goods coming through.")
                print("Apparently this guy is located at the Black Market. If you take a speeder you can be there in 1h.")
                print()
                print("You decide to ask for further information.")
                sleep(sl)
                print("Another patron steps in. He throws a beverage at you and yells that you better leave now.")
                sleep(sl - 2)
                print("You duck at the last second.")
                sleep(sl - 2)
                print("The drink hits somebody else, your karma decreased.")
                print()
                sleep(sl)
                print("A full on brawl ensures. What will you do?")
                print()
                print("Option 1:")
                print("Fight your way out.")
                print()
                print("Option 2:")
                print("Try to use the turmoil to escape.")
                prompt = "Type 1 or 2 to make a choice: "
                length = 2
                choice2 = clean_input(prompt, length)
                if choice2 == 1:
                    sleep(sl)
                    print()
                    print("You partake in the brawl and sure enough you are able to overpower the attackers.")
                    print()
                    sleep(sl)
                    print("You decide to leave the bar but you are intercepted by the local police.")
                    sleep(sl)
                    print("They decide that you will spend some time in jail for violating the local order.")
                    value = prison_choice()
                    if value == 1:
                        break
                    else:
                        quit()
                elif choice2 == 2:
                    print("You weave between fighting drunks and manage to escape the bar.")
                    sleep(sl)
                    print("You decide to head for the Black Market. Time to see what this Arne guy knows.")
                    break
            else:
                print("The patrons don't seem intimidated by you. Maybe you should try something else.")
        elif choice == 3:
            print("You approach the hostess and ask her whether she has seen anything recently.")
            if character == "Jedi" or character == "Smuggler":
                sleep(sl)
                print("You decide to use your charme to persuade her to tell you about a local junk dealer.")
                sleep(sl - 2)
                print()
                print("There's a guy known for being involved in shady business and knowledgable about any valuable items passing through.")
                print()
                sleep(sl)
                print("The hostess tells you that his name is Arne. He frequents the Black Market, a cesspool for crooks.")
                sleep(sl)
                print()
                print("You leave the bar and head to the Black Market. With a speeder it will take 1h to arrive.")
                print()
                break
            else:
                print("You are not a very charming person, maybe if you were nicer she would be willing to help.")
        else:
            sleep(sl)
            print()
            print("The man at the gambling table does indeed know something - so he says at least.")
            print()
            sleep(sl)
            print("He is willing to give you the information if you win a game of galactic poker.")
            print("If you lose, he gets your ship.")
            print()
            sleep(sl)
            print("You see that he hides a blaster in his left hand. It seems you have no choice but to accept the wager.")
            print()
            sleep(sl - 2)
            print("Cards are being dealt and the game starts.")
            sleep(sl + 1)
            print("You are lucky! The gambler stands no chance against your hand.")
            print()
            print("He tells you that Arne, a local Black Market dealer may know something.")
            sleep(1)
            print("Apparently he is a shady guy involved with local smugglers.")
            print()
            sleep(0.5)
            print("If you take a speeder you can be there in 1h.")
            break
    return karma 

def prison_choice():
    sleep(10)
    print("After your clash with the law you find yourself in a jailcell, stripped of most of your equipment.")
    print()
    sleep(1)
    print("What will you do?")
    print()
    print("Option 1: Wait for your space attorney.")
    print()
    print("Option 2: Try to escape the cell.")
    print()
    prompt = "Please type 1 or 2 to a choice: "
    length = 2
    choice = clean_input(prompt, length)
    if choice == 1:
        print()
        print("You wait.")
        sleep(20)
        print()
        print("Hours pass.")
        sleep(20)
        print()        
        print("You slowly realize nobody will be coming.")
        sleep(10)
        print()
        print("Why did you even think that a bounty hunter like you could be saved by an attorney on some far away planet?")
        sleep(5)
        print()
        print()
        print("GAME OVER.")
        return 0
    else:
        print()
        print("You decide to scour the cell and the equipment you still have on you.")
        sleep(sl)
        print()
        print("You remember that you always carry a some explosives in your left shoe. A habit you could not shake since your childhood.")
        sleep(sl)
        print()
        print("You blow a hole in the wall. That was easy!")
        print()
        sleep(sl)
        print("You decide to head to the Black Market before the guards notice. They must be sleeping veeeeeeery tightly you think to yourself.")
        return 1

def main():
    karma = 0
    character = choose_character()
    intro_sequence(character)
    karma = bar(character, karma)


main()