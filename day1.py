
with open("day1-1.txt") as f:
    puzzle = [int(x) for x in f.readlines()]

# part 1

def part1():
    for item in puzzle:
        for item1 in puzzle:
            if item + item1 == 2020:
                print(f"Answer is {item} + {item1} = 2020. {item}*{item1}={item*item1}")
                return

part1()

# part 2

def part2():
    for item in puzzle:
        for item1 in puzzle:
            for item2 in puzzle:
                if item + item1 + item2 == 2020:
                    print(f"Answer 2 is {item} + {item1} + {item2} = 2020. {item}*{item1}*{item2}={item*item1*item2}")
                    return

part2()