from typing import List

def log(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} has been called")
        return result 
    return wrapped
        

class Model:
    def __init__(self) -> None:
        self.tasks: List[str] = []
        
    @log        
    def add_a_task(self, new_task: str) -> str:
        new_task = new_task.strip()
        if not new_task:
            return "Enter a task"
        elif new_task in self.tasks:
            return "You already added that Task"
        else:
            self.tasks.append(new_task)
            return f"Added {new_task} to your To Do List"
    
    @log
    def edit_a_task(self, old_task: int, new_task: str) -> str:
        new_task = new_task.strip()
        if not new_task:
            return "Enter a proper task to edit"
        if old_task < 0 or old_task >= len(self.tasks):
            return "You don't have that many tasks in your To Do List"
        self.tasks[old_task] = new_task
        return f"Edited task to: {new_task}"
    
    @log    
    def delete_a_task(self, old_index: int) -> str:
        if old_index < 0 or old_index >= len(self.tasks):
            return "You don't have that many tasks in your To Do List"
        deleted_task = self.tasks.pop(old_index)
        return f"Deleted {deleted_task} from your To Do List"
    
    @log
    def check_tasks(self) -> bool:
        return len(self.tasks) > 0
    
class View:
    def __init__(self) -> None:
        pass
    
    def print_a_message(self, text: str) -> None:
        print(text)
        return
    
    def ask_a_user(self, text: str) -> str:
        asking = input(f"{text}: ")
        return asking
    
    def print_list_question(self) -> None:
        print("Do you want to see your To Do List?")
    
    def show_list(self, task_list: List[str]) -> None:
        if not task_list:
            print("The List is empty")
            return

        output = ""
        for index, task in enumerate(task_list, start=1):
            output += f"{index}. {task}\n"
        print(output)
        return
    
class Controller:
    def __init__(self) -> None:
        self.view = View()
        self.model = Model()
    
    def start_task_manager(self) -> None:
        print("Welcome to the Mini Task Manager!")
        
        while True:
            print("\nDo you want to\n"
                  "1. Add a Task\n"
                  "2. Edit a Task\n"
                  "3. Delete a Task\n"
                  "4. Show list of Tasks\n"
                  "5. Exit Task Manager\n")
            
            choose_action = input("Enter the Action you want to continue with as a number: ").strip()
            try:
                if choose_action == "1":
                    ask_for_task = input("Which Task do you want to add: ")
                    message = self.model.add_a_task(ask_for_task)
                    self.view.print_a_message(message)
                    self.view.print_list_question()
                    answer = input("Type yes/no: ").lower()
                    if answer == "yes":
                        self.view.show_list(self.model.tasks)
                    else:
                        continue
                    
                elif choose_action == "2":
                    if not self.model.check_tasks():
                        self.view.print_a_message("The List is empty")
                        continue

                    old_index = int(input("Enter the number of the task you want to edit: ").strip())
                    if old_index <= 0:
                        self.view.print_a_message("Enter a positive number")
                        continue
                    elif old_index > len(self.model.tasks):
                        self.view.print_a_message("You don't have that many tasks in your To Do List")
                        continue
                    
                    old = old_index - 1
                    new = input("What should the new Task be: ")
                    message = self.model.edit_a_task(old, new)
                    self.view.print_a_message(message)
                    
                    self.view.print_list_question()
                    answer = input("Type yes/no: ").lower()
                    if answer == "yes":
                        self.view.show_list(self.model.tasks)
                    else:
                        continue
                
                elif choose_action == "3":
                    if not self.model.check_tasks():
                        self.view.print_a_message("The List is empty")
                        continue

                    old_index = int(input("Enter the number of the task you want to delete: ").strip())
                    if old_index <= 0:
                        self.view.print_a_message("Enter a positive number")
                        continue
                    elif old_index > len(self.model.tasks):
                        self.view.print_a_message("You don't have that many tasks in your To Do List")
                        continue
                    
                    old = old_index - 1
                    message = self.model.delete_a_task(old)
                    self.view.print_a_message(message)
                    
                    self.view.print_list_question()
                    answer = input("Type yes/no: ").lower()
                    if answer == "yes":
                        self.view.show_list(self.model.tasks)
                    else:
                        continue
                    
                elif choose_action == "4":
                    self.view.show_list(self.model.tasks)
                    
                elif choose_action == "5":
                    break

                else:
                    self.view.print_a_message("Please choose a valid action (1-5)")
                    
            except ValueError:
                self.view.print_a_message("Enter it properly")
                continue
            
if __name__ == "__main__":
    c = Controller()
    c.start_task_manager()