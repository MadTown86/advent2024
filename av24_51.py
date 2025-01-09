from collections import defaultdict

def main(inp: str)->int:
    print_procedures = []
    before = defaultdict(list)
    after = defaultdict(list)

    for line in inp.splitlines():
        print(line)
        if '|' in line:
            a, b = line.strip().split('|')
            print(a, b)
            before[a] += [b]
            after[b] += [a]
        elif len(line) > 1:
            print_procedures.append(line.split(','))
    
    print(before)
    print(after)

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