import re
from typing import List

# I had to look this up and see what I was doing wrong.  Not worth fixing at this point considering I would just re-create the same solution
# I have triple quoted below.

class AoC24_3():
    def __init__(self, text: str, inp_type: str, p_flag: bool = False) -> None:
        self.text = text # Input Text
        self.inp_type = inp_type # Input Type
        self.p_flag = p_flag # Print Flag
        self.first_pattern = r"(?<=do\(\)).*?(?=don\'t\(\))"
        self.last_pattern = r"mul\(\d{1,3}(?:,\d{1,3})?\)"
        self.res = 0


    def first_match(self) -> bool:
        # Calculate res for the active portion before first don't()
            first_chunk = self.text.split("don't()")[0]
            if self.p_flag:
                if len(first_chunk) < 75:
                    print(f'First Chunk: {first_chunk}')
                else:
                    x = 0
                    while x <= len(first_chunk):
                        print(f'First Chunk ->: {first_chunk[x:x+75]}')
                        x += 75
            matches = re.findall(self.last_pattern, first_chunk)
            for match in matches:
                match = match.replace("mul(", "").replace(")", "")
                line = match.strip().split(",")
                if self.p_flag:
                    print(f'Line after replacing "mul(" and ")", stripping then splitting is: {line}')
                if len(line) == 2:
                    x, y = line
                    if x.isdigit() and y.isdigit():
                        self.res += int(x) * int(y)
                        if self.p_flag:
                            print(f'Res after last update of res: {x} + {y} =  {self.res}')
                    else:
                        continue
            return 1
    
    def middle_match(self) -> bool:
        """
        This function will calculate the remaining res after the initial active chunk, but doesn't capture whether last do() is present after don't()
        """
        # Remove initial chunk from text
        rest = 'don\'t()'.join([x for x in self.text.split("don\'t()")[1:]])
        if self.p_flag:
                print(f'Rest: {rest}')
        do_dont_screen = re.findall(self.first_pattern, rest)
        if self.p_flag:
            count = 1
            for item in do_dont_screen:
                if len(item) < 75:
                    print(f'Item #{count}: {item}')
                    count += 1
                else:
                    x = 0
                    while x <= len(item):
                        print(f'String Found Between do() and don\'t() #{count}: {item[x:x+75]}')
                        x += 75
                    count += 1
        for item in do_dont_screen:
            mul_matches = re.findall(self.last_pattern, item)
            # Printing section
            if self.p_flag:
                count = 1
                for item in mul_matches:
                    if len(item) < 75:
                        print(f'Matches For Digits Between Mul(...,...) #{count}: {item}')
                        count += 1
                    else:
                        x = 0
                        while x <= len(item):
                            print(f'Matches For Digits Between Mul(...,...) #{count}: {item[x:x+75]}')
                            x += 75
                        count += 1
            # Calculating res
            for match in mul_matches:
                match = match.replace("mul(", "").replace(")", "")
                line = match.strip().split(",")
                if self.p_flag:
                    print(f'Line after replacing "mul(" and ")", stripping then splitting is: {line}')
                if len(line) == 2:
                    x, y = line
                    if x.isdigit() and y.isdigit():
                        self.res += int(x) * int(y)
                        if self.p_flag:
                            print(f'Res after last update of res: {x} + {y} =  {self.res}')
                    else:
                        continue
        return 1

    def last_match(self) -> bool:
        # Calculate res for the active portion after last don't()
        last_chunk = self.text.split("don't()")[-1]
        do_split = last_chunk.split("do()")
        do_split = do_split[1:]
        last_chunk = 'do()'.join([x for x in do_split])
        
        if self.p_flag:
            if len(last_chunk) < 75:
                print(f'Last Chunk: {last_chunk}')
            else:
                x = 0
                while x <= len(last_chunk):
                    print(f'Last Chunk ->: {last_chunk[x:x+75]}')
                    x += 75
        matches = re.findall(self.last_pattern, last_chunk)
        for match in matches:
            match = match.replace("mul(", "").replace(")", "")
            line = match.strip().split(",")
            if self.p_flag:
                print(f'Line after replacing "mul(" and ")", stripping then splitting is: {line}')
            if len(line) == 2:
                x, y = line
                if x.isdigit() and y.isdigit():
                    self.res += int(x) * int(y)
                    if self.p_flag:
                        print(f'Res after last update of res: {x} + {y} =  {self.res}')
                else:
                    continue
        return 1

    def main(self) -> int:
        if self.first_match():
            if self.middle_match():
                if self.last_match():
                    return self.res
        return 0
    

""" This was a pain, especially considering how I saw someone else solved the problem also using regex"""

"""
* Credit GitHub profile nitekat1124 - https:\\github.com\\nitekat1124\\advent-of-code-2024\\blob\\main\\solutions\\day03.py
import re
    
def part2(data):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, "".join(data))

    enabled = True
    result = 0

    for inst in instructions:
        match inst[0]: -> The concept of setting a switch was awesome my lack of understanding of regex was a miss, I didn't realize it separates out the digits making all of my cleaning and separating unnecessary.
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                result += int(inst[1]) * int(inst[2])

    return result
if __name__ == "__main__":
    with open("av24_3_input.txt", 'r') as file:
        data = file.read()
    print(part2(data))
"""
    
if __name__ == "__main__":
    # 48364229 was too low
    # 53200505 was too low
    # 78715693 ??
    # 83551969 - Incorrect no high/low information
    # 80698289 - ??
    # 84893551 - Correct - need to figure out why mine doesn't do that.
    example="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    with open("av24_3_input.txt", 'r') as file:
        text = file.read()
        text = "".join(text)
    AOC = AoC24_3(text, "str", False)
    print(AOC.main())