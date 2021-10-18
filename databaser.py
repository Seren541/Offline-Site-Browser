class Data:

    # imports array and link to categorize data by
    def __init__(self, words, link, path):
        self.words = words
        self.link = link
        self.path = path

    # Checks if the website is already indexed. TODO: See if it would be faster if it only checked website names
    def add(self):

        #Imports database and turns it into an array
        with open('Websites.database', 'r') as file:
            db = file.read()
        db = db.split()

        # Checks for redundancy. TODO: update sites if already there
        if not self.link in db:
            # Adds the link to the end of the database
            with open('Websites.database', 'a') as file:
                file.write('\n')
                file.write(self.link)
                file.write(' ')
                file.write(self.path)
                for r in range(len(self.words)):
                    file.write(' ')
                    file.write(self.words[r])
                file.write(' ')
                file.close()




    # If all is good, adds the index to the database