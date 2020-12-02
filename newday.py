import requests

no = int(input("dayno: "))

code = f"""
from typing import Any
with open("day{no}.txt") as f:
    inp = f.read()

def section_1() -> Any:
    return None

def section_2() -> Any:
    return None

print(f"section 1 answer: {{section_1()}}")
print(f"section 2 answer: {{section_2()}}")
"""

# this should be your adventofcode.com cookie, the api requires it to get the day input
with open("cookie.txt") as f:
    cookie = f.read().strip()

with requests.get(f"https://adventofcode.com/2020/day/{no}/input", headers={"cookie": cookie}) as f:
    if f.status_code != 200:
        raise ValueError(f"something fucked up: {f.status_code}, {f.reason}, {f.text}")

    data = f.text

with open(f"day{no}.txt", "w") as f:
    f.write(data)

with open(f"day{no}.py", "w") as f:
    f.write(code)

