from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker 
from kanbanDb import KanbanDb, Base
from tabulate import tabulate 
from datetime import datetime

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
        self.session.commit()

    def view_tasks_todo(self):
        """View a list of all ToDo tasks"""
        print("==========Todo tasks list=======")
        todo_tasks = self.session.query(KanbanDb).filter(KanbanDb.task_status == "TODO")
        for task in todo_tasks:
            print (str(task.id) + "\t" + task.task_name )

    def move_todo_task_to_doing(self, task_id ):
        """Changing the status of todo task to doing"""
        start_time = datetime.now()
        self.session.query(KanbanDb).filter(KanbanDb.id == task_id).filter(KanbanDb.task_status == "TODO").update({"task_status": "DOING", "start_time": start_time})
        self.session.commit() 

    def view_tasks_doing(self):
        """View a list of all Doing tasks"""
        print("==========Doing tasks list=======")
        doing_tasks= self.session.query(KanbanDb).filter(KanbanDb.task_status == "DOING")
        for task in doing_tasks:
            doing_task_time_taken = datetime.now()  - task.start_time
            print (str(task.id) + "\t" + task.task_name + "\t" + str(doing_task_time_taken))

    def move_doing_task_to_done(self, task_id):
        """Changing the status of doing task to done"""  
        done_task = self.session.query(KanbanDb).filter(KanbanDb.id == task_id).filter(KanbanDb.task_status == "DOING")
        for task in done_task:
            finish_time = str(datetime.now() - task.start_time)
            self.session.query(KanbanDb).filter(KanbanDb.id == task_id).filter(KanbanDb.task_status == "DOING").update({"task_status": "DONE", "task_duration": finish_time })
            self.session.commit()                        

    def view_tasks_done(self):
        """View a list of all Done tasks"""
        print("==========Done tasks list=======")
        done_tasks = self.session.query (KanbanDb).filter(KanbanDb.task_status == "DONE") # Get a list of all done tasks
        for task in done_tasks:
            print (str(task.id) + "\t" + task.task_name + "\t" + task.task_duration)

    def view_all_tasks(self):
        """View a list of all Doing tasks"""
        print("==========All tasks======")
        self.view_tasks_todo()
        self.view_tasks_doing()
        self.view_tasks_done()

def main():
    pass      

if __name__ == '__main__':main()