import json
from pathlib import Path

#Definição de caminho para onde as tasks serão salvas
DATA_FILE = Path("data/tasks.json")

#inicia uma lista vazia
tasks = []

#cria a task
def add_task(description):
    #descricao da task e se ela esta feita ou não
    task = {
        "description": description,
        "completed": False
    }
    #adiciona a task na lista
    tasks.append(task)
    # print(f"Tarefa adicionada com a seguinte descrição: '{description}'.")

#lista todas tarefas com um indice da ordem de criação e status (true/false -  concluida/pendente)
def list_tasks():
    if not tasks:
        print("Não existe nenhuma tarefa na lista.")
    else:
        for idx, task in enumerate(tasks):
            status = "Concluída" if task.get ("completed") else "Pendente"
            print (f"{idx + 1}.{task['description']} [{status}]")

#marca se a task (por índice) foi completada ou não pelo usuario
def mark_task_completed(task_index):
    try:
        task = tasks[task_index]
        if task["completed"]:
            # print(f"Tarefa '{task['description']}' já está concluída.")
            # print("\n")
            escolha = input("Deseja marcar como pendente? (s/n): ").lower()
            # print("\n")
            if escolha == "s":
                task["completed"] = False
                # print(f"Tarefa '{task['description']}' marcada como pendente.")
                # print("\n")
            else:
                print(f"Tarefa '{task['description']}' permanece concluída.")
                # print("\n")
        else:
            task["completed"] = True
            # print(f"Tarefa '{task['description']}' marcada como concluída.")
    except IndexError:
        print("Índice de tarefa inválido.")

#remove a task (por índice) da lista
def remove_task(task_index):
    try:
        remove_task = tasks.pop(task_index)
        # print(f"Tarefa '{remove_task['description']}' removida da lista.")
    except IndexError:
        print("Índice de tarefa inválido. Confira o índice para exclusão.")

#edição de tarefa
def edit_task(task_index, new_description):
    try:
        task = tasks[task_index]
        task['description'] = new_description
        # print(f"Tarefa {task_index + 1 } atualizada para: '{new_description}'.")
    except IndexError:
        print("Índice de tarefa inválido.")

def search_tasks(query):
    return [task for task in tasks if query.lower() in task['description'].lower()]


#salva a lista de tasks no json
def save_tasks():
    #abre o arquivo em modo de escrita e salva a lista de tasks como Json
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)
    # print("Tarefas salvas.")

#Carrega as tasks do Json se o arquivo existir
def load_tasks():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as file:
                global tasks
                tasks = json.load(file)
                for task in tasks:
                    if "description" not in task or "completed" not in task:
                        raise ValueError("Formato de tarefa inválido no arquivo.")
            # print("Tarefas carregadas.")
        except json.JSONDecodeError as e:
            #se o json estiver vazio ou invalido, incia como uma lista vazia
            tasks = []
            # print("Arquivo de tarefas vazio ou invalido. Erro ao carregar tarefas: {e}. A lista será excluída e será iniciada uma lista vazia para uso.")
    else:
        print(f"O arquivo {DATA_FILE} não foi encontrado.")