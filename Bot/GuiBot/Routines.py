"""
will import all routines:
                - manyvids post free/vip
                - twitter
                - sharesome
                - etc

"""
from GuiBot.routines import watch_video
from utilities.helpers import *
from utilities.all_imports import *


class Routine:
    def load(self, job):
        self.site = job['site']
        self.task = job['task']

        commands = {
            'streamzz_watch': watch_video.StreamZZ}

        print_log(f'Routine.load_routine - routine loaded: {self.site} {self.task}')
        return commands[f"{self.site}_{self.task}"]


