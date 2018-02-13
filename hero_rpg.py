#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def alive(self):
      return self.health > 0
    
    def print_status(self):
      print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):
      enemy.health -= self.power
      print("The {} does {} damage to the {}.".format(self.name, self.power, enemy))
      if enemy.alive():
          print("The {} is dead.".format(enemy))    
    def __str__(self):
      return self.name
  # class Hero:

  # class Goblin:



  hero = Character('hero', 10, 5)
  goblin = Character('goblin', 6, 2)

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

      if goblin.alive():
        # Goblin attacks hero
        goblin.attack(hero)
      
      goblin.health += hero.power

main()
