
# This code implements a text adventure set in the star wars universe. It consists mainly of print statements and if-clauses to check
# for player input. Additional functions entail functions to get clean player input and to implement quicktime events. 

from time import sleep
from threading import Timer
import time

#global variable to define speed of text appearance
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


# These are functions which create quick time events in the later game, they're based on a function found on stack overflow.
# Credit: Stackoverflow User: AKX & Anthony


def quick_time_fight_1(character, karma):
    # the function counts the time someone takes to give the input.
    # if the user needs longer than 3 seconds "You were hit is printed" and the losing function is called.
    #
    timeout = 3
    t = Timer(timeout, print, ["You were hit!"])
    t.start()
    start_time = time.time()
    prompt = f" Quickly, dodge the hit, press ENTER!\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
         return lost_quick_time(character, karma)
            
    else:
        print("You dodged the hit!")
        

def quick_time_fight_2(character, karma):
    # the function counts the time someone takes to give the input.
    # if the user needs longer than 3 seconds "You were hit is printed" and the lsoing function is called.
    timeout = 3
    t = Timer(timeout, print, ["You were hit!"])
    t.start()
    start_time = time.time()
    prompt = f"Time for payback! Press ENTER again!\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
         return lost_quick_time(character, karma)
    
    else:
        print("You punched his face!")
        


def quick_time_hacking_1(character, karma):
    # the function counts the time someone takes to give the input.
    # Different to the two functions before, a specific input is needed this time.
    # The function has three outcomes. If the player was too slow "The System detects you" will be printed and the according function will be called.
    # For the wrong input another function will be called, only the correct answer results in a continuation of the game.
        timeout = 4
        t = Timer(timeout, print, ["The System seems to detect you!"])
        t.start()
        start_time = time.time()
        prompt = f"3 + 5 equals?\n"
        answer = int(input(prompt))
        t.cancel()
        end_time = time.time()
        reaction_time = end_time - start_time
        if answer != 8:
            return hacking_wrong(character, karma)
            
        elif reaction_time < timeout and answer == 8:
            print("Yes! Now go on!")
        
        elif reaction_time > timeout:
            return hacking_too_long(character, karma)    

def quick_time_hacking_2(character, karma):
    # the function counts the time someone takes to give the input.
    # Different to the two functions before, a specific input is needed this time.
    # The function has three outcomes. If the player was too slow "The System detects you" will be printed and the according function will be called.
    # For the wrong input another function will be called, only the correct answer results in a continuation of the game.
        timeout = 6
        t = Timer(timeout, print, ["The System seems to detect you!"])
        t.start()
        start_time = time.time()
        prompt = f"9 * 8 equals?\n"
        answer = int(input(prompt))
        t.cancel()
        end_time = time.time()
        reaction_time = end_time - start_time
        if answer != 72:
            return hacking_wrong(character, karma)
            
        elif reaction_time < timeout and answer == 72:
            print("Yes! Now go on!")
        
        elif reaction_time > timeout:
            return hacking_too_long(character, karma)
            
def quick_time_hacking_3(character, karma):
    # the function counts the time someone takes to give the input.
    # Different to the two functions before, a specific input is needed this time.
    # The function has three outcomes. If the player was too slow "The System detects you" will be printed and the according function will be called.
    # For the wrong input another function will be called, only the correct answer results in a continuation of the game.
        timeout = 10
        t = Timer(timeout, print, ["The System seems to detect you!"])
        t.start()
        start_time = time.time()
        prompt = f" 2^4 equals?\n"
        answer = int(input(prompt))
        t.cancel()
        end_time = time.time()
        reaction_time = end_time - start_time
        if answer != 16:
            return hacking_wrong(character, karma)
            
        elif reaction_time < timeout and answer == 16:
            print("You're through!")
        
        elif reaction_time > timeout:
            return hacking_too_long(character, karma)
        
def passing_laser(character, karma):
    # the function counts the time someone takes to give the input.
    # Different to the two functions before, a specific input is needed this time.
    # The function has three outcomes. If the player was too slow "The System detects you" will be printed and the according function will be called.
    # For the wrong input another function will be called, only the correct answer results in a continuation of the game.
        timeout = 5
        t = Timer(timeout, print, ["You're through, now press ENTER to grab the Holocron!"])
        t.start()
        start_time = time.time()
        prompt = f"Don't move!"
        answer = input(prompt)
        t.cancel()
        end_time = time.time()
        reaction_time = end_time - start_time
        if reaction_time > timeout:
            print("You grabbed the Holocron!")
            
        else:
            return passing_laser_failed(character, karma)
        

