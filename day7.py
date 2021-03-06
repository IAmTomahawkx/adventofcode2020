
from typing import Any
with open("day7.txt") as f:
    inp = f.read().splitlines()

def split():
    global inp
    inp = [x.strip() for x in inp.splitlines(False)]

bags = {}

for line in inp:
    name, contents = line[:-1].split(" contain ", 1)
    if contents == "no other bags":
        items = {}
    else:
        t = contents.split(",")
        items = {}
        for item in t:
            item = item.split()
            no = int(item[0])
            rest = " ".join(item[1:]).replace("bags", "bag").strip()
            items[rest] = no

    bags[name.replace("bags", "bag").strip()] = items

def find_golden_bags(bag):
    if bag == "shiny gold bag":
        return True

    deps = bags[bag]
    for typ in deps:
        if find_golden_bags(typ):
            return True
    return False

def count_bags(bag, ind=1):
    count = 1
    for a, b in bags[bag].items():
        print("-"*ind, count, b, a)
        count += b * count_bags(a, ind+1)

    return count

def section_1() -> Any:
    count = sum(find_golden_bags(x) for x in bags) -1
    return count

def section_2() -> Any:
    return count_bags("shiny gold bag") - 1

# note to self: if todays input is line seperated, uncomment the following line
#split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
