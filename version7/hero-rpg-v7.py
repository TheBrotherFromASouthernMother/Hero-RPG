#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#TODOS
              #CHARACTERS
#1. MAKE HERO DO DOUBLE DAMAGE WITH A PROBABLITY OF 20%
  #Using random module to generate percentage chance

#2. MAKE A NEW CHARACTER MEDIC WHO CAN RECUPERATE HEALTH AFTER BEING ATTACKED
#WITH A PROBABILITY OF 20%
   #use random.randint method to do this

#3 MAKE NEW CHARACTER SHADOW WHO HAS 1 HEALTH AND CAN ONLY TAKE DAMAGE
#  EVERY TENTH TIME
  #use counter variable to determine how many times shadow has been attacked,
  #if counter variable is equal ten he takes damage, counter variable is reset to 0 if
  #he survives the attack

#4 MAKE A ZOMBIE CHARACTER WHO CANNOT BE KILLED EVEN IF HIS HEALTH IS BELOW 0
  #ZOMBIE CHARACTER HEALTH RETURN TRUE EVEN IF HEALTH IS LESS THAN 0

#5 MAKE TWO UNIQUE CHARACTERS AND IMPLEMENT THEM
  #ANTI-HERO - ANDY'S idea
  #RANDOM GUARADIAN ANGEL - CHRISTIAN'S idea

#6 MAKE CHARACTES GOBLIN PRIZE WOULD BE EQUAL TO 5, WIZARD TO 6
  #INVENTORY ATTRITUBE WITH PROPERTIES INCLUDING PURSE ATTRIBUTE WHICH WOULD CONTAIN COINS
  #IF ALIVE METHOD RETURNS FALSE ENEMY GETS THE VALUE OF CHARACTER'S PURSE


              #ITEMS

  #MAKE USE ITEM FUNCTION
    #IF ITEM QUANITY IS GREATER THAN 0
      #USE ITEM FUNCTION TAKE EFFECT
      #BREAK
    #ELIF THEY GO BACK
      #IT TAKES THEM BACK OUT TO MAIN MENU
      #PRINT YOU WASTED YOUR TURN
    #ELSE
      #PRINT SORRY ALL OUT OF ITEM.NAME
      #RELIST THE INVENTORY PROBABLY USING A WHILE LOOP

#1. MAKE HEALING POTION, RESTORE 10 HP
  #




#SUB MENU ON MAIN MENU OPTION 4

    #IF CHARACTER SELECTS SUB MENU IT SHOWS THEM THEIR INVENTORY AND OPTIONS
      #

#class Merchandise
  #if not in battle
  #display options
    #do_shoppig
    #list_inventory
  #else:
  #list_inventory
   #use_items



 #class Inventory:
    #def __init__(self)
        #self.items = {
            #armor : 1
            #evade : 1
            #supertonic : 1
            #protein - increase health : 0
            #grenade - deals a certain amount of damage to all : 0
        #}
        #self.size = len(items)
        #def print_inventory(self):
            #print('You have {} in your inventory:\n\n {} \n\n'.format(self.size, str(self.items)))

        #def use_items(self, user, item, enemy=None):
            #if item == self.items.supertonic and item > 0:
                # if user.health + 10 > user.maxHealth:
                    #user.health = user.maxHealth
                #else:
                    #user.health += 10
                #item -= 1

            #elif item == self.items.grenade and item > 0 and enemy != None:
                #user.health -= 8
                #enemy.health -= 8
                #item -= 1
            #else:
                #print('Cannot find item')



import random

