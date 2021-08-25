# Program start
# More info in Read.md

print('Would you like to:')
print('1. Download a website')
print('2. Update current websites (at the moment skips previous sites)')
print('3. Access a website')

usage = input()

if usage == '1':
    # Import the downloader
    from downloader import Download

    # Import file tools
    import os
    import os.path

    # Gets the site directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + '\\Sites'

    # Gets the website
    domainName = input('What is the name of the site you want to scrape (only include the domain): ')
    d = Download(domainName, dir_path)
    d.scrape()

elif usage == '2':
    # Import file tools
    import os
    import os.path

    # Gets the directory of the files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + '\\Sites'

    # Import classes
    from indexer import Index
    from databaser import Data

    # TODO: Import link and file
    link = "test.com"

    # Looks for all html files
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".html")]:
            dirpath = dirpath[1:]
            slash = 0
            for l in range(len(dirpath)):
                if dirpath[l] == '\\':
                    slash +=1
                if slash >= 2:
                    break
            dirpath = dirpath[l:]
            properPath = dir_path + dirpath + '\\' + filename
            print(properPath)
            i = Index(properPath)
            words = i.indexDocument()
            d = Data(words, dirpath, properPath)
            d.add()

elif usage == '3':
    # Imports all my classes
    from retriever import Get
    from sender import Send
    from browser import Display

    # What keywords to search for
    keywords = input('What would you like to search: ')
    find = Get(keywords)
    line = find.search()

    # Searches for what line(s) the keywords appear on
    s = Send(line)
    output = s.getPage()

    if len(output) > 0:
        # Prints outputted links
        for r in range (len(output)):
            print(output[r])

        # This part gets the website in question to show on screen
        num = '1 2 3 4 5 6 7 8 9 10'.split()
        site = input('Type link or number to get html (1 = first link, 2 = second, etc): ')

        if site in num:
            show = Display(output[(int(site))-1])
            show.run()
        else:
            show = Display(site)
            show.run()
input('Press enter to escape.')