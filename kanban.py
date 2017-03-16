from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker 
from kanbanDb import KanbanDb, Base
from tabulate import tabulate 
from datetime import datetime
#from firebase import firebase
import json

class Kanban():
    """KanBan is a console application that is used to manage to-do tasks using the KanBan way of organizing todo into 3 sections: todo, doing, done. The app also tracks the time taken on a particular task and displays each task in the doing and done section with the time-taken so far on the task."""

    def __init__(self):
        engine = create_engine('sqlite:///kanban.db')
        Base.metadata.bind = engine # Bind the engine to the metadata of the Base class in order declaratives to be accessedvia DBSessionInstance
        DBSession = sessionmaker(bind=engine) # Establishes connection with the database
        self.session = DBSession()
    
    def add_new_task(self, taskName):
        """Insert a Task ToDo in the kanban table"""    
        new_task = KanbanDb()
        new_task.task_name = taskName
        new_task.task_status = "TODO"
        new_task.start_time = None
        new_task.task_duration = None 
        self.session.add(new_task)
        try:
            self.session.commit()
            return "Task added"
        except:
            self.session.rollback()
            return "Task not added"

    def view_tasks_todo(self):
        """View a list of all ToDo tasks"""
        todo_str = "Todo tasks list"
        print(todo_str.center(29, "*"))
        todo_tasks = self.session.query(KanbanDb).filter(KanbanDb.task_status == "TODO")
        if todo_tasks.all():
            todo_list = []
            for task in todo_tasks:
                todo_list.append([task.id, task.task_name])
            return(tabulate(todo_list, ["Task Id", "Task Description"], "fancy_grid"))
        else:
            return "No todo task"        

    def move_todo_task_to_doing(self, task_id ):
        """Changing the status of todo task to doing"""
        todo_doing_task = self.session.query(KanbanDb).filter(KanbanDb.task_status == "TODO")
        if todo_doing_task.all():
            for task in todo_doing_task:
                start_time = datetime.now()
                todo_doing = self.session.query(KanbanDb).filter(KanbanDb.id == task_id).filter(KanbanDb.task_status == "TODO")
                if todo_doing.all():
                    todo_doing.update({"task_status": "DOING", "start_time": start_time})
                    try:
                        self.session.commit()
                        return "Task moved from doing to done"
                    except:
                        self.session.rollback()
                        return "Task moved"
                else:
                    return "Task id provided is not for a todo task"
        else:
            return "Task id provided does not exist"                        

    def view_tasks_doing(self):
        """View a list of all Doing tasks"""
        doing_str = "Doing tasks list"
        print(doing_str.center(29, "*"))
        doing_tasks = self.session.query(KanbanDb).filter(KanbanDb.task_status == "DOING")
        if doing_tasks.all():
            doing_task_list = []
            for task in doing_tasks: 
                doing_task_time_taken = datetime.now()  - task.start_time
                doing_task_list.append([task.id, task.task_name, doing_task_time_taken])
            return(tabulate(doing_task_list, ["Task Id", "Task Description", "Task Duration"], "fancy_grid"))
        else:
            return "No doing task"

    def move_doing_task_to_done(self, task_id):
        """Changing the status of doing task to done"""  
        doing_task = self.session.query(KanbanDb).filter(KanbanDb.task_status == "DOING")
        if doing_task.all():
            for task in doing_task:
                finish_time = str(datetime.now() - task.start_time)
                doing_done = self.session.query(KanbanDb).filter(KanbanDb.id == task_id).filter(KanbanDb.task_status == "DOING")
                if doing_done.all():
                    doing_done.update({"task_status": "DONE", "task_duration": finish_time })
                    try:
                        self.session.commit()
                        return "Task moved from doing to done"
                    except:
                        self.session.rollback()
                        return "Task not moved"
                else:
                    return "Task id provided is not for a doing task"
        else:
            return "Task id provided does not exist"                        

    def view_tasks_done(self):
        """View a list of all Done tasks"""
        done_str = "Done tasks list"
        print(done_str.center(29, "*"))
        done_tasks = self.session.query(KanbanDb).filter(KanbanDb.task_status == "DONE") # Get a object of all done tasks
        if done_tasks.all():
            done_task_list = []
            for task in done_tasks:
                done_task_list.append([task.id, task.task_name, task.task_duration])
            return(tabulate(done_task_list, ["Task Id", "Task Description", "Task Duration"], "fancy_grid"))
        else:        
            return "No done task"

    def view_all_tasks(self):
        """View a list of all Doing tasks"""
        """View a list of all Done tasks"""
        done_str = "All tasks"
        print(done_str.center(29, "*"))
        todo_list2= []
        doing_list = []
        done_list =[]
        all_task_dict ={}
        done_task = self.session.query(KanbanDb).all()
        if len(done_task)  != 0:
            for task in done_task:
                if task.task_status == "TODO":
                    todo_list2.append(task.task_name)
                elif task.task_status == "DOING":
                    doing_list.append(task.task_name)
                else:
                    done_list.append(task.task_name)
            all_task_dict = {"TODO" : todo_list2, "DOING" :  doing_list, "DONE" : done_list}
            return(tabulate(all_task_dict, headers = "keys", tablefmt = "fancy_grid"))
        else:
            return "No tasks available"       

    # def sync_tasks(self):
    #     task_backup = self.session.query(KanbanDb).all()
    #     firebase = firebase.firebaseApplication("https://kanban-andela.firebaseio.com/")
    #     upload_tasks = firebase.post(json.dumps(task_backup))
    #     return "tasks synced successifully"    

    def main():
        pass      

if __name__ == '__main__':main()