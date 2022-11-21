from Cerebro import Cerebro
from utilities.all_imports import *
from utilities.helpers import *
import time
from threading import Thread


def star():
    bot = Cerebro()
    return True


def keep_alive():
    t = Thread(target=star)
    t.start()