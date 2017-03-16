from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from kanbanDb import Kanban, Base 

class KanbanMain(object):
	"""docstring for KanbanMain"""
	def __init__(self):
		engine = create_engine('sqlite:///kanban.db')
		Base.metadata.bind = engine # Bind the engine to the metadata of the Base class in order declaratives to be accessedvia DBSessionInstance
		DBSession = sessionmaker(bind=engine) # Establishes con with the database
		session = DBSession()
	
	def add_new_task(self):
		"""Insert a Task ToDo in the kanban table"""	
		print("==========New task to Todo=======")
		new_task = input("Add new task Todo? ")
		new_task = Kanban(task_name = new_task)
		session.add(new_task)
		session.commit()

	def view_tasks_todo(self):
		"""View a list of all ToDo tasks"""
		print("==========Todo tasks list=======")
		todo_tasks= session.query (Kanban).all()
		for task in todo_tasks:
			print (str(task.id) + "\t" + task.task_name)

    def move_todo_task_to_doing(self):
        print ("====== Kindly select task you are doing to add it to Doing list =========")
		todo_tasks= session.query (Kanban).all()
        for  task in todo_tasks:
        	print (str(task.id) + "\t" + task.task_name )
        task_id = input("Task Id: ")
        for  task in todo_tasks:
        	if task.id is task_id:
        		#
        		Update database
        		#
        		self.status = "NOT_DONE"
        	else:
        		print("Task id entere does not exist")	

	def view_tasks_doing(self):
		"""View a list of all Doing tasks"""
		print("==========Doing tasks list=======")
		doing_tasks= session.query (Kanban).all()
		for task in doing_tasks:
			task.completion_time = current_time - task.completion_time
			print (str(task.id) + "\t" + task.task_name + "\t" + task.completion_time)

    def move_doing_task_to_done(self):
        print ("====== Kindly select task you have finished to add it to Done list =========")
		doing_tasks= session.query (Kanban).all()
        for  task in doing_tasks:
        	print (str(task.id) + "\t" + task.task_name )
        task_id = input("Task Id: ")
        for  task in doing_tasks:
        	if self.task.id is task_id:
        		#
        		Update database
        		#
        		self.status = "DONE"
        	else:
        		print("Task id entere does not exist")
	def view_tasks_done(self):
		"""View a list of all Done tasks"""
		print("==========Done tasks list=======")
		done_tasks= session.query (Kanban).all()
		for task in done_tasks:
			task.completion_time = current_time - task.completion_time
			print (str(task.id) + "\t" + task.task_name + "\t" + task.completion_time)

	def view_all_tasks(self):
		"""View a list of all Doing tasks"""
		print("==========All tasks======\n\n")
		print("==========Not started tasks======\n")
		self.view_tasks_todo()
		print("\n==========Pending tasks======\n")
		self.view_tasks_doing()
		print("\n==========finished tasks======\n")
		self.view_tasks_done()		
