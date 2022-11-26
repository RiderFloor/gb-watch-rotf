from Builder import ScriptBuilder

from threading import Thread
from pprint import pprint
import time


def run_cerebro(mess):
    from GbCerebro import Cerebro
    pprint('# INFO: app.py: starting cerebro')
    bot = Cerebro(mess)
    bot.run()

def build(mess):
    pprint('# INFO: app.py: building scripts')
    builder = ScriptBuilder()
    builder.build(mess['scripts'])
    run_cerebro(mess)

