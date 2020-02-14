import string
def mostCommonWord(paragraph, banned):
    """
        convert to lower
        remove punctuation
        create list of words
        count words
        find most common
        """
        
        # convert to lower
        newString = paragraph.lower()
        
        #remove punctutation
        for c in string.punctuation:
            newString = newString.replace(c, " ")
            
        
        word_dict = {}
        count = 0
        result = ""
        
        # create a list of words
        for word in newString.split():
            # bc we replaced punc with " ", we skip " "
            if word not in banned and word != " ":
                # keep track of count in dict
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
                    # most occured tracked by count and result
                if word_dict[word] > count:
                    count = word_dict[word]
                    result = word
        return result


        

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

mostCommonWord(paragraph, banned)