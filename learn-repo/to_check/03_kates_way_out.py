# On the first line, you will be given how many rows there are in the maze. On the following n lines,
# you will be given the maze itself. Here is a legend for the maze:
#     • "#" - means a wall; Kate cannot go through there
#     • " " - means empty space; Kate can go through there
#     • "k" - the initial position of Kate; start looking for a way out from there
#  are two options: Kate either gets out or not:
#     • If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
#     • Otherwise, print: "Kate cannot get out".

maze = []
kate_pos = []

for row in range(int(input())):
    maze.append(list(input()))
    if "k" in maze[row]:
        kate_pos = [row, maze[row].index("k")]

r = kate_pos[0]
c = kate_pos[1]
moves = 0


def check_pos(r, c , moves):
    if not (0 <= r <= len(maze) and 0 <= c <= len(maze[0])):
        return moves
    if maze[r][c] == "#":
        return 0
    maze[r][c] = "#"     # mark old positio for no way back



print(maze)
print(len(maze))
print(len(maze[0]))


