import prettify_exceptions
prettify_exceptions.hook()
from typing import Any
from functools import lru_cache
with open("day10.txt") as f:
    inp: list = f.read()
    _inp = inp

def split():
    global inp
    inp = sorted([int(x.strip()) for x in inp.splitlines(False)])

def section_1() -> Any:
    low, high = 1,1
    for i, n in enumerate(inp):
        if i == len(inp)-1:
            break

        if inp[i+1] - n == 1:
            low += 1
        elif inp[i+1] - n == 3:
            high += 1
        else:
            print(inp[i+1]-n)

    return low*high

@lru_cache(maxsize=None)
def solve(i=0):
    if i == len(inp) - 1:
        return 1
    count = 0
    for j, x in enumerate(inp[i + 1:], i + 1):
        if x - inp[i] > 3: break
        count += solve(j)
    return count

def section_2() -> Any:
    global inp
    inp = [0] + inp + [max(inp)+3]

    @lru_cache(None)
    def find_rest(index):
        if index == len(inp)-1:
            return 1

        count = 0
        for i, n in enumerate(inp[1 + index:], 1+index):
            if 3 < n - inp[index]:
                break

            count += find_rest(i)
        return count

    return find_rest(0)

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
