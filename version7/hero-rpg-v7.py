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
  #ANTI-HERO - ANDY'S IDEA
  #RANDOM GUARADIAN ANGEL - CHRISTIAN'S IDEA

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



def main():
  class Character:
    def __init__(self, name, health, power, CharSkill=None):
      self.name = name
      self.health = health
      self.power = power
      #self.armour = armour
      #self.evade = chance to evade
      #self.CharSkill = CharSkill

    def alive(self):
      return self.health > 0
    
    def print_status(self):
      print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):
    
      #if enemy.evade():
        #print {self.name}'s attack has missed the {enemy}
        #return False
      enemy.health -= self.power #-  enemy.armour attribute
      print("The {} does {} damage to the {}.".format(self.name, self.power, enemy))
      if enemy.alive():
          print("The {} is dead.".format(enemy))   
    
    #def evade():
      #random.radint() > self.evade percentage, return True else Return False

    #def special(self.name, self.CharSkill, probability):
        #if random.randint() < probability:
          #self.CharSkill  

    def __str__(self):
      return self.name
    
  # class Hero:
    

  # class Goblin:

  class Medic(Character):
    def heal(self, target):
        target.health += 2
        print("The {} has cast heal restoring 2 health points to {}".format(self.name, target.name))
      else:
        print("The {} tried to cast heal but has failed!".format(self.name))

  
  hero = Character('hero', 10, 5)
  goblin = Character('goblin', 6, 2)

  while goblin.alive() and hero.alive():
    #BATTFIELD MENU FUNCTION:
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
        goblin.health += hero.power # to make goblin a zombie that heals by amount hero attacks
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

      if goblin.alive():
        # Goblin attacks hero
        goblin.attack(hero) # disable so that hero never dies


main()


#if __name__ == "__main__":

  #allies = []

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

  
  
    