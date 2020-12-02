with open("day2.txt") as f:
    inp = f.readlines()

valid = 0
for text in inp:
    texts = text.split()
    low, high = texts[0].split('-')
    low, high = int(low), int(high)

    letter = texts[1].replace(":", "")
    if low <= texts[2].count(letter) <= high:
        valid += 1

print(valid)

valid = 0
for text in inp:
    texts = text.split()
    low, high = texts[0].split('-')
    low, high = int(low), int(high)

    letter = texts[1].replace(":", "")
    if (texts[2][low-1] == letter and texts[2][high-1] != letter) or (texts[2][low-1] != letter and texts[2][high-1] == letter):
        valid += 1

print(valid)