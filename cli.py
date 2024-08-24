from  mojors.functions import get_todos, set_todos
import time

now = time.strftime("%a ,%d %b %Y ,%I:%M:%S %p")
print("It is ", now)
todos = []

while True:
    user_action = input("enter add or show or delete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        # todo = input("enter: ")+"\n"

        todos = get_todos("todos.txt")
        todo = user_action[4:]
        todos.append(todo+"\n")
        set_todos(todos, "todos.txt")
        massage = f"todo {todo} add."
        print(massage)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}.{todo.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos("todos.txt")
            number = int(user_action[5:])
            new = input("enter new item: ")+"\n"
            number = number - 1
            todos[number] = new
            set_todos(todos, "todos.txt")
        except IndexError:
            print("your number is out of range")
        except ValueError:
            print("you should enter number")

    elif user_action.startswith("delete"):
        try:
            todos = get_todos("todos.txt")
            index = int(user_action[7:])-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            set_todos(todos, "todos.txt")

            massage = f"todo {todo_to_remove} has been delete."
            print(massage)
            set_todos(todos, "todos.txt")
        except ValueError:
            print("you should enter number")
        except IndexError:
            print("your number is out of range")


    elif user_action.startswith("exit"):
        break
    else:
        massage = (f"not{y}is proclab")
        print(massage)
print("Done")