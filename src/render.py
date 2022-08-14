def render(grid):
    for y_pos, line in enumerate(grid):
        for x_pos, val in enumerate(line):
            print(val, end="")
            if (x_pos+1) % 9 == 0:
                continue
            if (x_pos+1) % 3 == 0:
                print(" | ", end="")

        print()
        if (y_pos+1) % 9 == 0:
            continue
        if (y_pos+1) % 3 == 0:
            print("---------------")
        

if __name__ == "__main__":
    grid = [
        [0,2,0,0,0,0,0,0,0],
        [0,0,0,6,0,0,0,0,3],
        [0,7,4,0,8,0,0,0,0],
        [0,0,0,0,0,3,0,0,2],
        [0,8,0,0,4,0,0,1,0],
        [6,0,0,5,0,0,0,0,0],
        [0,0,0,0,1,0,7,8,0],
        [5,0,0,0,0,9,0,0,0],
        [0,0,0,0,0,0,0,4,0]
    ]

    render(grid)