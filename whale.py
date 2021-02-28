# coding=utf-8
"""
Created on Thu Mar  5 22:27:24 2020

@author: User
"""


import pygame as pg
import time as t
import random


a = open("whale_name.txt")
f=a.read().splitlines() #cname ename img
k=0
for i in f:
   f[k]=i.split(' ') 
   k+=1
a.close()

pg.init()
pg.mixer.init()
page1=pg.mixer.Sound('page1.wav')
#page2=pg.mixer.Sound('page2.wav')
corrects=pg.mixer.Sound('correct.wav')
wrongs=pg.mixer.Sound('wrong.wav')
push=pg.mixer.Sound('click.wav')
page2 = pg.mixer.music.load('page2.mp3')
icon=pg.image.load('whale.ico') 


screen_size=(800,600)
screen = pg.display.set_mode(screen_size,0,32)
pg.display.set_caption('Whale test')

pg.display.set_icon(icon)
color=(255,255,255)
FontColor=(146,26,255)
running = 1
for i in range(len(f)):
    f[i][2]=pg.image.load(f[i][2]) 
    if i<=41:
        n=int((600/f[i][2].get_width())*f[i][2].get_height())
        f[i][2] = pg.transform.scale(f[i][2],(600,n))

def textbox(text,fontsize,pos,fontcolor,backcolor,screen):
    fontObj = pg.font.Font('TaipeiSansTCBeta-Bold.ttf',fontsize)
    #render
    textsur = fontObj.render(text,True,fontcolor,backcolor)
    #get_rect()
    textRect = textsur.get_rect()
    textRect.center=pos
    screen.blit(textsur,textRect)
    return (textsur,textRect)
def click(start):
    mousepos=pg.mouse.get_pos()
    if start[1].left<=mousepos[0]<=start[1].left+start[1].width and start[1].top<=mousepos[1]<=start[1].top+start[1].height:
        if event.type==pg.MOUSEBUTTONDOWN:
            return True
        else:
            return False
def img(img,pos):
    imgrect = img.get_rect()
    imgrect.center=pos
    screen.blit(img,imgrect)
page1.play(-1)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()  
    screen.fill(color)
    icon = pg.image.load('firstpage.jpg').convert()
    icon.set_alpha(150)
    #icon = pg.transform.scale(icon, (128,128))
    iconpos=icon.get_rect()
    iconpos.center=(400,300)
    screen.blit(icon,iconpos)
    title=textbox('whale test',100,(400,300),(25,25,85),None,screen)
    start=textbox('start',50,(400,400),(25,25,85),None,screen)
    if click(start):
            running=0
            color=(135,206,235)
  
    pg.display.update()

