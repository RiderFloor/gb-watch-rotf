from GuiBot.Routines import Routine
from GuiBot.Browser import Browser
from DataBase.Face import DataBase

from utilities.all_imports import *
from utilities.helpers import *




class Cerebro(Browser):
    def __init__(self):
        self.browser = Browser()
        
        print_log("Cerebro initiated")
        self.job = self.get_job()
        self.routine = self.load_routine()
        self.run()

    def run(self):
        self.browser._set_up(self.job['site'])
        self.routine(browser=self.browser, job=self.job)

    def get_job(self):
        print_log('Cerebro.get_job')
        job = {
            'site': 'streamzz',
            'task': 'watch',
            'params': self.__get_sequence()
        }
        return job

    def __get_sequence(self):
        all_ids = []
        for i in range(55, 85):
            all_ids.append(str(i))

#        l = len(all_ids[:-60])
 #       x = random.choice(range(1, l))
        return all_ids

    def load_routine(self):
        res = Routine()
        return res.load(self.job)








class Cerebro1(Routine):
    def __init__(self):
        self.bot_id = '#0001'
        self.db = DataBase()

        table = self.db.tables['VideosToWatch']
        self.all_vids = self.db.read_table(table)

        for i in range(len(self.all_vids)):
            self.__setup_bot()
            self.run()

    def run(self):
        if self.routine(self.job):
            vid = self.job['task']['vid_to_watch']
            self.db.mark_video_watched(vid)

    def __setup_bot(self):
        print_log(f'Cerebro.__setup_bot')

        # self.job = self.__get_new_vids()
        vid = self.__get_new_vid()

        job = {
            'site': 'watch',
            'task': 'video',
            'vid_to_watch': vid,
        }
        self.job = {
            'task': job
        }
        if self.job['task']['vid_to_watch']:
            self.routine = self._load_routine(self.job)

    def __get_new_vid(self):
        print_log('Cerebro.__get_new_vids')
        table = self.db.tables['VideosToWatch']
        all_vids = self.db.read_table(table)
        li = []
        for vid in all_vids:
            if not vid['watched'] == 'true':
                li.append(int(vid['id']))

        if len(li) > 0:
            return min(li)
        else:
            print_log('Cerebro.__get_job - no jobs found', level='ALERT')
