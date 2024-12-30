def main():
    with open("av24_2_input.txt", 'r') as file:
        file.seek(0)
        lines = file.readlines()

    safe = 0
    unsafe = False
    for liner in range(len(lines)):
        # print("\n")
        # print(liner)
        line = lines[liner].strip().split()
        line = list(map(int, [x for x in line]))
        # print("safecount: ", safe)
        # print(line)
        orgx = 0
        if line[orgx] == line[orgx+1]:
            continue
        if line[orgx] > line[orgx+1]:
            for x in range(1, len(line)):
                # print(f'({line[x-1]}, {line[x]}) : {abs(line[x]-line[x-1])=}')
                if line[x-1] > line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                    continue
                else:
                    unsafe = True
                    break
            if unsafe:
                unsafe = False
                continue
            else:
                safe += 1
                continue
        else:
            for x in range(1, len(line)):
                # print(f'({line[x-1]}, {line[x]}) : {abs(line[x]-line[x-1])=}')
                if line[x-1] < line[x] and 1 <= abs(line[x] - line[x-1]) <= 3:
                    continue
                else:
                    unsafe = True
                    break
            if unsafe:
                unsafe = False
                continue
            else:
                safe += 1
                continue
    return safe

if __name__ == "__main__":
    print(main())