import re

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
    # Compare and add absolute value of the difference to res
    for a, b in zip(al, bl):
        res += abs(a - b)
    return res


if __name__ == "__main__":
    print(main())