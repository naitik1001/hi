#Libs
import random
#Init
standardCards=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"] #Standard cards
standardDeck=[]#Deck of 52 cards
cardDetails={}#Number of card of each kind
playerName=""#Name of the player
totalPlayers=0#Total players playing the game
botData={}#Name and the deck of bots
playerDeck=[]#Deck of the player
activePlayer=""#Player who has an active chance
cardsPerPerson=0#Cards distribued per person
sequencePlayer=[]#Sequence in which players will take chances
activeCard=""#Card which is being played right now
deckInHand=[]#Collection of unflushed cards
totalMoves=-1#Total moves played in game
totalPass=0#Total number of passes
lastPlayer=""#Person who played the last move
lastPlayerCard=""#Person who last played the card
passPerson=""#Who passed last
isGameOver=False#Determines the state of the game
playerWon=""#Player who has won the game
#Logic
def PrintRules():
    print("""
          _____
         |A ^  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|""")
    print("This is exactly like the game of bluff but with bot(s) and you can only play 1 card at a time")

def ProduceStandardDeck():
    for i in range(len(standardCards)):
        c=standardCards[i]
        for j in range(4):
            standardDeck.append(c)
    #print(standardDeck,len(standardDeck))
def DistributeCards():
    global playerName,totalPlayers,botData,playerDeck,standardDeck,cardsPerPerson,cardDetails
    isValid=False
    playerName=input("Enter your name:")
    while not isValid:
        tp=int(input("Total number of players you want in your game including you (>=2 & <=4):"))
        if tp>=2 and tp<=10:
            totalPlayers=tp
            isValid=True
    if len(standardDeck)%totalPlayers!=0:
        rem=len(standardDeck)%totalPlayers
        for i in range(rem):
            r=random.randint(0,len(standardDeck)-1)
            standardDeck.pop(r)
    for i in range(len(standardCards)):
        count=standardDeck.count(standardCards[i])
        cardDetails[standardCards[i]]=count
    cardsPerPerson=int(len(standardDeck)/totalPlayers)
    for i in range(cardsPerPerson):
        r=random.randint(0,len(standardDeck)-1)
        c=standardDeck[r]
        playerDeck.append(c)
        standardDeck.pop(r)
    for i in range(totalPlayers-1):
        botDeck=[]
        for j in range(cardsPerPerson):
            r=random.randint(0,len(standardDeck)-1)
            c=standardDeck[r]
            botDeck.append(c)
            standardDeck.pop(r)
        botData[f"Bot {i+1}"]=botDeck
        #print(f"Bot {i+1} Deck:",botData[f"Bot {i+1}"],len(botData[f"Bot {i+1}"]))
    #print("Players Deck:",playerDeck,len(playerDeck))

def PrintPlayerDeck():
    print(f"{playerName}'s deck:{playerDeck}")
def FirstPlayer():
    global activePlayer
    targetCard="Ace"
    isFound=False
    while not isFound:
        for i in range(len(playerDeck)):
            if playerDeck[i]==targetCard:
                activePlayer=playerName
                isFound=True
                break
        if not isFound:
            for x in range(totalPlayers-1):
                name=f"Bot {x+1}"
                deck=botData[name]
                if not isFound:
                    for j in range(cardsPerPerson):
                        if deck[j]==targetCard:
                            activePlayer=name
                            isFound=True
                            break
    print(f"{activePlayer} starts first")
def EstablishSequenceOfPlayers():
    global sequencePlayer
    if activePlayer==playerName:
        sequencePlayer.append(playerName)
        for i in range(totalPlayers-1):
            name=f"Bot {i+1}"
            sequencePlayer.append(name)
    else:
        sequencePlayer.append(activePlayer)
        for i in range(totalPlayers-1):
            name=f"Bot {i+1}"
            if name!=activePlayer:
                sequencePlayer.append(name)
        sequencePlayer.append(playerName)
def IncreaseSequence():
    global sequencePlayer,activePlayer,totalMoves
    p=sequencePlayer.index(activePlayer)
    if p<len(sequencePlayer)-1:
        activePlayer=sequencePlayer[p+1]
    else:
        activePlayer=sequencePlayer[0]
    print(f"It is {activePlayer}'s turn")
