def LineList(F):
    file = open(F, "r")
    x = file.readlines()
#   x is a list of the strings of each line
    L = []
    
    for string in x:
#   for one of the strings in the list of strings x
        string = string.replace("\n", "")
#       because I used the file.readlines() function, it adds "\n" for the new paragraphs so I have to remove it
        string = string.lower()
        n = string.split()
#       this stores each word in the original strings as strings in n
        m = []
#       I am creating a new list within the first for loop to store the new words in the upcoming for loop

        for string1 in n:
#       for one of the words in the nested list of a string n
            string2 = string1.strip("1234567890!%&\"()'?;-,.:][}{")
            if string2.isalpha() == True:
                m.append(string2)
#               I add the stripped word to m if it is all alphabetical

        L.append(m)
#       I add the list of words in one of the lines to L and loop that again for the other lines

    file.close()
    return L

def SentenceCount(F):
    file = open(F, "r")
    x = file.readlines()
    count = 0
#   start the count at 0

    for string in x:
        string = string.replace("Mr.", "")
        string = string.replace("Mrs.", "")
        string = string.replace("Ms.", "")
        string = string.replace("Dr.", "")
        string = string.replace("\"", "")
        '''replacing all of these with an empty string just erases it,
        and I erased the quotation marks because in some instances,
        the quotation marks come after the period,
        but still finishes the sentences!'''
        n = string.split()
        
        for string1 in n:
            if "..." in string1:
#           I prioritized the "..." because if it counted each period, then there would be 2 extra sentences
                count += 1
            elif "." in string1:
                count += string1.count(".")
                '''in the case of the text file with the string "G.I.",
                we wanted to count both of those periods as sentences,
                but since they are in the same string,
                we had to count the number of periods there were in each string'''
            elif "!" in string1 or "?" in string1:
#           finally, the only other two punctuation marks that can end a sentence are these two
                count += 1
                
    file.close()
    return count

def WordDict(F):
    z = LineList(F)
#   I called the LineList() function because the restriction for words are the same in WordDict()
    L2 = []
#   I created a new list so that we can remove the nests in the LineList() function
    dictionary = {}
    
    for string in z:
        for words in string:
            L2.append(words)
            '''it takes the word string in from the LineList function
            and moves each individual word into the big list of L2
            while ignoring the nested list that it was originally in'''
            
    for word in L2:
        if word not in dictionary.keys():
            dictionary[word] = 1
#           since the word wouldn't be originally in the dictionary, you just start the count at 1...
        else:
            dictionary[word] += 1
#           then add more here when you find the same word

    return dictionary

def SentimentCount(D):
    file1 = open("negativesentimentwords.txt", "r")
    x = file1.readlines()
    a = []
    
    file2 = open("positivesentimentwords.txt", "r")
    y = file2.readlines()
    b = []

    file3 = open("ignorewords.txt", "r")
    z = file3.readlines()
    c = []
    
#   I opened all the files and created a new list under each where I will fill those empty lists with the words in the files removing "\n"
    
    Negative = 0
    Positive = 0
    Neutral = 0
    
    for string in x:
        newstring = string.replace("\n", "")
        a.append(newstring)
        
    for string in y:
        newstring = string.replace("\n", "")
        b.append(newstring)
        
    for string in z:
        newstring = string.replace("\n", "")
        c.append(newstring)
       
#       the new strings from x, y, and z without "\n" got appended to a, b, and c respectively
        
    for keys in D.keys():
        if keys in a:
            Negative += D[keys]
        elif keys in b:
            Positive += D[keys]
        elif keys not in c:
            Neutral += D[keys]
    '''this for loop basically took the values of the keys that were present in the given text files for this function
    and added them to "Negative", "Positive", and "Neutral"'''
            
    Total = Negative + Positive + Neutral
    
    Negative1 = round(Negative / Total * 100)
    Positive1 = round(Positive / Total * 100)
    Neutral1 = round(Neutral / Total * 100)
    
    file = open("Results.txt", "w")
    file.write("Positive Sentiment Word Count: " + str(Positive) + " (" + str(Positive1) + "%)\n")
    file.write("Negative Sentiment Word Count: " + str(Negative) + " (" + str(Negative1) + "%)\n")
    file.write("Neutral Sentiment Word Count: " + str(Neutral) + " (" + str(Neutral1) + "%)\n")
    '''opened a new file with the name given to write a concatenation of the given text
    while concatenating the integers from the above variables before this new file was written
    making them strings because you cannot concatenate integers'''

    if Positive1 > Negative1:
        file.write("This document has a positive sentiment")
    elif Negative1 > Positive1:
        file.write("This document has a negative sentiment")
    elif Negative1 == Positive1:
        file.write("This document has a neutral sentiment")
#   this is just the if statements of what the output will be depending on the inequalities
    
    file1.close()
    file2.close()
    file3.close()
    file.close()
#   the closing for all the files after they have all been used
    
    return None
#   since we were not asked to return anything, we just finalize the script by returning nothing