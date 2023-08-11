import pgzrun

HEIGHT=600
WIDTH=1200

music.play('remix')

p=Actor('ironman',(WIDTH//2, HEIGHT//2))
e=Actor('alien',(WIDTH//2, 200))
c=Actor('coin',(WIDTH//2, HEIGHT-200))

def draw():
    screen.fill('black')
    p.draw()
    e.draw()
    c.draw()

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
    e.x+=5
    if e.x > WIDTH:
        e.x=0

def update():
    enemy_update()
    player_update()

pgzrun.go()