def lost_quick_time(character, karma):
    # This function is called when the quick time fight is lost and ends the game
    print("You were not quick enough...")
    print()
    sleep(sl-2)
    print("You didn't manage to beat them.")
    print()
    sleep(sl-2)
    print("This shop will be your grave...")
    print()
    sleep(sl)
    print("GAME OVER")
    quit()

def hacking_wrong(character, karma):
    # This function is called when the quick time hacking input was wrong and ends the game
    print("Dammit, you got detected!")
    print()
    sleep(sl-3)
    print("The datapad shocks with electricity!")
    print()
    sleep(sl-2)
    print("It doesn't seem like you can continue your mission...")
    print()
    sleep(sl)
    print("GAME OVER")
    quit()
            
def hacking_too_long(character, karma):
    # This function is called when the quick time hacking wasn't solved in the right amount of time and ends the game
    print("Dammit, you got detected!")
    print()
    sleep(sl-3)
    print("You get shocked by the datapad immediatley!")
    print()
    sleep(sl-2)
    print("It doesn't seem like you will continue your mission...")
    print()
    sleep(sl)
    print("GAME OVER")
    quit()

def passing_laser_failed(character, karma):
# This function is called when the quick time hacking wasn't solved in the right amount of time and ends the game
    print("An alarm starts ringing.")
    print()
    sleep(sl-3)
    print("Smoke starts entering the room, it smells weirdly.")
    print()
    sleep(sl-2)
    print("Your eyes become heavier and heavier...")
    print()
    sleep(sl)
    print("GAME OVER")
    quit()

                  

def choose_character():
    # This is the first sequence of the actual game in this sequence one can choose the character.
    # You will see the print and sleep pattern very much throughout this code. Through the print statement the story is transmitted and the sleep statements keep the programm
    # from printing everything at once.
    print("Welcome to our text adventure!")
    print("The game is contained to your terminal. Enlarge it and enjoy!")
    print("The following story takes place in the STAR WARS universe.")
    print()
    sleep(sl)
    
    # Giving the name of the player
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
    
    #This functions sets the attribute character 
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
    print("Be on the lookout for quicktime events. Should you be prompted, enter your answer and press ENTER.")
    print()
    return character

def intro_sequence(character):
    # After setting the character the intro sequence starts.
     
    sleep(sl)
    print("2 weeks ago, a Holocron - a Jedi artifact containing immense knowledge - was stolen from the Jedi temple.")
    print("Word is that the Holocron is being stored on a junk planet called 9-NR3W.")
    print()
    sleep(sl)
    print()
     
        
    #  Depending on the character a different intro will be executed   
    if character == "Jedi":
        print("The Jedi council has tasked you to retrieve the artifact, since it contains valuable wisdom about the force.")
        print("Make sure that the artifact does not stay in the hands of crooks and bring it back to the Jedi council!")
        sleep(sl)
    if character == "Bounty Hunter":
        print("You are a bounty hunter. The Huts, a powerful clan, have tasked you with retrieving a valuable artifact.")
        print("You don't know what a Holocron even is but you are in it for the money.")
        print("You are determined to get your reward, whatever it takes!")
        sleep(sl)
    if character == "Smuggler":
        print("Your brother, the thief of the Holocron has tasked you with retrieving the artifact.")
        print("You don't know what to expect on the dangerous planet but you are determined to find the Holocron.")
        print("Due to its high value, you hope that your family may finally be free of their debt.")
        sleep(sl)
        
        
    print()
    print()
    print("You are approaching 9-NR3W and decide to land your ship on a nearby mining village, located at the edge of a huge junk field.")
    print("There is garbage everywhere but it seems that the local people have managed to adapt to their environment.")
    print()
    sleep(2*sl)
    print("A shady alien approaches you, he is asking for 5 credits due to you parking your ship in his backyard.")
    print()
    sleep(sl)
    print("You argue with him but ultimately decide to pay. He's not worth the effort. You don't have many credits left. The journey was long.")
    print()
    

