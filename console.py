#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd, sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    '''console execution'''
   # intro = 'welcome to the AirBnB console make by Coulby and Akinla. \n'
    prompt = '(hbnb)'
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }
    
    '''Methods to close console'''
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argC = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argC[1])
            if match is not None:
                command = [argC[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argC[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        argC = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argC[0] == obj.__class__.__name__:
                count += 1
            print(count)


    def do_create(self, arg):
        """create a new instance of BaseModel,saves it to the Json file and prints the id"""
        argC = parse(arg)
        if len(argC) == 0:
            print("** class name missing **")
        elif argC[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argC[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name id"""
        argC = parse(arg)
        objdict = storage.all()
        if len(argC) == 0:
            print("** class name missing **")
        elif argC[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argC) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argC[0], argC[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argC[0], argC[1])])

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id (save the change into the JSON file"""
        argC = parse(arg)
        objdict = storage.all()
        if len(argC) == 0:
            print("** class name missing **")
        elif argC[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argC) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argC[0], argC[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argC[0], argC[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        argC = parse(arg)
        if len(argC) > 0 and argC[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objC = []
            for obj in storage.all().values():
                if len(argC)  and argC[0] == obj.__class__.__name__:
                    objC.append(obj.__str__())
                elif len(argC) == 0:
                    objC.append(obj.__str__())
            print(objC)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute(save the change into JSON file"""
        argC = parse(arg)
        objdict = storage.all()

        if len(argC) == 0:
            print("** class name missing **")
            return False
        if argC[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argC) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argC[0], argC[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argC) == 2:
            print("** attribute name missing **")
            return False
        if len(argC) == 3:
            try:
                type(eval(argC[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argC) == 4:
            obj = objdict["{}.{}".format(argC[0], argC[1])]
            if argC[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argC[2]])
                obj.__dict__[argC[2]] = valtype(argC[3])
            else:
                obj.__dict__[argC[2]] = argC[3]
        elif type(eval(argC[2])) == dict:
            obj = objdict["{}.{}".format(argC[0], argC[1])]
            for k, v in eval(argC[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
