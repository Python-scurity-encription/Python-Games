import time
print('\n你好，欢迎来到决战天际，这里原来是勇士的集体训练场，因为一个怪物种族在这里修建了营地，把我们的勇士都囚禁在各地监狱,我们需要你来帮助我们，现在请输入你的昵称')
name=input()
print('你好'+name+'勇士，现在将显示你的信息...请等待')
time.sleep(3)
print('血量：5，战斗力：10，饥饿值:0,普通攻击距离:不定')
blood=5
fight=10
hungry=0
time.sleep(5)
print('当看见DOD的字样时请输入您想要用的招术，"d"攻击')
time.sleep(7)
print('第一关,丛林冒险!')
time.sleep(3)
print('你慢慢走进了丛林')
time.sleep(3)
print('你发现了30米的距离内,有一只老虎...') 
time.sleep(3)
print('DOD')
input()
print('你攻击了它')
time.sleep(2)
print('由于你的攻击力太低,你没能杀死他')
time.sleep(2)
print('它向你扑来!!DOD')
box=input()
print('你做到了!你杀死了老虎!')
time.sleep(2)
print('你现在解锁了第一招,攻击力:30,距离100米!使用按a')
time.sleep(2)
print('系统奖励你:食物,3块老虎肉,食物将在你饿的时候提供你吃的选项你可以选择不吃')
time.sleep(7)
print('已经到了中午,按下a吃肉X1,,饥饿值:1,不吃按别的')
eat=input()
if eat=='a':
    print('剩余肉x2,饥饿值:0')
    hungry=0
else:
    print('剩余肉x3,饥饿值:1')
    hungry=1
time.sleep(5)
print('你往前走了一会儿')
time.sleep(3)
print('你看到了一片树林,你走了进去...')
time.sleep(5)
print('你在几棵小树上看见了许多小果子')
time.sleep(3)
print('采果子按q,不采按别的')
box=input()
if box=='q':
    print('你采集了许多果子')
    time.sleep(3)
    print('你吃了一半,把剩下的一半存了起来')
    fight=30
    blood=15
    time.sleep(2)
    print('你的攻击力提升到了15(只用于普攻)')
    time.sleep(3)
    print('你的血量提升到了15')
else:
    print('你没有采集那些果子')
    time.sleep(3)
    print('你的饥饿度提升到了5')
    hungry=5
time.sleep(3)
print('你继续往前走')
time.sleep(3)
print('你在前面看到了一群狼兵')
time.sleep(3)
print('系统提示:狼兵,血量:10,速度:慢,攻击力:5,数量3,离你的距离5米')
time.sleep(3)
print('DOD')
box=input()
if box=='d':
    print('你没有攻击到他们，他们三只把你杀死了')
    quit()
elif box=='a':
    if fight>=30:
        print('太棒了!')
        time.sleep(2)
        print('你解锁了第二招,攻击力:50,距离50米,使用按s')
    else:
        print('你杀死了一只狼,剩下两只向你扑来,距离你2米')
        time.sleep(4)
        print('DOD')
        box=input()
        if box=='a':
            print('你使用了一招')
        elif box=='d':
            print('你使用了普攻')
        elif box=='s':
            print('你使用了第二招')
else:
    print('你的输入不符合系统内置操作，请重启游戏')
    quit()
time.sleep(2)
print('你把他们都杀死了')
time.sleep(1)
print('系统奖励:一次性大招,攻击力:100,距离:400米,使用输入xyz,血量提升至:100')
one=0
time.sleep(5)
print('系统预警:第一关的Boss来临')
time.sleep(2)
print('你前面出现了一座“山”')
time.sleep(2)
print('系统提醒:获野兽孟,也称第一关的BOSS,血量:200,攻击力:5,速度:巨慢,数量:1,距离:20米')
boss=200
time.sleep(3)
print('获野兽孟攻击了你')
blood-=1
time.sleep(2)
print('剩余血量:'+str(blood)+' ,Boss血量:'+str(boss))
time.sleep(2)
print('DOD')
box=input()
if box=='d':
    print('你攻击了他')
    boss-=15
elif box=='a':
    print('你使用了一招')
    boss-=30
elif box=='s':
    print('你使用了二招')
    boss-=50
elif box=='xyz':
    print('你使用了一次性大招')
    one='1'
    boss-=100
if blood>0:
    while boss>=0:
        time.sleep(1)
        print('获野兽孟再次攻击了你')
        blood-=1
        time.sleep(2)
        print('剩余血量:'+str(blood)+' ,Boss血量:'+str(boss))
        time.sleep(2)
        print('DOD')
        box=input()
        if box=='d':
            print('你攻击了他')
            boss-=15
        elif box=='a':
            print('你使用了一招')
            boss-=30
        elif box=='s':
            print('你使用了二招')
            boss-=50
        elif box=='xyz':
            if one==0:
                print('你使用了一次性大招')
                one==1
                boss-=100
print('你杀死了他,你赢了!!!!')
time.sleep(1)
print('系统提示:你第一关通关了!!!')
time.sleep(1)
print('恭喜你'+name+'勇士，你通过了第一关,期待你未来的表现，为了增加游戏自由度，我们决定关闭导览模式，为了阅读下一条信息，请安回车键（enter）')
input()
print('操作成功！')
input()
input('欢迎你'+name+'勇士，这里是第二关，金雕峡谷！')
input('从现在开始，你的武器将变成弓箭，因为系统奖励你的各项分数都将提高，稍后我会为你显示你的信息')
arrow=12
blood+=30
fight+=15
input(' 血量:'+str(blood)+' 攻击力:'+str(fight)+' 弓箭数量:'+str(arrow)+' 距离100米, "d"攻击')
input('第二关，金雕峡谷！')
input('你走出了丛林，看见了远处的一座山，上面有一个巨大的原漩涡')
input('你走了过去。。。')
E_Blood=30
E_Attak=15
E_Life=30
E_Number=3
input('''在路上你遇见了一群狼兵，
系统提示：狼兵,血量:10,速度:慢,攻击力:5,数量3,离你的距离12米
DOD
''')
box=input()
while box=='d':
    arrow-=1
    E_Blood-=fight
    blood-=E_Attak
    E_Life-=fight
    E_Life/=3
    input('剩余血量：'+str(blood)+' ,敌人剩余数量：'+str(E_Life))
input('''成功！你打败了狼兵！你继续向前行走，你遇到了一群鸟，最大的''')