def bar(character, karma):
    # This sequence is played after the intro and the first where the player is able to make a choice, which has an impact on the storyline.
    
    
    print("You decide to head to the local bar as a starting point for your investigation.")
    sleep(sl)
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
    
    
    # Here the Player can chose one of the four options
    prompt = "Please type 1, 2, 3, or 4 to make a choice: "
    length = 4
    while True:
        # The choice is checked 
        choice = clean_input(prompt, length)
        
        # Choice one leads for every player to nothing.
        if choice == 1:
            sleep(sl)
            print("You approach the barkeeper and ask for information about any recent uncommon occurrances.")
            print()
            sleep(sl)
            print("The barkeeper grunts. No payment, no information he says.")
            print("Considering your bleak finances, you decide to try talking to somebody else.")
            print()
            
            
        # Choice two checks which value character has. Only the Bounty hanter can go this path.    
        elif choice == 2:
            karma = karma - 1
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
                
                # Here players with the character Bounty hunter can make a choice. Depending on that a different function is called. These are defined further below.
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

                    value = prison_choice(character, karma)
                    if value == 1:
                        break
                    else:
                        quit()
                elif choice2 == 2:
                    print("You weave between fighting drunks and manage to escape the bar.")
                    sleep(sl)
                    print("You decide to head for the Black Market. Time to see what this Arne guy knows.")
                    return black_market(character, karma)
            else:
                print("Your karma decreased but the patrons don't seem intimidated by you. Maybe you should try something else.")
                
        # Choice three works if the value of character is either Jedi or Smuggler, the bounty hunter will be send back to options        
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
                
                return black_market(character, karma)
            else:
                print("You are not a very charming person, maybe if you were nicer she would be willing to help.")

                
        # The last choice works for everybody        
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
            sleep(sl)
            print("Apparently he is a shady guy involved with local smugglers.")
            print()
            sleep(sl-2)
            print("If you take a speeder you can be there in 1h.")
            return black_market(character, karma)
        
def prison_choice(character, karma):
    # This function is called if the bounty hunter decided to fight. 
    
    sleep(2*sl)
    print("After your clash with the law you find yourself in a jailcell, stripped of most of your equipment.")
    print()
    sleep(sl-3)
    print("What will you do?")
    print()
    print("Option 1: Wait for your space attorney.")
    print()
    print("Option 2: Try to escape the cell.")
    print()
    
    
    # Again one can choose one of two options.
    prompt = "Please type 1 or 2 to make a choice: "
    length = 2
    choice = clean_input(prompt, length)
    
    # Choice one ends the Game
    if choice == 1:
        
        
        print()
        print("You wait.")
        sleep(4*sl)
        print()
        print("Hours pass.")
        sleep(4*sl)
        print()        
        print("You slowly realize nobody will be coming.")
        sleep(2*sl)
        print()
        print("Why did you even think that a bounty hunter like you could be saved by an attorney on some far away planet?")
        sleep(sl)
        print()
        print()
        print("GAME OVER.")
        

        return 0
    
    # And choice 2 brings the player to the black market.
    else:
        
        
        print()
        print("You decide to scour the cell and the equipment you still have on you.")
        sleep(sl)
        print()
        print("You remember that you always carry some explosives in your left shoe. A habit you could not shake since your childhood.")
        sleep(sl)
        print()
        print("You blow a hole in the wall. That was easy!")
        print()
        sleep(sl)
        print("You decide to head to the Black Market before the guards notice. They must be sleeping veeeeeeery tightly you think to yourself.")
        
        
        return black_market(character, karma)

