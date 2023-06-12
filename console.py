#!/usr/bin/python3
"""Command interpreter module"""
import cmd
import uuid
import json
import shlex
import models
from models.review import Review
from models.place import Place
from models. user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                objects = models.storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                objects = models.storage.all()
                if key in objects:
                    objects.pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        objects = models.storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls_name = args[0]
                if cls_name in models.classes.keys():
                    filtered_objs = [str(obj) for obj in objects.values()
                                     if type(obj).__name__ == cls_name]
                    print(filtered_objs)
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                obj_id = args[1]
                key = "{}.{}".format(cls_name, obj_id)
                objects = models.storage.all()
                if key in objects:
                    obj = objects[key]
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        attr_name = args[2]
                        attr_value = args[3].strip('"')
                        if attr_name not in ["id", "created_at", "updated_at"]:
                            setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
                            obj.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def postloop(self):
        """Prints a new line after the command is executed"""
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
