import time
print('\nHello, welcome to the battle of Skyrim, this was originally a collective training ground for warriors, because a monster race built a camp here and save our imprisoned warriors in prisons all over the place, we need you to help us, Please enter your nickname now:')
name=input()
print('Hello '+name+' Warrior, now your information will be displayed...Please wait...')
time.sleep(3)
print('HP: 5, combat power: 10, hunger value: 0, normal attack distance: uncertain.')
blood=5
fight=10
hungry=0
time.sleep(5)
print('When you see the word DOD, please enter the trick you want to use, press d to attack, a to use the first move.')
time.sleep(7)
print('First level, jungle adventure!')
time.sleep(3)
print('You slowly walked into the jungle...')
time.sleep(3)
print('You found a tiger within 30 meters!')
time.sleep(3)
print('DOD')
input()
print('You attacked it,')
time.sleep(2)
print('But your attack power is too low, you failed to kill him...')
time.sleep(2)
print('It comes at you!! DOD')
box=input()
print('You did it! You killed the tiger!')
time.sleep(2)
print('You have now unlocked the first move, attack power: 30, distance 100 meters!')
time.sleep(2)
print('The system rewards you: food, 3 pieces of tiger meat, the food will provide you with options when you are hungry, you can choose not to eat.')
time.sleep(7)
print("It's noon, press a to eat meat X1, hunger value: 1, don't eat press anything else.")
eat=input()
if eat=='a':
    print('Remaining meat x2, hunger value: 0.')
    hungry=0
else:
    print('Remaining meat x3, hunger value: 1.')
    hungry=1
time.sleep(5)
print('You walked forward for a while,')
time.sleep(3)
print('You saw a forest, you walked in...')
time.sleep(5)
print('You saw many small fruits on a few small trees.')
time.sleep(3)
print("Pick the fruit and press q, don't pick and press other.")
box=input()
if box=='q':
    print('You collected many fruits,')
    time.sleep(3)
    print('You eat half of it, save the remaining half.')
    fight=30
    blood=15
    time.sleep(2)
    print('Your attack power has increased to 15 (only used for basic attacks),')
    time.sleep(3)
    print('Your HP has increased to 15.')
else:
    print('You did not collect those fruits,')
    time.sleep(3)
    print('Your hunger level has increased to 5.')
    hungry=5
time.sleep(3)
print('You keep going forward,')
time.sleep(3)
print('You saw a group of wolf soldiers in front!')
time.sleep(3)
print('System prompt: wolf soldier, HP: 10, speed: slow, attack power: 5, quantity 3, distance 5 meters from you.')
time.sleep(5)
print('Do not press "d" for this war!')
time.sleep(1)
print('Use another way!')
time.sleep(1)
print('DOD')
box=input()
if box=='d':
    print('You did not attack them, the three of them killed you!')
    quit()
elif box=='a':
    if fight>=30:
        print('Awesome!')
        time.sleep(2)
        print('You unlocked the second move, attack power: 50, distance 50 meters, use "s"')
    else:
        print('You killed a wolf, and the remaining two pounce at you, 2 meters away from you.')
        time.sleep(4)
        print('DOD')
        box=input()
        if box=='a':
            print('You used a trick,')
        elif box=='d':
            print('You used a general attack,')
        elif box=='s':
            print('You used the second trick,')
else:
    print('Your input does not conform to the built-in operation of the system, please restart the game.')
    quit()
time.sleep(2)
print('You killed them all,')
time.sleep(1)
print('System reward: one-time big move, attack power: 100, distance: 400 meters, use input xyz, blood volume increased to: 100.')
one=0
time.sleep(5)
print('You found a river in front of you...')
time.sleep(2)
print('You came to the river.')
time.sleep(1)
print('You saw some fish in the river.')
time.sleep(2)
print('You caught them, and the system rewards you: food, 5 fish.')
time.sleep(2)
print('It is evening now, and you can eat something.')
time.sleep(3)
box=input("It's noon, press a to eat fish X1, hunger value: 1, don't eat press anything else.")
if box=='a':
    print('Remaining fish x4, hunger value: ?.')
    #hungry=?
else:
    print('Remaining fish x5, hunger value: ?.')
    #hungry=?
print('It is night now, so the system gave you a bed.')
time.sleep(3)
box = input('press b to sleep, don\'t sleep press anything else.')
if box == 'b':
      print('You are sleeping now... please wait 15 second.')
      time.sleep(15)
else:
      print('You did not sleep, so the zombies killed you!')
      quit()
print('You waked, and found a chest behind you.')
time.sleep(2)
box=input('Open the chest press o, don\'t open press anything else.')
if box=='o':
      print('You found a leather chest armor.')
      time.sleep(3)
      print('Leather chest armor: increase protection value：2')
      protection = 2
else:
      print('You do not open the chest.')
      protection = 0
print('You walked by the river slowly...')
time.sleep(2)
print('You found a little house beside the river.')
time.sleep(2)
box=input('Walked in and press w, do not walk in press anything else.')
if box == 'w':
      print('You walked in and saw a ...')
      time.sleep(1)
      print('Zombie!')
      time.sleep(1)
      print('System prompt: zombie, HP: 20, speed: middle, attack power: 5, protection: 2, distance 5 meters from you.')
else:
      print("You did not walked in ti the house.")
print('System warning: the first level of the boss is coming!')
time.sleep(2)
print('A "mountain" appeared in front of you...')
time.sleep(2)
print('System reminder: Get the Beast Meng, also known as the BOSS of the first level, HP: 200, attack power: 5, speed: huge slow, number: 1, distance: 20 meters.')
boss=200
time.sleep(3)
print('Getting the beast Meng attacked you,')
blood-=1
time.sleep(2)
print('Remaining HP:'+str(blood)+' ,Boss HP:'+str(boss)+'.')
time.sleep(2)
print('DOD')
box=input()
if box=='d':
    print('You attacked him,')
    boss-=15
elif box=='a':
    print('You used a trick,')
    boss-=30
elif box=='s':
    print('You used two tricks,')
    boss-=50
elif box=='xyz':
    print('You used a one-time big move!')
    one='1'
    boss-=100
if blood>0:
    while boss>=0:
        time.sleep(1)
        print('Wu Ye Beast Meng attacked you again,')
        blood-=1
        time.sleep(2)
        print('Remaining HP:'+str(blood)+' ,Boss HP:'+str(boss)+'.')
        time.sleep(2)
        print('DOD')
        box=input()
        if box=='d':
            print('You attacked him,')
            boss-=15
        elif box=='a':
            print('You used a trick,')
            boss-=30
        elif box=='s':
            print('You used two tricks,')
            boss-=50
        elif box=='xyz':
            if one==0:
                print('You used a one-time big move!')
                one==1
                boss-=100
print('You killed him, you won!!!!')
time.sleep(1)
print('System prompt: You have passed the first level!!!')
input('Hit [ENTER] to continue this game.')
input('good job! unfortunaly the second level isn\'t ready, so don\'t forget to subscribe to our channel and always check you E-mail, Bye!')
#the '#' is for Peter to changed.
#this part of game haven't ready, so don't play it.