# def black market function
def black_market(character, karma):
    # This is the black market function. Again two choices are possible.
    
    sleep(sl)
    print()
    print()
    print("The jam-packed streets and booths remember you of Mos-Eisley.")
    sleep(sl-2)
    print("You start the search for Arne.")
    sleep(sl-2)
    print("It doesn't take long as he seems to be very known around the place.")
    sleep(sl)
    print()
    print("Definitely, he's one of the more wealthy shop owners in the market.")
    sleep(sl-1)
    print("He not just has a booth but an entire store filled with Bounty Hunter droids, genosian technic, and basically everything else that's forbidden in the Republic.")
    sleep(sl)
    print()
    print("\x1B[3m" + "Ahhh what are you lookin for? I can get you everything from here 'til Nal'utta." + "\x1B[0m" + " He says with a wide grin.")
    sleep(sl)
    print()
    print("As you explain what you're looking for, his grin starts to vanish...")
    sleep(sl-2)
    print()
    print("\x1B[3m" + "Look, my man, I'm not lookin for trouble 'ere, lemme say I could know something, but you look like someone who can solve problems…" + "\x1B[0m")
    sleep(2*sl)
    print("\x1B[3m" + "And as it just so 'appens, I 'ave a problem that needs to be solved." + "\x1B[0m")
    sleep(sl)
    print("What will you do?")
    print()
    print("Option 1: Help Arne")
    print()
    print("Option 2: Threaten him")
    print()
    
    
    # Depending on the choice made, the according function is called.
    prompt = "Please type 1 or 2 to make a choice: "
    length = 2
    choice = clean_input(prompt, length)
    if choice == 1:
        karma = karma + 2
        return side_quest(character, karma)
    else:
        karma = karma - 1
        return market_fight_scene(character, karma)
    

def market_fight_scene(character, karma):
    # This function checks which value character has.
    
    print("You decide it's not worth your time to bother yourself with his problems.")
    print()
    sleep(sl)
    print("You threaten Arne to tell you where the Holocron is. Your karma decreases.")
    print()
    sleep(sl-2)
    print("As you yell at him, more and more shady people start entering his shop.")
    print()
    print("Noticing this, your voice is getting quieter and quieter.")
    print()
    sleep(sl)
    print("\x1B[3m" + "How the tables turn" + "\x1B[0m" + " says Arne with an ominous grin.")
    sleep(sl)
    print("The people start closing in on you.")
    
    
    # For the smuggler the game ends here.
    if character == "Smuggler":
        
        sleep(sl-2)
        print("You try to reach for your Blaster.")
        print()
        sleep(sl-3)
        print("Oh no! It gets punched out of your hand immediately!")
        print()
        sleep(sl-2)
        print("You're not used to fighting with your bare hands.")
        print("The people start hitting you with bats and vibro-axes.")
        sleep(sl)
        print("This market will be your grave.")
        print()
        print()
        sleep(sl)
        print("GAME OVER")
        
        quit()
    
    # A new function is called.
    elif character == "Jedi":
        
        sleep(sl-2)
        print()
        print("It is enough to pull your lightsaber to scare off the rabble.")
        sleep(sl)
        print()
        print("As you turn to Arne again, he's shaking out of fear.")
        sleep(sl)
        print("\x1B[3m"+ "I 'ad no idea you're a Jedi " + "\x1B[0m" + "he whispers silently.")
        sleep(sl)
        print()
        print("\x1B[3m" + "Liiisten....." + "\x1B[0m")
        sleep(sl)
        print()
        print("\x1B[3m" + "I 'ad nothing to do with the theft of the Holocron..." + "\x1B[0m")
        sleep(sl)
        print("\x1B[3m" + "Look buddy, there's a secret base in the SACH53N sector....." + "\x1B[0m")
        sleep(sl)
        print("\x1B[3m" + "I heard some rumors about some valuable artifact they got, but I swear that's everything I know..." + "\x1B[0m")
        sleep(sl-2)
        print("\x1B[3m" + "But I have nothing to do with them, so I can't guarantee nothing, but I would look there." + "\x1B[0m")
        print()
        sleep(sl)
        print("You decide to trust him.")
        sleep(sl)
        print("You put your lightsaber away.")
        sleep(sl)
        print("The SACH53N sector is far out you will need some time to reach it.")
        
        return SACH3N_sector(character, karma)
      
    # The quick time functions defined at the start of the code are called. Only when they are completed succesfully the fuction goes on and calls the continuing function.    
    else:
        
        sleep(sl-2)
        print()
        print("Although you are outnumbered, these townsfolks are no match for you.")
        sleep(sl)
        quick_time_fight_1(character, karma)
        print()
        sleep(sl-2)
        quick_time_fight_2(character, karma)
        sleep(sl-2)
        print()
        print("After fighting them, you turn towards Arne.")
        sleep(sl)
        print()
        print("As he retreats, he starts talking hastily:")
        print()
        sleep(sl-2)
        print("\x1B[3m" + "Look buddy, the Holocron ....." + "\x1B[0m")
        sleep(sl-2)
        print("\x1B[3m" + "I was only the middleman, it's no longer 'ere." + "\x1B[0m")
        sleep(sl-2)
        print("\x1B[3m" + "I sold it to some shady guys, weird people who got their base in the SACH53N sector!" + "\x1B[0m")
        sleep(sl-2)
        print("\x1B[3m" + "That's all I know I swear." + "\x1B[0m")
        print()
        sleep(sl)
        print("The SACH53N sector you think...")
        print()
        sleep(sl-2)
        print("That's quite far out. You decide to leave immediately for it.")
        print()
        sleep(sl)
        print("You leave Arne whimpering in a destroyed booth.")
        
        return SACH3N_sector(character, karma)
    
