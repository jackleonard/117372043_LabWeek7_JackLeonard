from filemanager import DeckFileManager

# this is the main code.
char_pressed = None

deckA = DeckFileManager()
deckB = DeckFileManager()
deckC = DeckFileManager()
deckD = DeckFileManager()
while char_pressed != 'q': 
  # this will continue to loop until the participant clicks 'q' key
    char_pressed = input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    if char_pressed == 'a': # character 'a' refers to Deck A
      deckA.getWinsLoses()
      print(deckA.getWins())
      print(deckA.getLosses())
      print(deckA.getDeckNumber())
      print(deckA.getRowNumber()) #Testing get row number
      print(deckA)
      #print(deckA.setRowNumber(15)) #Testing set Row Number




    elif char_pressed == 'b': # character 'b' refers to Deck B
      deckB.getWinsLoses()
      print(deckB.getWins())
      print(deckB.getLosses())
      print(deckB.getDeckNumber())
      print(deckB.getRowNumber())

      #print(deckB)
      #print("character b has been pressed")


    elif char_pressed == 'c': # character 'c' refers to Deck C
      deckC.getWinsLoses()
      print(deckC.getWins())
      print(deckC.getLosses())
      print(deckC.getDeckNumber())
      print(deckC.getRowNumber())


    elif char_pressed == 'd': # character 'd' refers to Deck UnicodeDecodeError
      deckD.getWinsLoses()
      print(deckD.getWins())
      print(deckD.getLosses())
      print(deckD.getDeckNumber())
      print(deckD.getRowNumber())



