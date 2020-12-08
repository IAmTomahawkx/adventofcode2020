import prettify_exceptions
prettify_exceptions.hook()

from typing import Any
with open("day8.txt") as f:
    inp = f.read()
instructions = []

def split():
    global inp
    inp = [x.strip() for x in inp.splitlines(False)]

    for inst in inp:
        l, r  = inst.split()
        instructions.append((l, int(r)))

def section_1() -> Any:
    acc = 0
    index = 0
    ran = []

    while True:
        instr, val = instructions[index]

        if index in ran:
            print(index)
            break

        ran.append(index)

        if instr == "nop":
            index += 1

        elif instr == "acc":
            acc += val
            index += 1

        elif instr == "jmp":
            index += val

    return acc

def section_2() -> Any:
    acc = 0
    index = 0
    ran = []

    def _try(instrs):
        _acc = acc
        _index = index
        _ran = ran.copy()
        while True:
            if _index == len(instrs):
                return True, _acc

            instr, val = instrs[_index]

            if _index in _ran:
                return False, -1

            _ran.append(_index)

            if instr == "nop":
                _index += 1

            elif instr == "acc":
                _acc += val
                _index += 1

            elif instr == "jmp":
                _index += val

    for i, (inst, op) in enumerate(instructions):
        if inst in ("nop", "jmp"):
            _inst = instructions.copy()
            _inst[i] = ("nop" if inst == "jmp" else "jmp", op)
            suc, ac = _try(_inst)
            if suc:
                return ac

# note to self: if todays input is line seperated, uncomment the following line
split()

print(f"section 1 answer: {section_1()}")
print(f"section 2 answer: {section_2()}")
