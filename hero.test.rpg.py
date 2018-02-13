#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
  	class Hero: 
          def __init__(self, health, power):
            self.health = health
            self.power = power
                
          def attack(self, enemy):
            self.enemy = enemy
            # Hero attacks goblin
            self.enemy.health -= self.power
            print("You do {} damage to the {}.".format(self.power, self.enemy))
            if self.enemy.health <= 0:
                print("The {} is dead.".format(self.enemy))

          def alive(self):
            return self.health > 0
        
          def print_status(self):
            print("You have {} health and {} power.".format(self.health, self.power))
        	
        
    class Goblin:
      def __init__(self, health, power):
        self.health = health
        self.power = power
        
   		def attack(self, enemy):
        self.enemy = enemy

        self.enemy -= self.power
        print("The {} does {} damage to you".format(self, self.power))
        if self.enemy.health <= 0:
          print("you are dead.")
      
      def alive(self):
        return self.health > 0
      
      def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))
      
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)