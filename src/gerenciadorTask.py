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
    print(f"Tarefa adicionada com a seguinte descrição: '{description}'.")

#lista todas tarefas com um indice da ordem de criação e status (true/false -  concluida/pendente)
def list_tasks():
    if not tasks:
        print("Não existe nenhuma tarefa na lista.")
    else:
        for idx, task in enumerate(tasks):
            status = "Done" if task.get ("completed") else "Pending"
            print (f"{idx + 1}.{task['description']} [{status}]")

#salva a lista de tasks no json
def save_tasks():
    #abre o arquivo em modo de escrita e salva a lista de tasks como Json
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)
    print("Tarefas salvas.")

#Carrega as tasks do Json se o arquivo existir
def load_tasks():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as file:
                global tasks
                tasks = json.load(file)
            print("Tarefas carregadas.")
        except json.JSONDecodeError:
            #se o json estiver vazio ou invalido, incia como uma lista vazia
            tasks = []
            print("Arquivo de tarefas vazio ou invalido. Foi ajustado para o proximo uso.")
                