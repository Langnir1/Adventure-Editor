import json

def getMenuChoice():
    """ Print a menu """
    print("""
        Menu:
        0) Quit
        1) load default game
        2) load a game file
        3) save the current game
        4) edit or add node
        5) play the current game
    """)
    userChoice = input("What will you do? ")
    return userChoice

def getDefaultGame():
    game = {
        "start": ["This is a test", "Start over","start","Quit","quit"],
    }
    return game

def playGame(game):
    """ Play game """
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else: 
            #currentNode gets the playNode's RETURN value. THis allows the node to update and change
            currentNode = playNode(game, currentNode)
            

def playNode(game, node):
    #Variable currentNode gets the game
    currentNode = game[node]
    (desc, menu1, node1, menu2, node2) = currentNode
    print(f"""
    {desc}
    1) {menu1}
    2) {menu2}
    """)
    
    #userChoice enables the game to continue with the nodes
    userChoice = input("What will you do? ")
    if userChoice == "1":
        newNode = node1
    elif userChoice == "2":
        newNode = node2
    else:
        newNode = currentNode
    return newNode

def saveGame(game):
    file = open("game.json", "w")
    json.dump(game, file)
    file.close()
    print("Maybe it ran?")
    
def loadGame():
    file = open("game.json", "r")
    for line in file:
        line = line.strip()
        return line
    file.close()
    
def editNode(game):
    print("Current game status:")
    print(json.dumps(game))
    
    print("Current node names: ")
    for nodeName in game.keys():
        print(f"  {nodeName}")
    
    newNodeName = input("name of node to edit or add: ")
    if newNodeName == nodeName:
        newContent = game[newNodeName]
    else:
        newContent = ["","","","",""]
    
    (desc, menu1, node1, menu2, node2) = newContent
    newDesc = editField("description", desc)
    newMenuA = editField("Menu A", menu1)
    newNodeA = editField("Node A", node1)
    newMenuB = editField("Menu B", menu2)
    newNodeB = editField("Node B", node2)
    return newContent
    
def editField(prompt, currentVal):
    """If user presses enter for a key, keep currentVal
"""
    newVal = input(f"{prompt} ({currentVal}): ")
    if newVal == "":
        newVal = currentVal
    return newVal

def main():
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("Load default game")
        elif userChoice == "2":
            print("load a game file")
            loadGame()
        elif userChoice == "3":
            print("save the current game")
            saveGame(game)
        elif userChoice == "4":
            print("edit or add a node")
            editNode(game)
        elif userChoice == "5":
            print("Play the current game")
            playGame(game)
        else:
            print("Invalid")
main()