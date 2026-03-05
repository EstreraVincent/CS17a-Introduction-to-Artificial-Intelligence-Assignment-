"""
A* Algorithm - Example 1: Grid Maze Navigation
================================================
Finds the shortest path from Start (S) to Goal (G)
on a grid with walls (#).

Author: Binsoy
Subject: Algorithm Design
"""

import heapq

# Grid: 0 = open, 1 = wall
GRID = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

ROWS = len(GRID)
COLS = len(GRID[0])
START = (0, 0)
GOAL  = (6, 6)


def heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found


def print_grid(grid, path):
    path_set = set(path)
    symbols = {START: 'S', GOAL: 'G'}
    print("\n  " + " ".join(str(i) for i in range(COLS)))
    for r in range(ROWS):
        row_str = f"{r} "
        for c in range(COLS):
            cell = (r, c)
            if cell in symbols:
                row_str += symbols[cell] + " "
            elif cell in path_set:
                row_str += "* "
            elif grid[r][c] == 1:
                row_str += "# "
            else:
                row_str += ". "
        print(row_str)


if __name__ == "__main__":
    print("=" * 45)
    print("  A* Algorithm — Example 1: Grid Maze")
    print("=" * 45)
    print("Legend:  S=Start  G=Goal  #=Wall  *=Path  .=Open")

    path = astar(GRID, START, GOAL)

    if path:
        print_grid(GRID, path)
        print(f"\n✅ Path found! Length: {len(path)} steps")
        print("   Route:", " → ".join(str(p) for p in path))
    else:
        print("\n❌ No path found!")
