# Not great, need to get better at this.

from typing import List

def main():
    res = 0
    leftovers_1 = []
    leftovers_2 = []
    with open("av24_2_input.txt", 'r') as file:
        file.seek(0)
        lines = file.readlines()

    for numb, x in enumerate(lines):
        line = list(map(int, x.strip().split()))
        orgline = line.copy()
        if chk_straightup(line):
            res += 1
            continue
        elif chk_straightdown(line):
            res += 1
            continue
        else:
            leftovers_1.append((numb, line))

    for x in leftovers_1:
        line = x[1]
        orgline = line.copy()
        if chk_up(line):
            res += 1
            continue
        elif chk_down(line):
            res += 1
            continue
        else:
            leftovers_2.append((x[0], orgline))
    
    return res


def chk_straightup(line: List[int]) -> bool:
    """Check if the line is ascending and the difference between each element is 1-3"""
    for x in range(1, len(line)):
        if line[x-1] < line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
            continue
        else:
            return 0
    return 1

def chk_straightdown(line: List[int]) -> bool:
    """Check if the line is descending and the difference between each element is 1-3"""
    for x in range(1, len(line)):
        if line[x-1] > line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
            continue
        else:
            return 0
    return 1

def chk_up(line: List[int]) -> bool:
    """Check if the line is ascending and the difference between each element is 1-3"""
    # Includes removal of one false level check
    orgline = line.copy()
    bad_level = 0
    x = 1
    while x < len(line):
        if bad_level >= 2:
            return 0
        else:
            if line[x-1] < line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                x += 1 # Note x is only incremented upon passing criteria
                continue
            else:
                # Remove first element that doesn't fit the criteria
                line.pop(x)
                bad_level += 1
    if bad_level < 2 and 0 <= len(orgline) - len(line) <= 1:
        return 1
    else:
        return 0
        
def chk_down(line: List[int]) -> bool:
    """Check if the line is descending and the difference between each element is 1-3"""
    orgline = line.copy()
    bad_level = 0
    x=1
    while x < len(line):
        if bad_level >= 2:
            return 0
        else:
            if line[x-1] > line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                x += 1
                continue
            else:
                line.pop(x)
                bad_level += 1
    if bad_level < 2 and 0 <= len(orgline) - len(line) <= 1:
        return 1
    else:
        return 0

if __name__ == "__main__":
    assert(main() == 488)