
from typing import Any
with open("day12.txt") as f:
    inp: list = f.read()

def split():
    global inp
    inp = [x.strip() for x in inp.splitlines(False)]

def section_1() -> Any:
    direction = 90
    posx = posy = 0

    for instr in inp:
        if instr[0] in "NS":
            posy += int(instr[1:]) if instr[0] == "N" else -int(instr[1:])
        elif instr[0] in "WE":
            posx += int(instr[1:]) if instr[0] == "E" else -int(instr[1:])
        elif instr[0] == "F":
            if direction in (0, 180):
                posy += int(instr[1:]) if direction == 0 else -int(instr[1:])
            elif direction in (90, 270):
                posx += int(instr[1:]) if direction == 90 else -int(instr[1:])
            else:
                raise ValueError(direction)
        elif instr[0] in "LR":
            direction = (direction + (int(instr[1:]) if instr[0] == "R" else -int(instr[1:]))) % 360

    return abs(posx) + abs(posy)

def section_2() -> Any:
    posx = posy = 0
    wayx, wayy = 10, 1 # relative

    for instr in inp:
        if instr[0] == "F":
            posx += wayx * int(instr[1:])
            posy += wayy * int(instr[1:])
        elif instr[0] in "NS":
            wayy += int(instr[1:]) if instr[0] == "N" else -int(instr[1:])
        elif instr[0] in "WE":
            wayx += int(instr[1:]) if instr[0] == "E" else -int(instr[1:])
        elif instr[0] in "LR":
            n = int(instr[1:])
            for _ in range(((n if instr[0] == "L" else -n) // 90 ) % 4):
                wayx, wayy = -wayy, wayx

    return abs(posx) + abs(posy)


# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
