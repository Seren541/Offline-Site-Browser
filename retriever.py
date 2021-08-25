class Get:

    # Imports keywords
    def __init__(self, keywords):
        self.keywords = keywords.split()

    # Scans database for words
    def search(self):

        # Reads file
        with open('Database.dat', 'r') as file:
            base = file.read().replace('\n', ' %n ')
            base = base.split()

        linenum = []
        linecount = 0

        # I have to classify linescore for the first if. Not sure about templist tho, might be redundant
        linescore = 0
        templist = []
        # Cycles through lines
        for r in range(len(base)):
            # Cycles individual lines for words

            if base[r] != '%n':
                # Checks for the keywords in the file and if it finds them it adds 1. Duplicates are added, so be careful for spam.
                for l in range(len(self.keywords)):
                    if self.keywords[l] == base[r]:
                        linescore += 1
            else:
                # Adds the line number, score, and finally adds this array to the main one. Only adds if its a true result
                if (linescore > 0):
                    templist.append(linecount)
                    templist.append(linescore)
                    linenum.append(templist)

                linecount += 1
                templist = []
                linescore = 0
        
        # TODO: Make this for function look prettier. Shouldn't have to have this here twice, just need to trick it.
        if (linescore > 0):
            templist.append(linecount)
            templist.append(linescore)
            linenum.append(templist)

        # Sorts the search results based on the number of results using an algorithm I won't pretend to understand
        linenum.sort(key=lambda x:x[1],reverse=True)
        
        # Now that our linescores have been "compressed", we can sort them, and they will only sort by their int because the decimal is too small to 
        

        return linenum