#gets the number of words in a given text
def get_text_numwords(text):
    wordcount = 0
    text = text.split()
    for i in text:
        wordcount += 1
    return wordcount

#gets the number of characters in a given text as a dictionary of ints
def get_text_numchars(text):
    chardict = {}
    for char in text:
        lowerchar = char.lower()
        if lowerchar in chardict:
            chardict[lowerchar] += 1
        else:
            chardict[lowerchar] = 1
    
    return chardict


#sorts a dictionary of ints from highest value to lowest value
def sort_chardict(dict):
    dictlist = []
    for key in dict:
        tempdict = {}
        tempdict["char"] = key
        tempdict["count"] = dict[key]
        dictlist.append(tempdict)
    dictlist.sort(reverse=True, key=lambda d: d["count"])
    
    return dictlist


