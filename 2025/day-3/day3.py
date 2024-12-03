import re


def read_input(filename):
    with open(filename, "r") as f:
        data = f.read().strip()
    return data 


def puzzle1(data):
    res = 0
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    attributes = re.findall(pattern, data)
    for a in attributes:
        res += int(a[0]) * int(a[1])
    print(res)


def puzzle2(data):
    res = 0
    pattern = r"mul\(\d{1,3},\s*\d{1,3}\)|don't\(\)|do\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    proceed = True
    commands = re.findall(pattern, data)
    for cmd in commands:
        if cmd == "do()":
            proceed = True
        elif cmd == "don't()":
            proceed = False
        else:
            if proceed:
                x, y = re.findall(mul_pattern, cmd)[0]
                res += int(x) * int(y)
        print(cmd, res)
    print(res)


def main():
    data = read_input("input3.txt")
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()