def CardCheck(cardToBeTested,standard):
    isFound=False
    if not standard:
        for i in range(len(playerDeck)):
            if playerDeck[i]==cardToBeTested:
                isFound=True
    else:
        for i in range(len(standardCards)):
            if standardCards[i]==cardToBeTested:
                isFound=True
    if isFound:
        return True
    else:
        return False
def ValidateState():
    global sequencePlayer,activePlayer,botData,playerWon
    isOver=False
    indexCurrentPlayer=sequencePlayer.index(activePlayer)
    if indexCurrentPlayer!=0:
        previousPlayer=sequencePlayer[indexCurrentPlayer-1]
        if previousPlayer==playerName:
            if len(playerDeck)==0:
                playerWon=playerName
                isOver=True
        else:
            deckOfBot=botData[previousPlayer]
            if len(deckOfBot)==0:
                playerWon=previousPlayer
                isOver=True
    else:
        previousPlayer=sequencePlayer[len(sequencePlayer)-1]
        if previousPlayer==playerName:
            if len(playerDeck)==0:
                playerWon=playerName
                isOver=True
        else:
            deckOfBot=botData[previousPlayer]
            if len(deckOfBot)==0:
                playerWon=previousPlayer
                isOver=True
    if isOver:
        print(f"{playerWon} has won the game")
        return True
    else:
        return False
def NewSet():
    global activePlayer,activeCard,playerDeck,botData,totalMoves,lastPlayer,totalMoves,deckInHand,lastPlayerCard
    totalMoves=-1
    print("A new active card will be chosen")
    isValid=False
    if activePlayer==playerName:
        PrintPlayerDeck()
        while not isValid:
            realCard=input("Card to be played:")
            isValid=CardCheck(realCard,False)
        deckInHand.append(realCard)
        playerDeck.remove(realCard)
        activeCard=realCard
        bluffBool=input("Do you wanna bluff(y/n):")
        if bluffBool=="y":
            isValid=False
            while not isValid:
                bluffCard=input("Card to be announced(bluff):")
                isValid=CardCheck(bluffCard,True)
            activeCard=bluffCard
    else:
        deckOfBot=botData[activePlayer]
        rRealCard=random.randint(0,len(deckOfBot)-1)
        realCardBot=deckOfBot[rRealCard]
        deckInHand.append(realCardBot)
        deckOfBot.remove(realCardBot)
        activeCard=realCardBot
        #print("Original Card",activeCard)
        rBluffVal=random.random()
        if rBluffVal>0.7:
            rBluffCard=random.randint(0,len(standardCards)-1)
            bluffCardBot=standardCards[rBluffCard]
            activeCard=bluffCardBot
            #print("Bluff Card")
    totalMoves+=1
    lastPlayer=activePlayer
    lastPlayerCard=activePlayer
    print(f"{activePlayer} announced the card - {activeCard}")
    #print("Total Moves",totalMoves)
    #print("Deck Size",len(deckInHand))
    #print("Deck",deckInHand)
def BluffDeckChange(whichPlayer):
    global playerDeck,botData,deckInHand
    if whichPlayer==playerName:
        for i in range(len(deckInHand)):
            playerDeck.append(deckInHand[i])
    else:
        deckBot=botData[whichPlayer]
        for i in range(len(deckInHand)):
            deckBot.append(deckInHand[i])
    deckInHand=[]
def BotCardCheck(botName):
    global activeCard,botData
    deck=botData[botName]
    for i in range(len(deck)):
        if deck[i]==activeCard:
            return True
    return False
