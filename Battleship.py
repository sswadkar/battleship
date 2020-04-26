# Saraansh Wadkar
#
# Battleship in Python
#
# 4/26/2020
#
# Version 1.1
#
# Random module needed
import random
def printg(grid):
    print("     1    2    3    4    5    6    7    8    9    10")
    print("A ",grid[0])
    print("B ",grid[1])
    print("C ",grid[2])
    print("D ",grid[3])
    print("E ",grid[4])
    print("F ",grid[5])
    print("G ",grid[6])
    print("H ",grid[7])
    print("I ",grid[8])
    print("J ",grid[9])
def placepiece(grid,location,direction,piece):
    #location is list
    if direction == "up":
        count = 0
        try:
            tempx = location[0]
            for i in range(piece):
                 tempx -= 1
                 if tempx < 0:
                     break
                 if grid[tempx][location[1]-1] == ' ':
                     count += 1
            if count == piece:
                tempx = location[0]
                for i in range(piece):
                    tempx -= 1
                    grid[tempx][location[1]-1] = "O"
            return grid
        except Exception:
            return "Direction Incorrent"
    if direction == "left":
        count = 0
        try:
            tempy = location[1]
            for i in range(piece):
                 tempy -= 1
                 if tempy < 0:
                     break
                 if grid[location[0]-1][tempy] == ' ':
                     count += 1
            if count == piece:
                tempy = location[1]
                for i in range(piece):
                    tempy -= 1
                    grid[location[0]-1][tempy] = "O"
            return grid
        except Exception:
            return "Direction Incorrent"
    if direction == "right":
        count = 0
        try:
            tempy = location[1] - 2
            for i in range(piece):
                 tempy += 1
                 if tempy > 10:
                     break
                 if grid[location[0]-1][tempy] == ' ':
                     count += 1
            if count == piece:
                tempy = location[1] - 2
                for i in range(piece):
                    tempy += 1
                    grid[location[0]-1][tempy] = "O"
            return grid
        except Exception:
            return "Direction Incorrect"
    if direction == "down":
        count = 0
        try:
            tempx = location[0] - 2
            for i in range(piece):
                 tempx += 1
                 if tempx > 10:
                     break
                 if grid[tempx][location[1]-1] == ' ':
                     count += 1
            if count == piece:
                tempx = location[0] - 2
                for i in range(piece):
                    tempx += 1
                    grid[tempx][location[1]-1] = "O"
            return grid
        except Exception:
            return "Direction Incorrent"
#checking functions
def check(grid,x,y):
    if grid[x-1][y-1] == "O":
        return False
    else:
        return True
def checkgrid(grid):
    count = 0 
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == "O":
                count += 1
    if count == 14:
        return True
    else:
        return False
def checkwin(grid):
    count = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == "X":
                count += 1
    if count == 14:
        return True
    else:
        return False
def killpiece(grid,location):
    #attacks
    if grid[location[0]-1][location[1]] == "O":
        print("Hit")
        grid[location[0]-1][location[1]] = "X"
    elif grid[location[0]-1][location[1]] == " ":
        print("Miss")
        grid[location[0]-1][location[1]] = "-"
    return grid
