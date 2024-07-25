run_again = True
while run_again:
    print('Welcom to the Todo List Manager 😊')
    print('My name is Alexia, how may I help you today?')
    print(
        """
1. Add task
2. Remove task
3. view tasks
4. Edit task
        """
    )
    user_choice = input("Select an option [1 - 4]:")
    user_choice = int(user_choice)
    tasks = [ ]
    if user_choice == 1:
        new_task = input('Enter the task to add: ')
        tasks.append(new_task)
        print(f"{new_task} has been add successfully")
    elif user_choice == 2:
        for task in tasks:
            print(task)
        user_choice= input("Enter the task no of the task you wish to remove: ")
        user_choice = int(user_choice)
        task_to_remove = tasks.pop(user_choice - 1)
        print("f{task_to_remove}has been removed\n")
    elif user_choice == 3:
        for task in tasks:
            print(task)
    run_again = user_choice != 4