def Moves():
    global activePlayer,activeCard,playerDeck,botData,totalPass,totalMoves,lastPlayer,passPerson,deckInHand,lastPlayerCard
    isValid=False
    #print("Total Moves",totalMoves)
    #print("Last Player",lastPlayer)
    if activePlayer==playerName:
        print(f"{activeCard} is the active card")
        PrintPlayerDeck()
        passBool=input("Would you like to pass(y/n):")
        #print("Last Player",lastPlayer)
        if passBool=="y":
            print(f"{playerName} has passed")
            #print("Total Pass Initial",totalPass,"Last Pass Player",passPerson)
            if passPerson=="" or passPerson==lastPlayer:
                totalPass+=1
                passPerson=activePlayer
            else:
                totalPass=0
                passPerson=""
            #print("Total Pass Final",totalPass,"Last Pass Player",passPerson)
            lastPlayer=activePlayer
            return
        totalPass=0
        passPerson=""
        callBool="n"
        if lastPlayerCard!=activePlayer:
            callBool=input("Would you like to call the bluff on last card(y/n):")
        if callBool=="y":
            lastCard=deckInHand[totalMoves]
            #print("Deck",deckInHand)
            if lastCard==activeCard:
                print("Wrong Call")
                BluffDeckChange(playerName)
                activePlayer=lastPlayerCard
                NewSet()
                return
            else:
                print("Right Call")
                BluffDeckChange(lastPlayerCard)
                NewSet()
                return
        else:
            while not isValid:
                cardPlayed=input("Card to be played:")
                isValid=CardCheck(cardPlayed,False)
            deckInHand.append(cardPlayed)
            playerDeck.remove(cardPlayed)
            totalMoves+=1
           # print("Deck",deckInHand)
    else:
        botDeck=botData[activePlayer]
        #print(f"{activePlayer}'s original deck",botDeck)
        isPresent=BotCardCheck(activePlayer)
        rCallVal=random.random()
        rPassVal=random.random()
        if lastPlayerCard!=activePlayer:
            if rCallVal<0.4 or len(deckInHand)>5 : #Calling 
                lastCard=deckInHand[totalMoves]
                if lastCard==activeCard:
                    print(f"{activePlayer} made the wrong call")
                    BluffDeckChange(activePlayer)
                    activePlayer=lastPlayerCard
                    NewSet()
                    return
                else:
                    print(f"{activePlayer} made the right call")
                    if lastPlayerCard==playerName:
                        BluffDeckChange(playerName)
                        PrintPlayerDeck()
                        NewSet()
                        return
                    else:
                        BluffDeckChange(lastPlayerCard)
                        NewSet()
                        return
        elif rPassVal>0.3 and not isPresent: #Passing 
           # print("Last Player",lastPlayer)
            #print("Total Pass Initial",totalPass,"Last Pass Player",passPerson)
            print(f"{activePlayer} has passed")
            if passPerson=="" or passPerson==lastPlayer:
                totalPass+=1
                passPerson=activePlayer
            else:
                totalPass=0
                passPerson=""
            #print("Total Pass Final",totalPass,"Last Pass Player",passPerson)
            lastPlayer=activePlayer
           # print("Deck",deckInHand)
            return
        else:
            passPerson=""
            totalPass=0
            rBluffVal=random.random() #Playing
            if isPresent and rBluffVal<0.7: 
                botDeck.remove(activeCard)
                deckInHand.append(activeCard)
                #print("Card Played:",activeCard)
            else:
                rCardInd=random.randint(0,len(botDeck)-1)
                cardBeingPlayed=botDeck[rCardInd]
                botDeck.remove(cardBeingPlayed)
                deckInHand.append(cardBeingPlayed)
                #print("Card Played:",cardBeingPlayed)
            
           # print("Deck",deckInHand)
            totalMoves+=1
        #print(f"{activePlayer}'s new deck",botDeck)
    print(f"{activePlayer} has played")
    lastPlayer=activePlayer
    lastPlayerCard=activePlayer
    #print("Deck",deckInHand)
   #    print("Total Moves",totalMoves)
    #print("Deck Size",len(deckInHand))
def Flush():
    global totalPass,sequencePlayer
    if totalPass==len(sequencePlayer):
        totalPass=0
        return True
    return False
def Game():
    global isGameOver
    PrintRules()
    ProduceStandardDeck()
    DistributeCards()
    FirstPlayer()
    EstablishSequenceOfPlayers()
    NewSet()
    while not isGameOver:
        if Flush():
            NewSet()
        IncreaseSequence()
        Moves()
        isGameOver=ValidateState()
#Run
Game()