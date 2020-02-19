def reorderLogFiles(logs):
    digits = []
    letters = []
    ans = []

    for string in logs:
        # split strings into seperate words
        newString = string.split()
        # categorize into digits or letter lists
        if newString[1].isalpha():
            # move the identifier to end of string for the letters so we can sort later
            letters.append(" ".join(newString[1:]) + " " + newString[0])
        else:
            # keep digits in original order. Just append them to digits list
            digits.append(" ".join(newString))
    
    # sort letter list alphabetically
    letters.sort()
    for l in letters:
        # split strings into word lists
        l = l.split()
        # move identifier to the front of the string and append to new list
        ans.append(" ".join((l[-1:] + l[:-1])))
    
    return ans + digits


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

reorderLogFiles(logs)