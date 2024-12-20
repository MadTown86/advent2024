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
    # Creating defaultdict to store count of each element in bl
    for val in bl:
        dd[val] += 1
    # Loop through al and add multiple of element and its count to res
    for a in al:
        if dd[a]:
            res += a*dd[a]
        else:
            continue
    return res


if __name__ == "__main__":
    print(main())