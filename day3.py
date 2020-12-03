
from typing import Any
with open("day3.txt") as f:
    inp = f.readlines()

def section_1() -> Any:
    total = 0
    posx = 0
    for row in inp:
        row = (row*100).replace("\n", "")
        if row[posx] == "#":
            total += 1

        posx += 3

    return total

def section_2() -> Any:

    checks = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    outs = []
    for a, b in checks:
        total = 0
        posx, posy = 0, 0

        while posy < len(inp):
            if (inp[posy]*100).replace("\n", "")[posx] == "#":
                total += 1
            posx += a
            posy += b

        outs.append(total)

    out = outs.pop(0)
    for o in outs:
        out *= o

    return out

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
