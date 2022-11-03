from Field import Field
import os

fields = []
turn = False
x = 0

while x < 9:
    fieldToAdd = Field(x)
    fields.append(fieldToAdd)
    x += 1

def printField():
    print(fields[0].value + '|' + fields[1].value + '|' + fields[2].value)
    print('------')
    print(fields[3].value + '|' + fields[4].value + '|' + fields[5].value)
    print('------')
    print(fields[6].value + '|' + fields[7].value + '|' + fields[8].value)

def checkForWin():
    if fields[0].value ==  fields[1].value == fields[2].value:
        return fields[0].value
    elif  fields[3].value ==  fields[4].value == fields[5].value:
        return fields[3].value
    elif  fields[6].value ==  fields[7].value == fields[8].value:
        return fields[6].value
    elif  fields[0].value ==  fields[3].value == fields[6].value:
        return fields[0].value
    elif  fields[1].value ==  fields[4].value == fields[7].value:
        return fields[1].value
    elif  fields[2].value ==  fields[5].value == fields[8].value:
        return fields[2].value
    elif  fields[0].value ==  fields[4].value == fields[8].value:
        return fields[0].value
    elif  fields[2].value ==  fields[4].value == fields[6].value:
        return fields[2].value
    else:
        return False

def win():
    os.system('cls')
    winner = checkForWin()
    print('player ' + winner + ' wins :)')

def startGame(startNotice):
    global turn
    os.system('cls')
    print(startNotice)
    if turn == False:
        startingPlayerInput = input('hwo starts the game X or O: ')
        if startingPlayerInput == 'X' or startingPlayerInput == 'x':
            turn = 'X'
        elif startingPlayerInput == 'O'  or startingPlayerInput == 'o':
            turn = 'O'
        else:
            startGame('that was not an option')
    printField()
    try:
        chosenField = int(input('player ' + turn + ' chose a field: '))
    except:
        startGame('please chose a valid field')

    if chosenField < 9 and fields[chosenField].checked == False:
        fields[chosenField].value = turn
        fields[chosenField].checked = True
    else:
        startGame('please chose a valid field')

    if checkForWin():
        win()
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        startGame(' ')

# start the game
os.system('cls')
startGame(' ')