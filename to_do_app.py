import sys, os

# FUNCTION TO CLEAR THE CONSOLE AFTER EACH OPERATION TO MAKE THE APP NEAT
def clear():
    os.system('cls')

# Function to display TO-DO list
def display_todo(todo_pending, todo_completed):
    #statement to verify if both pending and completed lists are empty.
    check = True
    while check:
        if (not todo_pending) and (not todo_completed):
            print('Press 1 to add new task ')
            print('Press 2 to cancel ')
            result = input('Input : ')

            if result == '1':
                check = False
                add_todo(todo_pending,todo_completed)
            elif result == '2':
                sys.exit()
            else:
                print('Enter a valid input 1 or 2 :')
    # condition if todo_pending contains infomation and todo_complted does not
        elif (todo_pending) and (not todo_completed):
            for index, x in enumerate(todo_pending):
                print(str(index) + "\t" + x)

            print("---------------------------END OF LIST---------------------------------")
            print('Press 1 to add new task ')
            print('Press 2 to mark as complete ')
            print('Press 3 to cancel ')
            result = input('Input : ')

            if result == '1':
                check = False
                add_todo(todo_pending, todo_completed)
            elif result == '2':
                check = False
                mark_as_complete(todo_pending, todo_completed)
            elif result == '3':
                sys.exit()
            else:
                print('Enter a valid input 1, 2 or 3: ')
                result = input( )

        elif ((todo_completed) and (todo_pending)) or ((todo_completed) and (not todo_pending)) or ((not todo_completed) and (todo_pending)):
            print("---------------------------TO DO LIST------------------------------")
            for index, x in enumerate(todo_pending):
                print(str(index) + "\t" + x)
            print("  ")

            print("---------------------------COMPLETED LIST------------------------------")
            for index, x in enumerate(todo_completed):
                print(str(index) + "\t" + x)

            print("---------------------------END OF LIST---------------------------------")
            print('Press 1 to add new task ')
            print('Press 2 to mark as complete ')
            print('Press 3 to mark as incomplete ')
            print('Press 4 to cancel ')
            result = input('Input : ')

            if result == '1':
                check = False
                add_todo(todo_pending, todo_completed)
            elif result == '2':
                check = False
                mark_as_complete(todo_pending, todo_completed)
            elif result == '3':
                check = False
                mark_as_incomplete(todo_pending, todo_completed)
            elif result == '4':
                sys.exit()
            else:
                print('Enter a valid input 1, 2, 3 or 4 : ')
                result = input( )
        else:
            Print("Something went wrong, go fix it")
            sys.exit()

#Function to add to todo_pending lists
def add_todo(new_todo_pending, new_todo_completed):
    clear()
    print('Enter new tasks below: \n')
    newtask = input(" - ")
    new_todo_pending.append(newtask)
    clear()
    display_todo(new_todo_pending, new_todo_completed)

# Function to mark item on list as completed.
def mark_as_complete(new_todo_pending, new_todo_completed):
    print('Pick an index position to mark as completed.')
    task_complete = int(input(': ' ))
    clear()
    # code that pops item specified at a given index position and appends to the completed list
    new_todo_completed.append(new_todo_pending.pop(task_complete))
    display_todo(new_todo_pending, new_todo_completed)

# reverse of the function markascomplete
def mark_as_incomplete(new_todo_pending,new_todo_completed):
    print('Pick an index position to mark as Incompleted.')
    task_not_complete = int(input(': ' ))
    clear()
    # code that pops item specified at a given index position and appends to the completed list
    new_todo_pending.append(new_todo_completed.pop(task_not_complete))
    display_todo(new_todo_pending, new_todo_completed)
