# Notes:
# Not proud of this one..., review av24_22_secondtry.py
# I wanted to separate out actions isntead of trying to do everything in one loop through once I reached 8 incorrect answers :/ .

def double_checkit(line):
    line = line[1:]
    increasing = 0
    decreasing = 0

    for x in range(1, len(line)):
        if line[x-1] > line[x]:
            decreasing += 1
        elif line[x-1] < line[x]:
            increasing += 1
        else:
            continue
    if decreasing > increasing:
        for x in range(1, len(line)):
            if line[x-1] > line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                continue
            else:
                return 0
        return 1
    else:
        for x in range(1, len(line)):
            if line[x-1] < line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                continue
            else:
                return 0
        return 1

def checkitright(line):
        orgline = line.copy()
        bad_level = 0
        unsafe = False
        decreasing_bank = 0
        increasing_bank = 0
        for x in range(1, len(line)):
            if line[x-1] > line[x]:
                decreasing_bank += 1
            elif line[x-1] < line[x]:
                increasing_bank += 1
            else:
                continue
        x = 1
        if decreasing_bank > increasing_bank:
            while x < len(line):
                if bad_level >= 2:
                    unsafe = True
                    break
                else:
                    if line[x-1] > line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                        x += 1
                        continue
                    else:
                        removed = line.pop(x)
                        # print(f'{removed=}')
                        bad_level += 1
                
            if unsafe or bad_level >= 2:
                return 0
            else:
                if 0 <= len(orgline) - len(line) <= 1:
                    return 1    
                else:
                    return 0
        else:
            while x < len(line):
                if bad_level >= 2:
                    unsafe = True
                    break
                else:
                    if line[x-1] < line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                        x += 1
                        continue
                    else:
                        removed = line.pop(x)
                        # print(f'{removed=}')
                        bad_level += 1

            if unsafe or bad_level >= 2:
                return 0
            else:
                if 0 <= len(orgline) - len(line) <= 1:
                    return 1
                else:
                    return 0

def main():
    res = 0
    double_check_bin = []
    with open("av24_2_input.txt", 'r') as file:
        file.seek(0)
        lines = file.readlines()
    
    for liner in range(len(lines)):
        line = lines[liner].strip().split()
        line = list(map(int, [x for x in line]))
        orgline = line.copy()     
        
        if not checkitright(line):
            double_check_bin.append((liner, orgline))
        else:
            res += 1

    with open("viewtext.txt", 'w') as file:
        file.truncate()
        for x in double_check_bin:
            file.write(f'{x}\n')
        file.close()
    
    second_round_fight = 0
    print(len(double_check_bin))
    for item in double_check_bin:
        if double_checkit(item[1]):
            second_round_fight += 1
            print(f'{item=}')
        else:
            continue
    
    print(f'{second_round_fight=}')

    return res

if __name__ == "__main__":
    print(main())