playerloc = []
botloc = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]
alpha = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}
playergrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
botgrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
playertobot = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] 
botships = [2,3,4,5]
direction = ["up","down","right","left"]
while checkgrid(botgrid) != True:
    botgrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for i in range(len(botships)):
        try:
            direct = random.choice(direction)
            if direct == "up":
                if botships[i] == 2:
                    tempx = random.randint(2,10)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(2,10)
                        tempy = random.randint(1,10)
                if botships[i] == 3:
                    tempx = random.randint(3,10)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(3,10)
                        tempy = random.randint(1,10)
                if botships[i] == 4:
                    tempx = random.randint(4,10)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(4,10)
                        tempy = random.randint(1,10)
                if botships[i] == 5:
                    tempx = random.randint(5,10)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(5,10)
                        tempy = random.randint(1,10)
            if direct == "down":
                if botships[i] == 2:
                    tempx = random.randint(1,9)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,9)
                        tempy = random.randint(1,10)
                if botships[i] == 3:
                    tempx = random.randint(1,8)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,8)
                        tempy = random.randint(1,10)
                if botships[i] == 4:
                    tempx = random.randint(1,7)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,7)
                        tempy = random.randint(1,10)
                if botships[i] == 5:
                    tempx = random.randint(1,6)
                    tempy = random.randint(1,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,6)
                        tempy = random.randint(1,10)
            if direct == "left":
                if botships[i] == 2:
                    tempx = random.randint(1,10)
                    tempy = random.randint(2,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(2,10)
                if botships[i] == 3:
                    tempx = random.randint(1,10)
                    tempy = random.randint(3,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(3,10)
                if botships[i] == 4:
                    tempx = random.randint(1,10)
                    tempy = random.randint(4,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(4,10)
                if botships[i] == 5:
                    tempx = random.randint(1,10)
                    tempy = random.randint(5,10)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(5,10)
            if direct == "right":
                if botships[i] == 2:
                    tempx = random.randint(1,10)
                    tempy = random.randint(1,9)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(1,9)
                if botships[i] == 3:
                    tempx = random.randint(1,10)
                    tempy = random.randint(1,8)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(1,8)
                if botships[i] == 4:
                    tempx = random.randint(1,10)
                    tempy = random.randint(1,7)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(1,7)
                if botships[i] == 5:
                    tempx = random.randint(1,10)
                    tempy = random.randint(1,6)
                    while check(botgrid,tempx,tempy) != True:
                        tempx = random.randint(1,10)
                        tempy = random.randint(1,6)
            placepiece(botgrid,[tempx,tempy],direct,botships[i])
        except IndexError:
            break
printg(playergrid)
for i in range(len(botships)):
    print("Length of piece:",botships[i])
    userinput = input("Where would you like to put the piece? And in what direction? (ex: A3 right): ")
    info = userinput.split(" ")
    directiona = ""
    info[0] = info[0].rstrip(" ")
    info[1] = info[1].rstrip(" ")
    for x in range(len(info[1])):
        directiona += info[1][x].lower()
    tempx = alpha[info[0][0]]
    tempy = int(info[0][1:])
    temp = [[],[],[],[],[],[],[],[],[],[]]
    for y in range(len(playergrid)):
        for z in range(10):
            temp[y].append(playergrid[y][z])
    playergrid = placepiece(playergrid,[tempx,tempy],directiona,botships[i])
    while temp == playergrid:
        print("Length of piece:",botships[i])
        userinput = input("Where would you like to put the piece? And in what direction? (ex: A3 right): ")
        infoa = userinput.split(" ")
        directionaa = ""
        infoa[0] = infoa[0].rstrip(" ")
        infoa[1] = infoa[1].rstrip(" ")
        for x in range(len(infoa[1])):
            directionaa += infoa[1][x].lower()
        tempx = alpha[infoa[0][0]]
        tempy = int(infoa[0][1:])
        temp = playergrid.copy()
        placepiece(playergrid,[tempx,tempy],directiona,botships[i])
        printg(playergrid)
    printg(playergrid)
print("Time to play, your turn first!")
turn = True
while checkwin(playergrid) != True and checkwin(botgrid) != True:
    if turn == True:
        userinput = input("Where do you want to attack?(ex: A3): ")
        infob = []
        infob.append(alpha[userinput[0]])
        infob.append(int(userinput[1:])-1)
        killpiece(botgrid,infob)
        for y in range(len(botgrid)):
            for z in range(10):
                if botgrid[y][z] == "O":
                    playertobot[y][z] = " "
                else:
                    playertobot[y][z] = botgrid[y][z]
        turn = False
    if turn == False:
        coordinates = random.choice(botloc)
        del botloc[coordinates[0]*10 + coordinates[1]]
        print("Opponents grid: ")
        printg(playertobot)
        print("Bot has made it's attack!")
        killpiece(playergrid,coordinates)
        print("Your grid")
        printg(playergrid)
        turn = True
if checkwin(playergrid) == True:
    print("Bot has won!")
elif checkwin(botgrid) == True:
    print("Player has won!")


