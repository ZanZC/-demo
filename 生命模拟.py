import os,pygame
from pygame.locals import *
import numpy as np
from scipy import ndimage

def get_pixar(arr,weights):
    states =ndimage.filters.convolve(arr,weights,mode='wrap')

    bools=(states==13)|(states==12)|(states==3)

    return bools.astype(int)

def draw_cross(pixar):
    (posx,posy)=pygame.mouse.get_pos()
    pixar[posx,:]=1
    pixar[:,posy]=1

def draw_pattern(pixar,pattern):
    print pattern

    if pattern=='glider':
        coords=[(0,1),(1,2),(2,0),(2,1),(2,2)]
    elif pattern=='block':
        coords=[(3,3),(3,2),(2,3),(2,2)]
    elif pattern=='exploder':
        coords=[(0,1),(1,2),(2,0),(2,1),(2,2),(3,3)]
    elif pattern=='fpentomino':
        coords=[(2,3),(3,2),(4,2),(3,3),(3,4)]
    pos=pygame.mouse.get_pos()

    xs=np.arange(0,pos[0],10)
    ys=np.arange(0,pos[1],10)

    for x in xs:
        for y in ys:
            for i,j in coords:
                pixar[x+i,y+j]=i

def main():
    pygame.init()

    N=400

    pygame.display.set_mode((N,N))
    pygame.display.set_mode("Life Demo")

    screen=pygame.display.get_surface()

    pixar=random_init(N)
    weights=np.array([[1,1,1]],[1,10,1],[1,1,11])

    cross_on=False

    while True:
        pixar=get_pixar(pixar,weights)

        if cross_on:
            draw_cross(pixar)
        pygame.surfarray.blit_array(screen,pixar*255**3)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==quit:
                return 
            if event.type==MOUSEBUTTONDOWN:
                cross_on=not cross_on
            if event.type==KEYDOWN:
                if event.key==ord('r'):
                    pixar=random_init(N)
                    print "Random init"
                if event.key==ord('g'):
                    draw_pattern(pixar,'glider')
            if event.key==ord('b'):
                draw_pattern(pixar,'block')
            if event.key==ord('e'):
                draw_pattern(pixar,'exploder')
            if event.key==ord('f'):
                draw.pattern(pixar,'fpentomino')
    if _name_ == '_main_':
        main()