def main():
  class Character:
    def __init__(self, name, health, power, agility, charSkill=None):
      self.name = name
      self.health = health
      self.power = power
      self.agility = agility

      # charSkill
      # self.special = special

    def alive(self):
      return self.health > 0

    def print_status(self):
      print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):


      if enemy.evade():
        print('{}\'s attack has missed the {}'.format(self.name, enemy))
        return False

      # set the probability value
      if random.random < probability:
				charSkill()
			else:
        enemy.health -= self.power #-  enemy.armor
	      print("The {} does {} damage to the {}.".format(self.name, self.power, enemy))

      if enemy.name == 'medic'and random.randint(1, 100) < 20 and enemy.alive():
        	enemy.charSkill()

      if not enemy.alive():
        print("The {} is dead.".format(enemy))


    def evade():
      if random.radint(1, 100) < agility:
        return True
      else Return False

    def __str__(self):
      return self.name

  class Hero(Character):
    def __init__(self):
      self.name = 'hero'
      self.health = 10 # =
      #self.maxHealth = 10 + inventory.items.protein
      self.power = 5
      self.coins = 20 # default value from hero_rpg_part2.py
      self.armor = 0 # + inventory.items.armor
      self.agility = 50 #CHECK WITH AGILITY # + inventory.items.evade
      def charSkill(self, enemy):
      	enemy.health -= self.power
        print('The {} does {} extra damage to {}'.format(self.name, self.power, enemy))



	class Goblin(Character):
    def __init__(self):
      self.name = 'goblin'
      self.health = 6
      self.power = 2
      self.coins = 5
      self.agility = 1

	class Medic(Hero):
    def __init__(self):
    	self.name = "medic"
      self.health = 6
      self.power = 3
      self.coins = 5
      super().__init__()
    def charSkill(self):
      self.health += 2
      print('The {} has healed and regenerated 2 hp!'.format(self.name))

  class Shadow(Character):
    def __init__(self):
      self.name = 'shadow'
      self.health = 1
      self.power = 1
      self.coins = 5
      self.agility = 90

  class Zombie(Character):
    def __init__(self):
      self.name = 'zombie'
      self.health = 6
      self.power = 2
      self.coins = 99
      self.agility = 99
  	def alive(self):
      return True

  class Wizard(Character):
    def __init__(self):
      self.name = 'wizard'
      self.health = 8
      self.power = 2
      self.coins = random.randint(0, 40)
      self.agility = 60
    def charSkill(self, enemy):
      enemy.health -= 8
      print('The {} shoots a freaking lightning bolt at {}'.format(self.name, enemy.name))

	class antihero(Hero):
  	def __init__(self):
      self.name = 'antihero'
      self.health = 10
      self.power = -5
      self.agility = 50
			self.coins = -5
    def charSkill(self, enemy):
      self.health -= self.power
      print('The {} does {} extra damage to {}. An antihero is its own worst enemy!'.format(self.name, self.power, self.name))



  class GuardianAngel(Character):
    def __init__(self):
      self.name = 'guardian angel'
      self.power = 10

    def savesTheDay(self, charToSave, enemy):
      if charToSave.health > 2 and random.randint(1, 100) < 30 and charToSave.alive():
        print('A {} steps in and deals {} damage to the {} before mysteriously disappearing'.format(self.name, self.power, enemy))
        enemy.health -= self.power






#   hero = Hero()
#   goblin = Goblin()

  while enemy.alive() and hero.alive():
    #BATTFIELD MENU FUNCTION:
      hero.print_status()
      goblin.print_status() # CHANGE
      print()
      print("What do you want to do?")
      print("1. fight goblin")
      print("2. do nothing")
      print("3. flee")
      print("> ", end=' ')
      raw_input = input()
      if raw_input == "1":
        hero.attack(goblin)
        goblin.health += hero.power # CHANGE
      elif raw_input == "2":
        pass
      elif raw_input == "3":
        print("Goodbye.")
        break
      #ELIF OPTION 4:
        # GO TO INVENTORY SUB MENU
          #OPTIONS
            #SO ATTACK "3X ITEM" IMMEDIATELY CALLS HERO.ATTACK 3 TIMES"
            #HEALING POTION WOULD RESTORE HEALTH IF QUANITY IS GREATER THAN 0

      else:
        print("Invalid input {}".format(raw_input))

      if enemy.alive():
        # Goblin attacks hero
        enemy.attack(hero) # disable so that hero never dies
        guardianAngel.saveTheDay(hero, enemy)


main()


#if __name__ == "__main__":



  #enemies = ['goblin, wizard, assasin, theif, crab] <--- all enemies
  #defeatedEnemies = [goblin]

  #if len(deafetedEnemies) == len(enemies)
    #print YOU DID IT YOU WON
    #exit(0)

  #enemy = enemies[random.randint()]
  #if enemy is not in defeatedEnemies
    #pass
  #elif enemy in deafetedEnemies gonb
    #enemy = enemies[random.randint()]
