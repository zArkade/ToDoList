import tkinter as tk
import datetime
from tkinter import messagebox
from tkinter import simpledialog
from gerenciadorTask import add_task, edit_task, list_tasks, mark_task_completed, remove_task, save_tasks, load_tasks, search_tasks, tasks

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.unsaved_changes = False

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.frame, width = 40)
        self.task_entry.pack( side = tk.LEFT, padx = (0,10))

        self.due_date_entry = tk.Entry(self.frame, width=15)
        self.due_date_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.due_date_entry.bind("<KeyRelease>", self.validate_date_input)

        self.add_button = tk.Button(self.frame, text = "Adicionar uma Tarefa", command = self.add_task)
        self.add_button.pack( side = tk.LEFT)

        self.task_listbox = tk.Listbox( root, width = 50, height = 15)
        self.task_listbox.pack( padx = 10, pady = (10, 0))

        self.mark_button = tk.Button(root, text = "Marcar como concluída", command = self.mark_task)
        self.mark_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.remove_button = tk.Button(root, text = "Remover Tarefa", command = self.remove_task)
        self.remove_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.save_button = tk.Button(root, text = "Salvar Tarefas", command = save_tasks)
        self.save_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.load_button = tk.Button(root, text = "Carregar Tarefas", command = self.load_tasks)
        self.load_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.edit_button = tk.Button(root, text="Editar Tarefa", command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=10, pady=(10, 10))

        self.search_entry = tk.Entry(root, width=40)
        self.search_entry.pack(padx=10, pady=(10, 0))

        self.search_button = tk.Button(root, text="Pesquisar", command=self.search_task)
        self.search_button.pack(padx=10, pady=(0, 10))

        self.filter_var = tk.StringVar(value="Todas")

        self.filter_menu = tk.OptionMenu(root, self.filter_var, "Todas", "Concluídas", "Pendentes", command=self.filter_tasks)
        self.filter_menu.pack(padx=10, pady=(10, 10))

        self.load_tasks()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.search_task()

    def validate_date_input(self, event):
        input_text = self.due_date_entry.get()
        if not all(c.isdigit() or c in "/-" for c in input_text):
            self.due_date_entry.delete(len(input_text) - 1, tk.END)

    def add_task(self):
        description = self.task_entry.get()
        due_date = self.due_date_entry.get()
        if description:
            if due_date:
                try:
                    due_date_obj = datetime.datetime.strptime(due_date, "%d/%m/%Y")
                    if due_date_obj.date() <= datetime.date.today():
                        messagebox.showwarning("Data Inválida", "A data deve ser posterior ao dia de hoje.")
                        return
                except ValueError:
                    messagebox.showwarning("Formato de Data Inválido", "Por favor, insira uma data válida no formato DD/MM/AAAA.")
                    return

            add_task(description, due_date)
            self.unsaved_changes = True
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.update_task_list()

    def mark_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            mark_task_completed(task_index)
            self.unsaved_changes = True
            self.update_task_list()
            self.search_task()
        except IndexError:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione uma tarefa para marcar como concluída.")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            remove_task(task_index)
            self.unsaved_changes = True
            self.update_task_list()
            self.search_task()
        except IndexError:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione uma tarefa para remover.")

    def edit_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            new_description = simpledialog.askstring("Editar Tarefa", "Nova descrição da tarefa:")
            if new_description:
                self.unsaved_changes = True
                edit_task(task_index, new_description)
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione uma tarefa para editar.")
        self.search_task()
    
    def load_tasks(self):
        load_tasks()
        self.unsaved_changes = False
        self.update_task_list()
        self.search_task()

    def save_tasks(self):
        load_tasks()
        self.unsaved_changes = False
        messagebox.showinfo("Salvar tarefas", "Tarefas salvas com sucesso")

    def update_task_list(self):
        # print("Atualizando lista de tarefas...")  
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "Concluída" if task["completed"] else "Pendente"
            if "due_date" in task:
                self.task_listbox.insert(tk.END, f"{task['description']} [{status}] - Prazo: {task['due_date']}")
            else:
                self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")
        # print("Lista de tarefas atualizada:", tasks)

    def search_task(self):
        query = self.search_entry.get()
        results = search_tasks(query)
        self.task_listbox.delete(0, tk.END)
        for task in results:
            status = "Concluída" if task["completed"] else "Pendente"
            if "due_date" in task:
                self.task_listbox.insert(tk.END, f"{task['description']} [{status}] - Prazo: {task['due_date']}")
            else:
                self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

    def filter_tasks(self, selection):
        if selection == "Concluídas":
            filtered_tasks = [task for task in tasks if task["completed"]]
        elif selection == "Pendentes":
            filtered_tasks = [task for task in tasks if not task["completed"]]
        else:
            filtered_tasks = tasks

        self.task_listbox.delete(0, tk.END)
        for task in filtered_tasks:
            status = "Concluída" if task["completed"] else "Pendente"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

        self.search_task()

    def on_closing(self):
        if self.unsaved_changes:
            if messagebox.askyesno("Sair", "Você tem tarefas não salvas. Deseja salvar antes de sair?"):
                self.save_tasks()
            else:
                if messagebox.askyesno("Sair", "Tem certeza de que deseja sair sem salvar?"):
                    self.root.destroy()
        else:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()