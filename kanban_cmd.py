#!/usr/bin/env python
"""
Kanban is an interactive command application.
Usage:
    Todo todo <taskname>
    Todo todo_list
    Todo doing <task_id>
    Todo done <task_id>
    Todo doing_list
    Todo done_list
    Todo list_all
    Todo sync_tasks
    Todo (-i | --interactive)
    Todo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from termcolor import colored
from pyfiglet import Figlet
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
    header = "  Design to help one to know task progress"
    main_menu = "main menu"
    main_option = "Menu Option 2"
    instruction = "Instructions:"
    todo_one = "Todo >> Input: task todo | view todo task list |"
    todo_two = "| move task from todo to doing | view doing task list"
    todo_three = "| move task from doing to done | view done task list"
    todo_four = "| View all task | sync database to firebase"
    todo_five = "Type help or -h for a list of commands"
    print(colored("  " + "~" * 89,"white"))
    print(colored("  " + Figlet(font='slant').renderText('\t      TODO TASK MANAGER'),"white"))
    print(" " * 93)
    print(" " * 93)
    print(colored("  ~" + "~" * 89 + "~","blue"))
    print(colored("  ~" + header.center(89, " ") + "~","white"))
    print(colored("  ~" + "~" * 89 + "~","blue"))
    print(colored("  ~" + instruction.ljust(89, " ") + "~","white"))
    print(colored("  ~" + "~" * 89 + "~","white"))
    print(colored("  ~" + main_menu.center(89, " ") + "~","green"))
    print(colored("  ~" + "~" * 89 + "~","white"))
    print(colored("  ~" + " " * 89 + "~","white"))
    print(colored("  ~" + todo_one.ljust(89, " ") + "~","white"))
    print(colored("  ~" + todo_two.center(89, " ") + "~","white"))
    print(colored("  ~" + todo_three.center(89, " ") + "~","white"))
    print(colored("  ~" + todo_four.center(89, " ") + "~","white"))
    print(colored("  ~" + " " * 89 + "~","white"))
    print(colored("  ~" + "~" * 89 + "~","white"))
    print(colored("  ~" + main_option.center(89, " ") + "~","green"))
    print(colored("  ~" + "~" * 89 + "~","white"))
    print(colored("  ~" + todo_five.center(89, " ") + "~","white"))
    print(colored("  ~" + "~" * 89 + "~","white"))
    print(" " * 93)
    print(" " * 93)
    
    prompt = "Todo >>"
    file = None

    @docopt_cmd
    def do_todo(self, arg):
        """Usage: todo <taskname>"""
        print(kanban.add_new_task(arg['<taskname>']))

    def do_todo_list(self, arg):
        """Usage: todo_list"""
        print(kanban.view_tasks_todo()) 

    def do_todo_doing(self, arg):
    	"""Usage: doing <task_id>"""
    	print(kanban.move_todo_task_to_doing(arg)) 
    	
    def do_doing_list(self, arg):
    	"""Usage: doing_list"""
    	print(kanban.view_tasks_doing())

    def do_doing_done(self, arg):
        """Usage: done <task_id>"""
        print(kanban.move_doing_task_to_done(arg))

    def do_done_list(self, arg):
        """Usage: done_list"""
        print(kanban.view_tasks_done())

    def do_list_all(self, arg):
        """Usage: list_all"""
        print(kanban.view_all_tasks())

    def do_sync_tasks(self,arg):
        """sync_tasks"""
        print(kanban.sync_tasks())         

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