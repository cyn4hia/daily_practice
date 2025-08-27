def shift_2d_grid(grid, k):
    # Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
    
    m = len(grid)
    n = len(grid[0])

    for p in range(k):
        last_num = grid[0][0]
        final_num = grid[m-1][n-1]

        for i in range(m):
            for j in range(n):
                current = grid[i][j]
                if j == 0 and i != m-1:
                    grid[i][0] = last_num
                    last_num = current

                elif grid[i][j] == final_num:
                    grid[0][0] = grid[i][j]
                    grid[i][j] = last_num

                else:
                    grid[i][j] = last_num
                    last_num = current

    return grid


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 2
    print(shift_2d_grid(grid, k))