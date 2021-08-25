class Send:
    
    def __init__(self, order):
        self.order = order

    def getPage(self):

        # Opens file
        with open('Database.dat', 'r') as file:
            links = file.read().replace('\n', ' %n ')
        # Makes into array
        links = links.split()

        results = []
        lineNum = 1
        # TODO: fix this up
        if len(self.order) >= 1:
            # Finds out number of lines
            for i in range(len(links)):
                if links[i] == '%n':
                    for r in range(len(self.order)):
                        if lineNum == self.order[r][0]:
                            results.append(links[i + 1])
                            # Control for common searches 
                            if len(results) >= 10:
                                break
                    # This goes after because arrays start at 0
                    lineNum += 1

        elif len(self.order) == 0:
            print('No results found')
        
        return results