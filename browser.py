class Display:

    def __init__(self, site):
        self.site = site

    def run(self):
        with open('Database.dat', 'r') as file:
            data = file.read()
        data = data.split()

        # If python has a function to search for the file, surely I can also get the position from that, right? TODO: Get this position to reduce cpu usage.
        if self.site in data:
            for r in range(len(data)):
                if data[r] == self.site:
                    path = data[r+1]

        # Formats C:\ to file:///

        for l in range(len(path)):
            if path[l] == '\\':
                path = path[:l] + '/' + path[l+1:]

        # Uses code I don't understand to open the file in Chrome
        import webbrowser
        new = 2

        url = "file:///" + path
        webbrowser.open(url,new=new)