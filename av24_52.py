from collections import defaultdict
from typing import List

def main(inp: str)->int:
    print_procedures = []
    res = 0
    before = defaultdict(list) # list of procedures that must be done after the key
    after = defaultdict(list) # list of procedures that must be done befor

    for line in inp.splitlines():
        if '|' in line:
            a, b = line.strip().split('|')
            before[a] += [b]
            after[b] += [a]
        elif len(line) > 1:
            print_procedures.append(line.split(','))
    
    def check_procedure(inst: List[str])->List[int]:
        for i in range(len(inst)):
            if inst[i] in before.keys():
                sub = inst[:i]
                for bef_num in before[inst[i]]:
                    if bef_num in sub:
                        return False, 0
            if inst[i] in after.keys():
                sub = inst[i:]
                for aft_num in after[inst[i]]:
                    if aft_num in sub:
                        return False, 0
        return True, int(inst[len(inst)//2] if len(inst) % 2 != 0 else 0)
                
    inc = []
    for line in print_procedures:
        if check_procedure(line)[0]:
            res += check_procedure(line)[1]
        else:
            inc.append(line)

    for il in inc:
        inc = True
        x = 0
        while x < len(il):
            for i in range(len(il)):
                front = il[:i]
                back = il[i:]
                if il[i] in before.keys():
                    for bef_num in before[il[i]]:
                        if bef_num in front: # Need to move the procedure to right after the current cursor
                            front.remove(il.index(bef_num))
                            back.insert(0, bef_num)
                            il = front + back
                            continue
                elif il[i] in after.keys():
                    for aft_num in after[il[i]]:
                        if aft_num in back: # Need to move the procedure to right before the current cursor
                            back.remove(il.index(aft_num))
                            front.append(aft_num)
                            il = front + back
                            continue
            x += 1
            print(  )
            inc = False



    return res

if __name__ == "__main__":
    with open('av24_5_input.txt', 'r') as f:
        inp = f.read()

    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    print(main(inp))