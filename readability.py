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
    
# Count words
def wordsCount():
    words = 0
    for i in range(textLentgh):
        if (givenText[i] == " "):
            words+= 1
    return words + 1

# Count sentences
def sentencesCount():
    sentences = 0
    for i in range (textLentgh):
        if (givenText[i] == "." or givenText[i] == "!" or  givenText[i] == "?"):
            sentences+=1
    return sentences
    
# Compute Cole Liau index
def indexColemanLiau():
    index = 0.0588 * (lettersCount() / wordsCount() * 100) - 0.296 * (sentencesCount() / wordsCount() * 100) - 15.8
    return index