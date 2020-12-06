import string

from typing import Any
with open("day6.txt") as f:
    inp = f.read()


def split():
    global inp
    _inp = []
    this = []
    for row in inp.splitlines(False):
        if not row.strip():
            _inp.append(this)
            this = []
        else:
            this.append(row)

    if this:
        _inp.append(this)

    inp = _inp

def section_1() -> Any:
    total = 0
    for group in inp:
        people = group
        has = set()
        for p in people:
            has.update(p)

        total += len(has)

    return total


def section_2() -> Any:
    total = 0
    for group in inp:
        for s in string.ascii_lowercase:
            if all(s in x for x in group):
                total += 1

    return total

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
