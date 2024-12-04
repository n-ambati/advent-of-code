def read_input(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")
    
    data = [list(line) for line in data]
    return data


def find_xmas(grid, r, c, search_word):
    n_rows = len(grid)
    n_cols = len(grid)
    directions = (
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    )


def puzzle1(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    count = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == "X":
                s = "XMAS"
                i, j = r, c
                it = 0
                # search top
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i -= 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search bottom
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i += 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search right
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    j += 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search left
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    j -= 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search top right
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i -= 1
                    j += 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search bottom right
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i += 1
                    j += 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search bottom left
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i += 1
                    j -= 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
                
                i, j = r, c
                it = 0
                # search top left
                while 0 <= i < n_rows and 0 <= j < n_cols and it < len(s):
                    if grid[i][j] != s[it]:
                        break
                    i -= 1
                    j -= 1
                    it += 1
                else:
                    if it == len(s):
                        count += 1
    return count


def puzzle2(grid):
    count = 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == "A":
                if 0 < r < n_rows - 1 and 0 < c < n_cols - 1:
                    word1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
                    word2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
                    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
                        count += 1
    return count
                

def main():
    data = read_input("sample_input4.txt")
    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()