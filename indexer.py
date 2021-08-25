class Index:

    #Imports the file path
    def __init__(self, file_path):
        self.file_path = file_path

    #Indexes the document
    def indexDocument(self):
        # Get File
        with open(self.file_path, 'r') as file:
            website = file.read().replace('\n', ' ')

        # Get rid of all html commands
        dele = False
        for r in range(len(website)):
            if website[r] == '<':
                website = website[:r] + ' ' + website[r+1:]
                dele = True
            elif website[r] == '>':
                website = website[:r] + ' ' + website[r+1:]
                dele = False
            elif dele == True:
                website = website[:r] + ' ' + website[r+1:]

        # Purge random characters
        characters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 \''.split()
        blanks = ' ' * len(website)

        for i in range(len(website)):
            if website[i] in characters:
                blanks = blanks[:i] + website[i] + blanks[i+1:]

        # Finally breaking into individual words
        blanks = blanks.split()

        return blanks