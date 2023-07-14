from ninja import Ninja
from pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")




for i in range(0,20,1):
    if(jack_sparrow.health > michelangelo.health):

            michelangelo.attack(jack_sparrow)
            jack_sparrow.show_stats()
            print("Nice Pirate Attack")
    else :
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()
        print("Nice Ninja Attack")

    if (jack_sparrow.health < 0 or michelangelo.health < 0):
        print("The fight is over") 
        break

# michelangelo.show_stats()
# jack_sparrow.show_stats()


