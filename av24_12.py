import re
from collections import defaultdict

def main():
    with open("av24_1_input.txt", 'r') as file:
        lines = file.readlines()
    al = []
    bl = []
    res = 0
    for line in lines:
        # Remove extra spaces and split the line into two numbers
        text = re.sub(r"(\d)\s{2,}(\d)", r"\1 \2", line.strip()).split(" ")
        al.append(int(text[0]))
        bl.append(int(text[1]))
    al.sort()
    bl.sort()
    dd = defaultdict(int)
    for val in bl:
        dd[val] += 1
    print(dd)
    # Compare and add absolute value of the difference to res
    for a in al:
        if dd[a]:
            res += a*dd[a]
        else:
            continue
    return res


if __name__ == "__main__":
    print(main())