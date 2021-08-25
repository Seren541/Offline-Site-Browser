class Download:

    def __init__(self, domain, path):
        self.domain = domain
        self.path = path
    
    def scrape(self):
        from pywebcopy import save_webpage

        # Uses code I don't understand to download any webpage
        url = 'http://' + self.domain + '/index.html'
        download_folder = self.path

        kwargs = {'project_name': self.domain, 'zip_project_folder': False}
        save_webpage(url, download_folder, **kwargs)