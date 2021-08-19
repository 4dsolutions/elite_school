"""
The Farm Ver 1.3 (thefarm.py)
Modified May 21, 2020

featuring...

a Tractor, for adding to a Farm, but this time it's
a generator function, not a class.

generator that moves forward to a boundary reading
current character, writing current marker.  Fuel
might run out.  The send method may be employed to
tank up, redirect, change the marker.  Farm is an
n x m array, presumably smallish, for interactive
console experiments.
"""

__author__ = 'kurner'

from farmworld import Farm # an ascii canvas

def tractor(thefarm, pos = [0,0], facing="N", marker="O", fuel=10):
    "pos is mutable = current position"

    while True:
        y,x = pos
        changes = yield (thefarm.field[y][x], pos, fuel)
      
        if changes:  # pass status quo if no change key for setting
            print("Incoming updates:", changes)    
            facing = changes.get('facing',facing)
            marker = changes.get('marker',marker)
            fuel   = changes.get('fuel',fuel)
            pos    = changes.get('pos',pos)
            continue

        thefarm.field[y][x] = marker
            
        if fuel > 0:

            if facing   == "N":
                if y > 0:
                    y -= 1
                else:
                    if x > 0:
                        x -= 1
                    else:
                        x = thefarm.w - 1
                    y = thefarm.h - 1

            elif facing == "S":
                if y < thefarm.h - 1:
                    y += 1
                else:
                    if x < thefarm.w - 1:
                        x += 1
                    else:
                        x = 0
                    y = 0

            elif facing == "W":
                if x > 0:
                    x -= 1
                else:
                    if y > 0:
                        y -= 1
                    else:
                        y = thefarm.h - 1
                    x = thefarm.w - 1

            elif facing == "E":
                if x < thefarm.w - 1:
                    x += 1
                else:
                    if y < thefarm.h - 1:
                        y += 1
                    else:
                        y = 0
                    x = 0
                    

            fuel -= 1
            pos = (y,x)

        else:
            return

def tick_tock_test(n):
    # Agile Programming:  TDD is your friend
    thefarm = Farm(20,20, bg = ".")
    print("Empty field, all is peaceful", thefarm, sep="\n\n")  # frame of film
    t1 = tractor(thefarm, pos=[10,10], marker="O", facing="N")
    t2 = tractor(thefarm, pos=[10,11], marker="X", facing="S")
    thefarm.add(t1)
    thefarm.add(t2)
    print("T1 starting:", next(t1))
    print("T2 starting:", next(t2))   
    print("Showing the tractors in a list: ", thefarm.tractors, "===", sep="\n")
    print("A busy day begins...", thefarm, sep="\n\n")  # frame of film

    update1 = {"marker":"*"}
    update2 = {"marker":"!"}
    
    t1.send(update1)
    t2.send(update2)
    
    for arrow_of_time in range(n):
        thefarm.ticktock()  # much physics involved in terms of what's a realistic throughput

    update1 = {"marker":"O"}
    update2 = {"marker":"X"}
    
    t1.send(update1)
    t2.send(update2)
    
    print("After {} ticks of the clock, the tractors have moved...".format(n),
        thefarm, sep="\n\n")  # frame of film

def raster_master():
    thefarm = Farm(5,5, bg = ".")
    t1 = tractor(thefarm, facing="E", marker="^", fuel=1000) 
    thefarm.add(t1)
    next(t1)
    for frame in range(20):
        print("movie frame", frame)
        next(t1)
        print(thefarm)
    t1.send(dict(marker="!"))
    for frame in range(20,28):
        print("movie frame", frame)
        next(t1)
        print(thefarm)
        
if __name__ == "__main__":
    # tick_tock_test(7)
    raster_master()
    
