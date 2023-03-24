#!/usr/bin/python3

import cmd, sys

class AirBnB(cmd.Cmd):
    '''console execution'''
    intro = 'welcome to the AirBnB console make by Coulby and Akinla. \n'
    prompt = '(AirBnB)'
    
    '''Methods to close console'''
    def do_exit(self, arg):
        'Stop recording, close the AirBnB console, and exit:  EXIT '
        print('Thank you for using AirBnB console make by Coulby and Akinla')
        self.close()
        exit()
        return True
if __name__ == '__main__':
    AirBnB().cmdloop()
