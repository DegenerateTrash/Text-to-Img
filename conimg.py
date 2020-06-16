import os
from PIL import Image
import time
import cProfile
import numpy as np
Image.MAX_IMAGE_PIXELS = 933120000

def main():
    im = Image.open(str(input("Image Name: ")))
    start = time.time()
    red = []
    blu = []
    gre = []
    for y in range(im.height):
        for x in range(im.width):
            red.append(int("{} ".format(im.getpixel((x,y))[0])))
            gre.append(int("{} ".format(im.getpixel((x,y))[1])))
            blu.append(int("{} ".format(im.getpixel((x,y))[2])))
    comblen = len(red)+len(gre)+len(blu)
    i = 0
    ou = ""
    r=0
    g=0
    b=0
    while True:
        #print(red,gre,blu)
        try:
            if i == 0:
                ou = ou + chr(red[r])
                r+=1
            elif i == 1:
                ou = ou + chr(int(gre[g]))
                g+=1
            elif i == 2:
                try:
                    ou = ou + chr(int(blu[b]))
                    b+=1
                except:
                    break
            i += 1
            if i == 3:
                i = 0
        except:
            break
        #print(ou)
        
    outxt = open("output.txt","w",encoding="utf-8")
    outxt.write(ou)
    print("Took {0:0.20f} seconds".format(time.time() - start))
    
    return
prof = cProfile.Profile()
prof.enable()
main()
prof.disable()
prof.print_stats(sort="time")