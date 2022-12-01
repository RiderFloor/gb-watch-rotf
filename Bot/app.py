from Builder import ScriptBuilder

from threading import Thread
from pprint import pprint
import time


def run_cerebro(mess):
    from GbCerebro import Cerebro
    pprint('# INFO: app.py: starting cerebro')
    bot = Cerebro(mess)
    bot.run()

def build():
    instructions = {
        'site': 'pornhub',
        'task': 'watch',
        'params': 'https://www.pornhub.com/view_video.php?viewkey=ph5e403f2f0eddc',
        'scripts': {
            'DataBase': ['Face', 'SupaBase', 'Publitio'],
            'utilities': ['all_imports', 'config', 'helpers'],
            'GuiBot': ['Browser', 'Pornhub', 'Streamzz', 'Routines'],
            'main': ['GbCerebro']
        }
    }
    
    pprint('# INFO: app.py: building scripts')
    builder = ScriptBuilder()
    builder.build(instructions['scripts'])
    run_cerebro(instructions)

def keep_alive():
    print('staring thread')

    t = Thread(target=build)
    t.start()
    print('thread started')
