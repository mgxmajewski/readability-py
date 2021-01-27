from cs50 import get_string

# Get text to analize from user
givenText = get_string("Text: ");
textLentgh = len(givenText)

# Count letters
def lettersCount():
    letters = 0
    for i in range(textLentgh):
        if ((givenText[i]).isalpha()):
           letters += 1
    return letters
    
# Counts words
def wordsCount():
    words = 0
    for i in range(textLentgh):
        if (givenText[i] == " "):
            words+= 1
    return words + 1