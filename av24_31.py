import re

def main():
    res = 0
    with open("av24_3_input.txt", 'r') as file:
        blobbiekins = file.read()

    pattern2 = r'mul\(\d{1,3}(?:,\d{1,3})?\)'
    # Reitterating How Above Works to Commit To Memory
    # mul\( - matches the string mul( - you have to escape the (
    # \d{1,3} - matches 1 to 3 digits
    # (?:,\d{1,3})? - matches a comma followed by 1 to 3 digits, 
    # the ?: is a non-capturing group
    # \) - matches the closing bracket

    matches = re.findall(pattern2, blobbiekins)

    cleaned = []
    for match in matches:
        match = match.replace("mul(", "").replace(")", "")
        cleaned.append(match)

    for match in cleaned:
        line = match.split(",")
        if len(line) == 2:
            x, y = line
            if x.isdigit() and y.isdigit():
                res += int(x) * int(y)
            else:
                continue
    
    return res

if __name__ == "__main__":
    # 158982546 - this was too low have to check the regex
    print(main())