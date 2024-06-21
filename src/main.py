from gerenciadorTask import add_task, list_tasks, save_tasks, load_tasks

#gerenciamento de interação com o usuário
def main():
    print("Carregando as tarefas...")
    load_tasks()
    print("Tarefas carregadas.")

    while True:
        print("1. Criar uma tarefa\n2. Ver lista de tarefas\n3. Sair")
        escolha = input("Escolha uma opção acima: ")

        #condição da escolha
            #add_task
        if escolha == "1":
            descricao = input("Descreva a tarefa: ")
            print(f"Tarefa adcionada: {descricao}")
            add_task(descricao)
        elif escolha == "2":
            #list_tasks
            print("Lista de tarefas:")
            list_tasks()
        elif escolha == "3":
            #save_tasks 
            save_tasks()
            print("Tarefas salvas. Saindo do programa.")
            break
        else:
            #saida de escolha errada
            print("Escolha invalidada, por favor, tente novamente.")

if __name__ == "__main__":
    main()