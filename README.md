KanbanApp

KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task

Installation

$ git clone https://github.com/Flevian/bc-16-kanban.git
$ cd bc-16-kanban

Create and activate a virtual environment.

$ virtualenv kanban
$ source kanban/Scripts/activate

Install

$ pip install –r requirements.txt

Run the application with either of the two commands:

$ python kanban_cmd.py --interactive
$ python kanban_cmd.py -i

Commands:

add <taskname> e.g add Git
doing <task_id> e.g doing 2
done <task_id> e.g done 5
task <task_id> e.g task 4
todo_list
doing_list
done_list
list_all
