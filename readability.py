from cs50 import get_string

# Get text to analize from user
givenText = get_string("Text: ")
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
            words += 1
    return words + 1


# Count sentences
def sentencesCount():
    sentences = 0
    for i in range(textLentgh):
        if (givenText[i] == "." or givenText[i] == "!" or givenText[i] == "?"):
            sentences += 1
    return sentences


# Call functions to pass to indexColemanLiau
letters = lettersCount()
words = wordsCount()
sentences = sentencesCount()

    
# Compute Cole Liau index
def indexColemanLiau():
    l = letters / words * 100
    s = sentences / words * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return index
    

# Display result refferenced to Grade
index = round(indexColemanLiau())
if indexColemanLiau() < 1:
    print("Before Grade 1")
elif indexColemanLiau() > 16:
    print("Grade 16+")
else:
    print("Grade " + str(index))