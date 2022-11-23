from GuiBot.Routines import Routine
from GuiBot.Browser import Browser
from DataBase.Face import DataBase

from utilities.all_imports import *
from utilities.helpers import *



class Cerebro:
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
            'params': self.__get_sequence()}
        return job

    def __get_sequence(self):
        all_ids = []
        for i in range(1, 85):
            all_ids.append(str(i))

        l = len(all_ids[:-10])
        x = random.choice(range(0, l))
        return all_ids[x:]

    def load_routine(self):
        res = Routine()
        return res.load(self.job)
