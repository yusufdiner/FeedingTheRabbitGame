board1 = input("\nPlease enter feeding map as a list:\n").strip(" []").split("], [")
movement1 = input("\nPlease enter direction of movements as a list:\n").strip(" []").split(", ")
board3 = []
movement = []
point = 0
y = 0  # line of rabbit position
x = 0  # column of rabbit position
for a in movement1:
    movement.append(a[1:-1])

for s in range(len(board1)):
    board3.append(board1[s].strip("'").split("', '"))
board = board3
print("\nYour board is:")
for k in range(len(board)):
    print(*board[k])
for i in range(len(board)):
    lists = board[i]
    if lists.count("*") == 1:
        y = y + i
        z = lists.index("*")
        x = x + z
        break
for j in movement:
    if j == "U":
        if y - 1 > -1:
            if board[y - 1][x] == "X":
                board[y - 1][x] = "*"
                board[y][x] = "X"
                y = y - 1
            elif board[y - 1][x] == "A":
                board[y - 1][x] = "*"
                board[y][x] = "X"
                point += 5
                y = y - 1
            elif board[y - 1][x] == "C":
                board[y - 1][x] = "*"
                board[y][x] = "X"
                point += 10
                y = y - 1
            elif board[y - 1][x] == "M":
                board[y - 1][x] = "*"
                board[y][x] = "X"
                point += -5
                y = y - 1
            elif board[y - 1][x] == "P":
                board[y - 1][x] = "*"
                board[y][x] = "X"
                break
            elif board[y - 1][x] == "W":
                pass
        else:
            pass
    elif j == "D":
        if y + 1 < len(board):
            if board[y + 1][x] == "X":
                board[y + 1][x] = "*"
                board[y][x] = "X"
                y = y + 1
            elif board[y + 1][x] == "A":
                board[y + 1][x] = "*"
                board[y][x] = "X"
                point += 5
                y = y + 1
            elif board[y + 1][x] == "C":
                board[y + 1][x] = "*"
                board[y][x] = "X"
                point += 10
                y = y + 1
            elif board[y + 1][x] == "M":
                board[y + 1][x] = "*"
                board[y][x] = "X"
                point += -5
                y = y + 1
            elif board[y + 1][x] == "P":
                board[y + 1][x] = "*"
                board[y][x] = "X"
                y = y + 1
                break
            elif board[y + 1][x] == "W":
                pass
        else:
            pass
    elif j == "R":
        if x + 1 < len(board[0]):
            if board[y][x + 1] == "X":
                board[y][x + 1] = "*"
                board[y][x] = "X"
                x = x + 1
            elif board[y][x + 1] == "A":
                board[y][x + 1] = "*"
                board[y][x] = "X"
                point += 5
                x = x + 1
            elif board[y][x + 1] == "C":
                board[y][x + 1] = "*"
                board[y][x] = "X"
                point += 10
                x = x + 1
            elif board[y][x + 1] == "M":
                board[y][x + 1] = "*"
                board[y][x] = "X"
                point += -5
                x = x + 1
            elif board[y][x + 1] == "P":
                board[y][x + 1] = "*"
                board[y][x] = "X"
                x = x + 1
                break
            elif board[y][x + 1] == "W":
                pass
        else:
            pass

    elif j == "L":
        if x - 1 > -1:
            if board[y][x - 1] == "X":
                board[y][x - 1] = "*"
                board[y][x] = "X"
                x = x - 1
            elif board[y][x - 1] == "A":
                board[y][x - 1] = "*"
                board[y][x] = "X"
                point += 5
                x = x - 1
            elif board[y][x - 1] == "C":
                board[y][x - 1] = "*"
                board[y][x] = "X"
                point += 10
                x = x - 1
            elif board[y][x - 1] == "M":
                board[y][x - 1] = "*"
                board[y][x] = "X"
                point += -5
                x = x - 1
            elif board[y][x - 1] == "P":
                board[y][x - 1] = "*"
                board[y][x] = "X"
                x = x - 1
                break
            elif board[y][x - 1] == "W":
                pass
        else:
            continue
    else:
        break
print("\nYour output should be like this: ")
for q in board:
    print(*q)
print("Your score is: {0}".format(str(point)))