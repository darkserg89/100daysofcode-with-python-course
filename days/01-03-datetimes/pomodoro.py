# -*- coding: utf-8 -*-




import datetime
from time import sleep
import os

def timer(time=25):
    now = datetime.datetime.now()
    after = now + datetime.timedelta(minutes = time)
    while datetime.datetime.now() < after:
        sleep(1)
        os.system('clear')
        now = datetime.datetime.now()
        delta = after - now
        minutes = delta.seconds//60
        seconds = delta.seconds%60
        timer_mod = ' <------Live time: {} ------ time left {}:{} ------>'.format(now.strftime('%H:%M:%S'),minutes,seconds)
        print(timer_mod)
    print(finished_motd)
        
        
if __name__ == '__main__':
    timer(time = 1)
