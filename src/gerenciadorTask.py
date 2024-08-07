import json
from pathlib import Path
from datetime import datetime

# Definição do caminho para onde as tasks serão salvas
DATA_FILE = Path("data/tasks.json")

# Inicia uma lista vazia
tasks = []

# Cria uma task
def add_task(description, due_date = None):
    global tasks
    # Verifica se a data é válida e posterior ao dia atual
    if due_date:
        try:
            due_date_obj = datetime.strptime(due_date, "%d/%m/%y")
            if due_date_obj.date() <= datetime.today().date():
                raise ValueError("A data deve ser posterior ao dia de hoje.")
        except ValueError as e:
            raise ValueError(f"Data inválida: {e}")

    # Cria um dicionário para a tarefa com descrição e status de conclusão
    task = {
        "description": description,
        "completed": False,
        "due_date": due_date
    }

    # Adiciona a tarefa na lista
    tasks.append(task)
    # print(f"Tarefa adicionada com a seguinte descrição: '{description}'.")

# Lista todas as tarefas com índice e status
def list_tasks():
    if not tasks:
        print("Não existe nenhuma tarefa na lista.")
    else:
        for idx, task in enumerate(tasks):
            status = "Concluída" if task.get ("completed") else "Pendente"
            print (f"{idx + 1}.{task['description']} [{status}]")
    return tasks

# Função para marcar uma tarefa como concluída ou pendente
def mark_task_completed(task_index):
    global tasks
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        task["completed"] = not task["completed"]
    else:
        print("Índice de tarefa inválido.")

# Função para remover uma tarefa da lista
def remove_task_completed(task_index):
    global tasks
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Índice de tarefa inválido. Confira o índice para exclusão.")

# Função para editar a descrição de uma tarefa
def edit_task_completed(index, new_description, new_due_date=None):
    tasks[index]["description"] = new_description
    if new_due_date:
        tasks[index]["due_date"] = new_due_date
        # print(f"Tarefa {task_index + 1 } atualizada para: '{new_description}'.")
    else:
        print("Índice de tarefa inválido.")

# Função para buscar tarefas com base em uma query
def search_tasks(query):
    return [task for task in tasks if query.lower() in task['description'].lower()]

# Função para salvar a lista de tarefas no arquivo JSON
def save_tasks():
    # Abre o arquivo em modo de escrita e salva a lista de tarefas como JSON
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)
    save_tasks()
    # print("Tarefas salvas.")

# Função para carregar as tarefas do arquivo JSON se ele existir
def load_tasks():
    global tasks
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as file:
                tasks = json.load(file)
                for task in tasks:
                    if "description" not in task or "completed" not in task:
                        raise ValueError("Formato de tarefa inválido no arquivo.")
        except json.JSONDecodeError as e:
            tasks = []
            print(f"Arquivo de tarefas vazio ou inválido. Erro ao carregar tarefas: {e}. A lista será excluída e uma lista vazia será iniciada para uso.")
    else:
        print(f"O arquivo {DATA_FILE} não foi encontrado.")
