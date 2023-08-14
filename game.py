import pgzrun
from random import randint
HEIGHT=600
WIDTH=1200

music.play('remix')

p=Actor('ironman',(WIDTH//2, HEIGHT//2))
e=Actor('alien',(WIDTH//2, 200))
c=Actor('coin',(WIDTH//2, HEIGHT-200))
score=0
game_state=0

def draw():
    if game_state==0:
      screen.fill('black')
      p.draw()
      e.draw()
      c.draw()
      screen.draw.text(f'Score:{score}',(10,10),color="white")
    elif game_state==1:
        screen.draw.text(f'Game Over',(WIDTH//2, HEIGHT//2),color="red")
    elif game_state==2:
        screen.draw.text(f'You Win',(WIDTH//2, HEIGHT//2),color="green")


def player_update():
    if keyboard.left:
        p.x-=5
    elif keyboard.right:
        p.x += 5
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5

def enemy_update():
    if c.x>e.x:
        e.x+=3
    if c.x<e.x:
        e.x-=3
    if c.y>e.y:
        e.y+=3
    if c.y<e.y:
        e.y-=3
    

    

def score_update():
    global score, game_state
    if p.colliderect(c):
        score+=10
        c.x=randint(0,WIDTH)
        c.y=randint(0,HEIGHT)
        sounds.action.play()
    if e.colliderect(c):
        score-=10
        c.x=randint(0,WIDTH)
        c.y=randint(0,HEIGHT)
        sounds.action.play()
    if score<=-50:
        game_state=1 #game over
    if score>=50:
        game_state =2#win





def update():
    if game_state==0:
      enemy_update()
      player_update()
      score_update()

pgzrun.go()