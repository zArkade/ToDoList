import tkinter as tk
from tkinter import messagebox
from gerenciadorTask import add_task, list_tasks, mark_task_completed, remove_task, save_tasks, load_tasks, tasks

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.frame, width = 40)
        self.task_entry.pack( side = tk.LEFT, padx = (0,10))

        self.add_button = tk.Button(self.frame, text = "Adicionar uma Tarefa", command = self.add_task)
        self.add_button.pack( side = tk.LEFT)

        self.task_listbox = tk.Listbox( root, width = 50, height = 15)
        self.task_listbox.pack( padx = 10, pady = (10, 0))

        self.mark_button = tk.Button(root, text = "Marcar como concluída", command = self.mark_task)
        self.mark_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.save_button = tk.Button(root, text="Salvar Tarefas", command=save_tasks)
        self.save_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.load_button = tk.Button(root, text="Carregar Tarefas", command=self.load_tasks)
        self.load_button.pack( side = tk.LEFT, padx = 10, pady = (10, 10))

        self.load_tasks()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            add_task(description)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()

    def mark_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            mark_task_completed(task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione uma tarefa para marcar como concluída.")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            remove_task(task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione uma tarefa para remover.")

    def load_tasks(self):
        load_tasks()
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "Concluída" if task["completed"] else "Pendente"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()