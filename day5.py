
from typing import Any
with open("day5.txt") as f:
    inp = f.read()

def split():
    global inp
    inp = [x.strip() for x in inp.splitlines(False)]

def _ids():
    global ids
    ids = []
    for ticket in inp:
        l = list(range(128))
        nums = iter(ticket)
        while len(l) > 1:
            x = next(nums)
            if x == "F":
                l = l[:int(len(l) / 2)]
            else:
                l = l[int(len(l) / 2):]

        c = list(range(8))
        for x in nums:
            if x == "R":
                c = c[int(len(c) / 2):]
            else:
                c = c[:int(len(c) / 2)]

        row = int(l[0])
        col = int(c[0])
        id = (row * 8) + col

        ids.append(id)

def section_1() -> Any:
    return max(ids)


def section_2() -> Any:
    for i in range(len(ids)):
        if i not in ids and i+1 in ids and i-1 in ids:
            return i


# note to self: if todays input is line seperated, uncomment the following line
split()
_ids()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
