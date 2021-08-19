"""
FarmWorld Ver 2.2
(farmworld.py)
(gpl) OST, 2011; 4D, 2018

Possible workout:
    Rewrite self.field as a numpy array instead
"""

__author__ = 'kurner'

class Farm:

    def __init__(self, rows=8, columns=8, bg="*"):
        self.h = rows
        self.w = columns
        self.bg = bg  # background character
        self.tractors = []  # like Snake or Dog stomach
        self.field = [list(bg*self.w) for x in range(self.h)]  # model
        self.framenumber = 0
        self.trace = []

    def add(self, tractor):
        self.tractors.append(tractor)

    def ticktock(self):  # controller
        """tick tock o' the clock
        time marches on!
        Advance each tractor in the direction it's facing,
        ignoring stuck tractors already at a fence (some
        types of Tractor are smarter than others about fences).
        """
        for tractor in self.tractors:
            try:
                next(tractor) # state changer
            except StopIteration:
                pass  # harmless stuck tractor signal

        self.framenumber += 1
        return self.framenumber

    def render(self):
        display=""
        for line in self.field:
            display += "".join(line)+"\n"
        return display  # view

    __str__ = render

    def __repr__(self):
        return "Farm({},{}) @ {}".format(self.w, self.h, id(self))


class Tractor:

    def __init__(self, farm , pos = [0,0], facing="N", marker="*" , fuel=100):
        self.thefarm = farm
        self.pos = pos
        self.facing = facing
        self.marker = marker
        self.thefarm.add(self)
        self.fuel = fuel

    def __next__(self):
        """
        Makes me an iterator
        """
        y,x = self.pos

        if self.fuel > 0:

            if self.facing   == "N":
                if y > 0:
                    y -= 1
                else:
                    raise StopIteration

            elif self.facing == "S":
                if y < self.thefarm.h - 1:
                    y += 1
                else:
                    raise StopIteration

            elif self.facing == "W":
                if x > 0:
                    x -= 1
                else:
                    raise StopIteration

            elif self.facing == "E":
                if x < self.thefarm.w - 1:
                    x += 1
                else:
                    raise StopIteration

            self.fuel -= 1
            self.pos = (y,x)

        else:  # outta gas
            raise StopIteration

        return self.thefarm.field[y][x]

    def __iter__(self):
        return self  # because I'm already an iterator

    def plow(self, marker=None):
        if marker:
            self.marker = marker
        y,x = self.pos
        self.thefarm.field[y][x] = self.marker

    def __repr__(self):
        return "Tractor(pos={}, facing={}, marker={}, fuel={})".format(self.pos, self.facing, self.marker, self.fuel)

def wordplow(thefarm, start=[0,0], message="Hello World"):
    "writes messages in thefarm's field"
    if len(message)>0:
        t = Tractor(thefarm, pos=start, facing="E")
        t.plow(message[0])

        for new, old in zip(message[1:], t):
            t.plow(marker = new)


def _test( ):
    print("make a movie")
    thefarm = Farm(20,20)
    print("Empty field, all is peaceful", 
          thefarm.render(), sep="\n\n")  # frame of film
    t1 = Tractor(thefarm, pos=[10,10], marker="O", facing="E")
    t2 = Tractor(thefarm, pos=[10,11], marker="X", facing="W")
    t1.plow() # use default markers
    t2.plow()
    print("Showing the tractors in a list: ", 
          *thefarm.tractors, end="\n===\n", sep="\n")
    
    print("A busy day begins...", thefarm.render(), sep="\n\n")  # frame of film
    t1.plow("*")  # conceal previous locations
    t2.plow("*")
    for frame in range(3):  # try boosting to 11, why no crash?
        thefarm.ticktock()
        print("Advance the film: Frame {}".format(frame))
    t1.plow("O")  # reveal new locations
    t2.plow("X")
    print("After 3 ticks of the clock, the tractors have moved...",
        thefarm.render(), sep="\n\n")  # frame of film

if __name__ == "__main__":
    _test()
