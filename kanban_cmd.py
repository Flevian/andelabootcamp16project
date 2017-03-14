#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    kanban todo <taskname>
    kanban list_todo
    kanban doing <task_id>
    kanban done <task_id>
    kanban list_doing
    kanban list_done
    kanban list_all
    kanban (-i | --interactive)
    kanban (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from kanban import Kanban
kanban = Kanban()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class ToDo(cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'todo > '
    file = None

    @docopt_cmd
    def do_todo(self, arg):
        """Usage: todo <taskname>"""
        kanban.add_new_task(arg['<taskname>'])

    def do_todo_list(self, arg):
        """Usage: todo_list"""
        kanban.view_tasks_todo() 

    def do_todo_doing(self, arg):
    	"""Usage: todo_doing <task_id>"""
    	kanban.move_todo_task_to_doing(arg) 
    	
    def do_doing_list(self, arg):
    	"""Usage: doing_list"""
    	kanban.view_tasks_doing()

    def do_doing_done(self, arg):
        """Usage: done <task_id>"""
        kanban.move_doing_task_to_done(arg)

    def do_done_list(self, arg):
        """Usage: list_done"""
        kanban.view_tasks_done()

    def do_list_all(self, arg):
        """Usage: list_all"""
        kanban.view_all_tasks()     

    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ToDo().cmdloop()

print(opt)