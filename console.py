#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    '''console execution'''
    intro = 'welcome to the AirBnB console make by Coulby and Akinla. \n'
    prompt = '(hbnb)'
    
    '''Methods to close console'''
    def do_exit(self, arg):
        'Stop recording, close the AirBnB console, and exit: quit '
        print('Thank you for using AirBnB console make by Coulby and Akinla')
        self.close()
        quit()
        return True
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
