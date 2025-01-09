import numpy as np
from typing import List

def av24_41(inp: List[List[str]]) -> int:
    res = 0
    s1 = 'XMAS'
    s2 = 'SAMX'

    # Create numpyarray
    a = np.array(inp)

    # Get list of diagonals
    def get_diagonals(inp):
        l = []
        for offset in range(-a.shape[0] + 1, a.shape[0]):
            diag = np.linalg.diagonal(a, offset=offset)
            l.append(diag)

        for offset in range(-a.shape[0] + 1, a.shape[0]):
            diag = np.linalg.diagonal(np.fliplr(a), offset=offset)
            l.append(diag)

        return l
    
    # Count occurances of s1 and s2 in diagonals and rows
    def calc_count(a, diags):
        count = 0
        for diag in diags:
            count += int(np.strings.count(''.join(diag), s1)) + int(np.strings.count(''.join(diag), s2))
            
        for line in a:
            count += int(np.strings.count(''.join(line), s1)) + int(np.strings.count(''.join(line), s2))

        for line in a.transpose():
            count += int(np.strings.count(''.join(line), s1)) + int(np.strings.count(''.join(line), s2))

        return count
          
    return calc_count(a, get_diagonals(a))

if __name__ == "__main__":
    with open('av24_4_input.txt', 'r') as f:
        lines = []
        for line in f.readlines():
            row = [x for x in line.strip()]
            lines.append(row)
    
    example = """MMMSXXMASM
                MSAMXMSMSA
                AMXSXMAAMM
                MSAMASMSMX
                XMASAMXAMM
                XXAMMXXAMA
                SMSMSASXSS
                SAXAMASAAA
                MAMMMXMMMM  
                MXMXAXMASX"""
    
    print(av24_41(lines))
    
