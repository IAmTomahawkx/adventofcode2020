#### INCOMPLETE ####

import copy
from typing import Any
with open("day11-1.txt") as f:
    inp: list = f.read()

def split():
    global inp
    inp = [x.strip() for x in inp.splitlines(False)]
    inp = [[False if c != "." else None for c in x] for x in inp]

def section_1() -> Any:
    def find_adjacent(y, x):
        out = []
        if y > 0:
            out += _now[y-1][x-1:x+2]
            print(out)
        if x > 0:
            out.append(_now[y][x-1])
        if x < len(_now[y])-1:
            out.append(_now[y][x+1])
        if y < len(_now)-1:
            out += _now[y + 1][x - 2:x + 2]
        return out

    def do_row(index, row):
        for i, c in enumerate(row):
            if c is None:
                continue

            adj = find_adjacent(index, i)
            #print(adj)
            t = sum([x for x in adj if x is not None])
            if not c and not t:
                _mod[index][i] = True
            elif c and t <= 4:
                _mod[index][i] = False

    def _print(t):
        for _c in t:
            for _x in _c:
                if _x is None:
                    print(".", end="")
                elif _x is True:
                    print("#", end="")
                else:
                    print("L", end="")
            print("\n", end="")
        print("\n")

    _last = []
    _now = copy.deepcopy(inp)
    while _last != _now:
        _mod = copy.deepcopy(_now)
        for _index, _row in enumerate(_now):
            do_row(_index, _row)
        _last = _now
        _now = _mod
        _print(_now)
        _print(_last)

    return sum(sum(c for c in x if c is not None) for x in _now)

def section_2() -> Any:
    return None

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
