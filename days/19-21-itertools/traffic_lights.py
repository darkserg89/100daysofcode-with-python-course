


import termcolor
import sys
import os
import itertools
import time

template = '''
    #####
    #####
    #####
    '''

class Colors:
    
    def __init__(self,color,seconds=2):
        self.color=color
        self.seconds = seconds
        
        
    def light(self):
        print(termcolor.colored(template,self.color))
        time.sleep(int(self.seconds))
        os.system('clear')
        

def main():
    colors = [Colors('red',5),Colors('yellow'),Colors('green',10),Colors('yellow')]
    traffic_light = itertools.cycle(colors)
    for i in traffic_light:
        i.light()


if __name__ == '__main__':
    main()