# def side quest function
def side_quest(character, karma):
    # If the player decides to go with helping Arne this function is called.
    # It's some text and afterward the hacking functions defined on the start of the code will get called..
    
    
    print("This seems like a reasonable deal for you.")
    print()
    sleep(sl-2)
    print("You nod.")
    print()
    sleep(sl-2)
    print("\x1B[3m" + "Okay, a couple of days ago some guys took a little something from my shop." + "\x1B[0m")
    print()
    sleep(sl)
    print("\x1B[3m" + "Shady guys..." + "\x1B[0m")
    print()
    sleep(sl-2)
    print("I want it back.")
    print()
    sleep(sl-1)
    print("He gives you the adress of a nearby warehouse.")
    print()
    sleep(sl)
    print("It's by the edge of the Black Market.")
    print()
    sleep(sl-2)
    print("You depart, you better want to do this quickly...")
    print()
    sleep(sl+1)
    print("After staking out the warehouse, you conclude that the best way to do this is quietly.")
    print()
    sleep(sl)
    print("The front is heavily protected by many guards. However there seems to be an unprotecteded side-door .")
    sleep(sl-2)
    print()
    print("There's a security console next to the door.")
    sleep(sl-2)
    print("Hopefully your skills are good enough to crack the code.")
    print()
    sleep(sl)
    
    
    # Here the hacking functions which are defined at the beginning of the file are called.
    quick_time_hacking_1(character, karma)
    print()
    sleep(sl)
    quick_time_hacking_2(character, karma)
    print()
    sleep(sl)
    quick_time_hacking_3(character, karma)
    
    
    print()
    sleep(sl)
    print("It worked!")
    print()
    sleep(sl-2)
    print("You're able to enter the warehouse unnoticed.")
    sleep(sl)
    print("In contradiction to the outside, there are no guards inside.")
    print()
    sleep(sl-2)
    print("It's easy to find Arne's stuff.")
    print()
    print("What even is that? Did Arne just make you retrieve some sort of weapon?")
    sleep(sl)
    print("As quietly as you enter the warehouse you leave again.")
    print()
    print("You head back to the Black Market, better not tamper too much with the thing you just retrieved.")
    sleep(sl)
    print("Arne is happy that you managed to get it back.")
    print()
    sleep(sl)
    print()
    print("For a second you doubt whether the item was his in the first place....")
    sleep(sl-2)
    print("He tells you:")
    print()
    sleep(sl-2)
    print("This Holocron you're looking for, it's in a secret base in the SACH53N sector. However, I don't know where exactly.")
    print()
    sleep(sl-2)
    sleep(sl)
    print("The SACH53N sector you think...")
    print()
    sleep(sl-2)
    print("That's quite far out. You decide to head out immediately.")
    print() 
    
    return SACH3N_sector(character, karma)
              

def SACH3N_sector(character, karma):
    sleep(sl)
    print()
    print("After strolling for hours through the sector you still didn't find anything…")
    sleep(sl-2)
    print()
    print("As you approach a big canyon, you feel no longer unobserved…")
    sleep(sl-2)
    print()
    print("You hear grunting...")
    sleep(sl-3)
    print()
    print("Something is moving under the sand across the abyss....")
    sleep(sl-3)
    print()
    print("\x1B[3m" + "Trrööööllllllaaaaaaaa" + "\x1B[0m")
    sleep(sl-1)
    print()
    print("A particularly ugly rancor emerges, it seems as if he smelled you…")
    sleep(sl)
    print("However, you stay calm.")
    sleep(sl-2)
    print("There is a nearly 10-meter ravine between you and the Rancor.")
    sleep(sl)
    print()
    print("And every child knows that Rancors aren't the smartest....")
    sleep(sl)
    print()
    print("As if he would like to prove it, the ugly Rancor suddenly starts sprinting toward you…")
    sleep(sl-2)
    print("It seems as if he wouldn't mind the gap.")
    sleep(sl)
    print()
    print("While falling into the depths he screams one last time…")
    sleep(sl+2)
    print()
    print("At this moment, you want to turn your view away from him, but then you see something…")
    sleep(sl-2)
    print("It seems as if something is approaching the wrecked Rancor.")
    sleep(sl)
    print()
    print("As you look closer, it seems some heavily armed mercenaries inspect the Rancor at the bottom of the canyon.")
    sleep(sl)
    print()
    print("Seems like you finally found the base!")
    print()
    print()
    return inside_base(character, karma)


