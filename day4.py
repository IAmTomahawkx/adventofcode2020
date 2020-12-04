
from typing import Any
with open("day4.txt") as f:
    inp = f.read()

def split():
    global inp
    _inp = []
    this = ""
    for row in inp.splitlines(False):
        if not row.strip():
            _inp.append(this.strip())
            this = ""
        else:
            this += row + " "

    inp = _inp


def section_1() -> Any:
    required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    total = 0
    for item in inp:
        contains = []
        for i in item.split():
            contains.append(i.split(":")[0])

        if all(x in contains for x in required):
            total += 1

    return total

def section_2() -> Any:
    required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    total = 0
    for item in inp:
        contains = []
        for i in item.split():
            key, value = i.split(":")
            if key == "byr":
                if value.isnumeric() and 1920 <= int(value) <= 2002:
                    contains.append(key)
            elif key == "iyr":
                if value.isnumeric() and 2010 <= int(value) <= 2020:
                    contains.append(key)
            elif key == "eyr":
                if value.isnumeric() and 2020 <= int(value) <= 2030:
                    contains.append(key)
            elif key == "hcl":
                if value.startswith("#") and value[1:].isalnum():
                    contains.append(key)
            elif key == "hgt":
                if not value.isalnum():
                    continue
                if value.endswith("cm"):
                        if 150 <= int(value.replace("cm", "")) <= 193:
                            contains.append(key)

                elif value.endswith("in"):
                    if 59 <= int(value.replace("in", "")) <= 76:
                        contains.append(key)
            elif key == "ecl":
                if value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    contains.append(key)
            elif key == "pid":
                if len(value) == 9 and value.isnumeric():
                    contains.append(key)

        if all(x in contains for x in required):
            total += 1

    return total

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
