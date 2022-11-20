#from GuiBot.Browser import Browser
from utilities.all_imports import *
from utilities.helpers import *


class StreamZZ:
    def __init__(self, browser, job):
        print_log('StreamZZ initiated')
        self.browser = browser
        self.job = job
        #self.browser.open_site(self.job['site'])
        self.run_job()

    def run_job(self):
        links = []
        base = 'https://FlaskVideo.riderfloor.repl.co/video'

        for id in self.job['params']:
            link = f'{base}?id={id}'
            links.append(link)
        
        
        for link in links:
            self.browser.open(link)
            if self.browser.await_loading():

                if self.start_watching():
                    print_log(f'Watch.watch - is watching', level='MESS')
                    t = 8
                    print_log(f'Watch.watch - waiting {t}min: {dt.now()}', level='MESS')
                    wait(t*60)  # video length
                    print_log(f'Watch.watch - finished watching', level='MESS')

                    self.browser._take_snapshot(f'done-watching-{link[-3:]}')
                    self.browser.close_browser()

    def start_watching(self):
        self.target_window_id = self.browser.get_current_tab_id()
        while True:
            position = (328, 251)
            self.browser.click(position=position)
            wait(1)
            open_tabs = self.browser.get_open_tabs_id()
            print_log(f'Watch.start_watching - number of tabs open: {len(open_tabs)}', level='DEBUG')
            if len(open_tabs) > 1:
                self.browser.close_tabs(self.target_window_id, open_tabs)
                wait(1)
            elif len(open_tabs) == 1:
                return True
