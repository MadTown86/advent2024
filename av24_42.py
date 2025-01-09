from typing import List

def main(text: str) -> int:
    translated_inp = []
    for line in text.splitlines():
        translated_inp.append([x for x in line.strip()])

    count = 0
    alright_alright = ['MSMS', 'MMSS', 'SMSM', 'SSMM']
    for line in range(1, len(translated_inp)-1):
        for x in range(1, len(translated_inp[line])-1):
            if translated_inp[line][x] == 'A':
                term = ''.join([translated_inp[line-1][x-1], translated_inp[line-1][x+1], translated_inp[line+1][x-1], translated_inp[line+1][x+1]])
                if term in alright_alright:
                    count += 1

    return count

if __name__ == "__main__":
    with open('av24_4_input.txt', 'r') as f:
        inp = f.read()

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
    assert main(example) == 9
    print(main(inp))