running=1
page1.fadeout(500)
push.play()
playing=0
while running:
    if playing == 0:
        pg.mixer.music.play(-1)
        playing =1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()  
    screen.fill(color)
    Test=textbox('Start test',50,(400,200),(255,255,255),None,screen)
    About=textbox('About',50,(400,300),(255,255,255),None,screen)
    Exit=textbox('exit',50,(700,500),(255,255,255),None,screen) 
    pg.display.update()
    if click(Test):
        push.play()
        #pg.mixer.music.fadeout(500)
        pos=[340,390,440,490]
        q=[0,1,2,3]
        picpos=(400,200)
        choice=['A','B','C','D']
        right=pg.image.load('right.png') 
        wrong=pg.image.load('wrong.png')
        lists=[]
        for i in range(len(f)):
            lists.append(i)      
        picran1=0
        picran2=0   
        picran3=0
        r=0
        score=0

        for i in range(len(f)):
            random.shuffle(q)
            r=random.choice(lists)        
            lists.remove(r)      
            dice=[]
            for i in range(len(f)):
                dice.append(i)
            dice.remove(r)
            #print(len(dice))
            picran1=random.choice(dice)
            dice.remove(picran1)
            picran2=random.choice(dice)
            dice.remove(picran2)      
            picran3=random.choice(dice)
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        pg.quit()  
                screen.fill((50,50,50))
                
                img(f[r][2],picpos)
                answer=textbox(choice[q[0]]+': '+f[r][0],30,(400,pos[q[0]]),FontColor,None,screen)
                
                op1=textbox(choice[q[1]]+': '+f[picran1][0],30,(400,pos[q[1]]),FontColor,None,screen)
                
                op2=textbox(choice[q[2]]+': '+f[picran2][0],30,(400,pos[q[2]]),FontColor,None,screen)
                
                op3=textbox(choice[q[3]]+': '+f[picran3][0],30,(400,pos[q[3]]),FontColor,None,screen)
                pg.display.update()
                if click(answer):
                    corrects.play()
                    #print('right')
                    screen.fill((255,255,255))
                    img(right,(400,300))
                    textbox('正確',50,(400,200),(0,0,0),None,screen)
                    textbox(f[r][0],50,(400,300),(0,0,0),None,screen)
                    textbox(f[r][1],50,(400,400),(0,0,0),None,screen)
                    pg.display.update()
                    t.sleep(0.5)
                    score+=1
                    break
                if click(op1) or click(op2) or click(op3):
                    wrongs.play()
                    #print('wrong')
                    screen.fill((0,0,0))
                    img(wrong,(400,300))
                    textbox('錯誤',50,(400,200),(255,255,255),None,screen)
                    textbox(f[r][0],50,(400,300),(255,255,255),None,screen)
                    textbox(f[r][1],50,(400,400),(255,255,255),None,screen)
                    pg.display.update()
                    t.sleep(0.5)
                    break
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  
            screen.fill((0,0,0,))
            page1.play()
            textbox('your score is ',50,(300,300),(255,255,255),None,screen)
            textbox(str(score),70,(500,300),(255,255,255),None,screen)
            back=textbox('back',50,(700,400),(255,255,255),None,screen)
            pg.display.update()
            if click(back):
                page1.fadeout(300)
                #playing=0
                break
        continue
    if click(Exit):
        push.play()
        running=0    
    if click(About):   
        push.play()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  
            screen.fill((255,10,120))
            li=textbox('species list',50,(400,200),(255,255,255),None,screen)
            message=textbox('message from designer',50,(400,400),(255,255,255),None,screen)
            back=textbox('back',30,(400,500),(255,255,255),None,screen)
            pg.display.update()
            if click(li):
                l=[]
                load=0
                push.play()
                while running:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()  
                    screen.fill((255,10,120))
                    for i in range(len(f)):
                        c=int(i/10)
                        a=i%10
                        if load==0:
                            l.append(textbox(f[i][0],20,(100+c*150,75+a*50),(255,255,255),None,screen))
                        else:
                            textbox(f[i][0],20,(100+c*150,75+a*50),(255,255,255),None,screen)
                    load=1
                    back=textbox('back',30,(700,500),(255,255,255),None,screen)
                    pg.display.update()
                    
                    for i in range(len(l)):
                        if click(l[i]):
                            push.play()
                            screen.fill((255,10,120))
                            textbox(f[i][0],50,(400,100),(255,255,255),None,screen)
                            textbox(f[i][1],30,(400,200),(255,255,255),None,screen)
                            img(f[i][2],(400,400))
                            pg.display.update()
                            #顯示時間
                            t.sleep(2)
                    if click(back):
                        push.play()
                        break
                continue    
            if click(message):
                push.play()
                l=[]
                load=0
                while running:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()  
                    a = open("about.txt")
                    screen.fill((255,10,120))
                    txt = a.readlines()
                    for i in range(len(txt)):
                            textbox(txt[i],30,(400,100+i*50),(255,255,255),None,screen)
                    re=textbox('back',30,(700,500),(255,255,255),None,screen)
                    pg.display.update()
                    if click(re):
                        push.play()
                        break
                continue        

            if click(back):
                push.play()
                break
        continue
                
pg.quit()  
