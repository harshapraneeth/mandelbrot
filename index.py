import pygame as pg
from pygame import gfxdraw as gf

length, width = 800, 800
maxi = 100
colors = [(i,255,255) for i in range(256)]
z, mx, my, r = 1, 0, 0, False

def scaled_x(p): return (p-length/2)/(z*100)+mx
def scaled_y(p): return (p-width/2)/(z*100)+my

d = 1
def compute():
    pixels = []
    for px in range(0,length//d):
        for py in range(0, width//d):
            x0, y0 = scaled_x(px), scaled_y(py)
            x, y, i = 0, 0, 0
            while(x*x+y*y <= 4 and i < maxi): x, y, i = x*x-y*y+x0, 2*x*y+y0, i+1
            if i<=25: pixels.append(((px*d, py*d), (0,0,0)))
            if i<=50: pixels.append(((px*d, py*d), (32,32,32)))
            elif i<=75: pixels.append(((px*d, py*d), (128,128,128)))
            elif i<=100: pixels.append(((px*d, py*d), (255,255,255)))
    return pixels

pixels = compute()
pg.init()
screen = pg.display.set_mode((length, width))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                z = z+1
                print('zooming')
                pixels = compute()
                print('done')
            if event.key == pg.K_w:
                my = my+0.2
                print('moving')
                pixels = compute()
                print('done')
            if event.key == pg.K_s:
                my = my-0.2
                print('moving')
                pixels = compute()
                print('done')
            if event.key == pg.K_a:
                mx = mx+0.2
                print('moving')
                pixels = compute()
                print('done')
            if event.key == pg.K_d:
                mx = mx-0.2
                print('moving')
                pixels = compute()
                print('done')
            if event.key == pg.K_r: r = True
    if r:
        r = False
        z, mx, my = 1, 0, 0
        pixels = compute()
    for p in pixels:
        #gf.pixel(screen, p[0][0], p[0][1], p[1])
        pg.draw.rect(screen, p[1], pg.Rect(p[0][0], p[0][1], d, d))
    pg.display.update()
