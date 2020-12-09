
from typing import Any
with open("day9.txt") as f:
    inp = f.read()

def split():
    global inp
    inp = [int(x.strip()) for x in inp.splitlines(False)]

def section_1() -> Any:
    pream = 25
    index = pream

    def once():
        valid = inp[index - pream:index]
        n = inp[index]
        for a in valid:
            for b in valid:
                if a + b == n:
                    return True
        return False

    while index < len(inp):
        if not once():
            return inp[index]
        index += 1


def section_2() -> Any:
    pream = 25
    index = pream

    def once():
        valid = inp[index - pream:index]
        n = inp[index]
        for a in valid:
            for b in valid:
                if a + b == n:
                    return True
        return False

    def find():
        n = inp[index]
        ind = 0
        nums = []
        while True:
            for i in range(ind, len(inp)):
                nums.append(inp[i])
                if sum(nums) == n:
                    return min(nums) + max(nums)
                if sum(nums) > n:
                    break

            ind += 1
            if ind == len(inp):
                return None
            nums.clear()


    while index < len(inp):
        if not once():
            return find()
        index += 1

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
