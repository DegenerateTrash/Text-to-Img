from PIL import Image
import time
import os
import math
import re
import cProfile

def main():
    

    userin = open(str(input("Give file to convert: ")),"r", encoding="utf-8") 
    #userin = open(__file__).read() 
    userin = userin.read()
    start = time.time()
    f = 0
    while True:
        if not len(userin) % 3 == 0 and f != 0:
            userin = userin + "0"
        elif not len(userin) % 3 == 0 and f == 0:
            userin = userin + "\n"
            f+=1
        else:
            break
    #print(userin)
    while True:
        if len(userin) % 3 == 0 and not(float(pow(len(userin),0.5)).is_integer()):
            userin = userin + "000"
            #print(userin)
        else:
            break
    #print(userin)
    print(len(userin))
    r=[]
    g=[]
    b=[]
    try:
        for x in range(0,len(userin),3):
            r.append(userin[x])
        for x in range(1,len(userin),3):
            g.append(userin[x])
        for x in range(2,len(userin),3):
            b.append(userin[x])
    except:
        f = 0
    ou = Image.new("RGB", (int(pow(len(userin),0.5)),int(pow(len(userin),0.5))), color="cyan")
    #ou2 = Image.new("RGB", (len(r),1), color="black")
    i = 0
    """ I am now going to attempt to make a square image
            To do this i require the input to be formatted so that the input is a muliple of three
            while giving an integer after being square rooted"""
    i=0
    yt = 0
    xt = 0
    h=0
    print(userin)
    for y in range(0,int(pow(len(userin),0.5)),1):
        yt +=1
        for x in range(0,int(pow(len(userin),0.5)),1):
            col = (0,0,0)
            if h == 0:
                xt +=1
            try:
                col = (ord(r[i]),ord(g[i]),ord(b[i]))
            except:
                f=0
            i+=1
            ou.putpixel((x,y),col)
            #if i < len(r):
                #ou2.putpixel((x,y),col)
                #i+=1
        h+=1
    #for y in range(0,int(pow(len(userin),0.5)),1):
    #    for x in range(0,int(pow(len(userin),0.5)),1):
    #       ou.putpixel((x,y),(0,0,0))
    print("Sqrroot: {0}".format(pow(len(userin),0.5)))
    print("{0}y".format(yt))
    print("{0}x".format(xt))
    print("Took {0:0.20f} seconds for a {1} char txt file".format(time.time() - start, len(userin)))
    ou.show()
    #ou.save(str(input("Provide a name + extension for storage: ")))
    ou.save("output.png")
    #ou2.save("out1px.png")
    #print(userin)
    return
#prof = cProfile.Profile()
#prof.enable()
main()
#prof.disable()
#prof.print_stats(sort="time")