def inside_base(character, karma):
    print("It seems as if the base is protected awfully, maybe they expected no one to find them here...")
    print()
    sleep(sl)
    print("Through a ventilation shaft, you manage to get inside the facility.")
    print()
    sleep(sl)
    print("After sneaking through the base for a while it seems as if you have found the room where the Holocron is hidden.")
    print()
    sleep(sl-2)
    print("However it is protected by lasers, you have to be very careful to pass through them. Don't activate the alarm!")
    print()
    sleep(sl-2)
    passing_laser(character, karma)
    print()
    sleep(sl-2)
    print("You made it!")
    print("Now get out of there!")
    print()
    sleep(sl)
    print("As fast as you came you leave this base again.")
    print()
    sleep(sl)
    return end_sequence(character, karma)

def end_sequence(character, karma):
    # this function defines the end sequence. Depending on the player's accumulated karma score, the ending differs.
    print("Having retrieved the Holocron, you depart the junk planet with your ship.")
    sleep(sl-2)
    if character == "Jedi":
        print("You head to the Jedi Temple on Corouscant. You cannot wait to give the Jedi Council the Holocron.")
        sleep(2*sl)
        print("As you stand before them and present them with the artefact, they look overjoyed. Suddenly, they start whispering among themselves.")
        sleep(sl)
        if karma < 1:
            print("The Council is enraged. They have heard about your evil deeds during your mission and decide that")
            sleep(sl-2)
            print(" you are hereby expelled from the Jedi Order!")
            sleep(sl)
            print("Being stripped of your whole identity, you opt for a life as a simple farmer on some faraway planet.")
            sleep(2*sl)
            print("Maybe your deeds were truly not worthy of a Jedi.")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()
        else:
            print("A member of the Council approaches you and looks you in the eye.")
            sleep(sl-2)
            print("They hereby grant you the ranks of Master and Council Member due to your heroic deeds during your last mission.")
            sleep(sl)
            print("Congratulations!")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()
    elif character == "Smuggler":
        print("Finally! You retrieved the Holocron! You cannot wait to give it to your Brother.")
        sleep(sl-2)
        print("Your family will be free of debt you think to yourself.")
        sleep(sl)
        if karma < 1:
            print("What is that? You spot a ship in the distance!")
            sleep(sl-3)
            print("They have detached some torpedos!")
            sleep(sl)
            print("As you look death in the eye, you think to yourself whether this is the result of past actions....")
            sleep(2*sl)
            print("Now your family will forever be indebted. You die in space, nobody is here for you.")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()
        else:
            print("Congratulations!")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()
    else:
        print("It is payday! The Huts have decided to reward you generously for your services!")
        if karma < 1:
            sleep(sl)
            print("As you leave the Hut palace, someone holds a blaster to your head.")
            sleep(sl)
            print("They say that you were too messy during your last mission.")
            sleep(sl)
            print("The Huts do not want to associate with you any longer.")
            sleep(sl)
            print("This is where your story ends.")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()
        else:
            sleep(sl)
            print("The Huts are very content with how you handled things.")
            sleep(sl)
            print("Maybe more lucrative business opportunities will present themselves if you keep working for the Huts.")
            sleep(sl)
            print("For the time being, you decide to enjoy your life with the money you earned.")
            sleep(sl)
            print("Congratulations!")
            sleep(2*sl)
            print("\x1B[3m" + "The END" + "\x1B[0m")
            sleep(2*sl)
            quit()

# this main function calls the first functions and initiliases the players karma score.
def main():
    karma = 0
    character = choose_character()
    intro_sequence(character)
    karma = bar(character, karma)
main()