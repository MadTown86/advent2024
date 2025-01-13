from collections import defaultdict
from typing import List

def main(inp: str)->int:
    print_procedures = []
    res = 0
    before = defaultdict(list)
    after = defaultdict(list)

    for line in inp.splitlines():
        print(line)
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
                

    for line in print_procedures:
        print(line)
        if check_procedure(line)[0]:
            print(check_procedure(line)[1])
            res += check_procedure(line)[1]
    return res

if __name__ == "__main__":
    with open('av24_4_input.txt', 'r') as f:
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

    print(main(example))