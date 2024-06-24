from gerenciadorTask import add_task, list_tasks, mark_task_completed, remove_task, save_tasks, load_tasks

#gerenciamento de interação com o usuário
def main():
    print("\n")
    print("Carregando as tarefas...")
    load_tasks()
    print("\n")
    print("Tarefas carregadas.")
    print("\n")

    while True:
        print("1. Criar uma tarefa\n2. Ver lista de tarefas\n3. Marcar uma tarefa como concluída\n4. Remover uma tarefa da lista\n5. sair")
        print("\n")
        escolha = input("Escolha uma opção acima: ")

        #condição da escolha
            #add_task
        if escolha == "1":
            descricao = input("Descreva a tarefa: ")
            print("\n")
            print(f"Tarefa adcionada: {descricao}")
            add_task(descricao)
            print("\n")
        elif escolha == "2":
            #list_tasks
            print("\n")
            print("Lista de tarefas:")
            list_tasks()
            print("\n")
        elif escolha == "3":
            print("\n")
            #marcar como concluida
            list_tasks()
            print("\n")
            try:
                task_index = int(input("Digite o índice da tarefa que deseja marcar como concluída:")) - 1
                mark_task_completed(task_index)
                print("\n")
            except ValueError:
                print("Índice inválido. Por favor, revise o índice da tarefa.")
                print("\n")
        elif escolha == "4":
            print("\n")
            list_tasks()
            try:
                task_index = int(input("Digite o índice da tarefa que deseja excluir da lista:")) - 1
                remove_task(task_index)
            except ValueError:
                print("Índice inválido. Por favor, revise o índice da tarefa.")
                print("\n")
            print("\n")
        elif escolha == "5":
            #save_tasks 
            save_tasks()
            print("\n")
            print("Tarefas salvas. Saindo do programa.")
            print("\n")
            break
    else:
        #saida de escolha errada
        print("Escolha invalidada, por favor, tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()