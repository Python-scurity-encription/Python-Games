backpack = []
name=input('hello,Warrior, what\'s your name?')
input('Hello '+name+' Warrior, now your information will be displayed...Please wait...')
input('HP: 5, combat power: 10, hunger value: 0, normal attack distance: uncertain.')
blood=5
fight=10
hungry=0
input('Welcome to the new Chapter, Lost Temple!')
input('You found a temple in the jungle...')
input('You walked in and see some angry bees!')
input('System prompt: angry bees, HP: 2, speed: medium, attack power: 1, quantity: 20, distance 8 meters from you.')
input('System reward: smokescreen trick, attack power: 70, distance: 50 meters, use input c, blood volume: 50.')
box=input('DOD')
if box == 'c':
    input('Excellent!')   
    input('You destroyed them, and they are all die!')
else:
    input('You only killed one bee, and the others killed you!')
    quit()
input('You go on and on...')
input('You found a chest.')
box=input('Open the chest and press o, do not open and press other.')
if box == 'o':
    input('You opened the chest,')
    input('And you find an enchanted iron sword!')    
    input('System prompt: enchanted iron sword, the property is sharp II, increase attack damage 30, reduce attack power 10.')
    backpack.append("enchanted iron sword: sharp II")
else:
    input('You do not open the chest.')   
input('You see a skeleton behind you!')
input('System prompt: skeleton, HP: 50, speed: slow, attack power: 5, distance 5 meters from you.')
box=input('DOD')
if box == 'd':
    input('You attacked it, and it is die.')
else:
    input('You used a trick, it died and gave you an enchanted bow and an arrow.')
input('System prompt: enchanted bow, the property is infinite I, increase attack range 10.')
backpack.append("enchanted bow: infinite I")
