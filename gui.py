from mojors.functions import get_todos, set_todos
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme('NeonBlue1')

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add", image_size=(100, 34), image_source="add.png", button_color='white', mouseover_colors="red")
list_box = sg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My TO-DO App",
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                   [exit_button],],
                   font=("Helvetica", 20),)

while True:
    event, values = window.read(timeout=10)
    window["clock"].Update(value=time.strftime("%b %d, %Y %I:%M:%S %p"))
    # print(event, values)
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            set_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                set_todos(todos)
                window["todo"].update(value="")
                window["todos"].update(values=todos)
            except:
                sg.popup("Something went wrong", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                set_todos(todos)
                window["todo"].update(value= "")
                window["todos"].update(values=todos)
            except:
                sg.popup("Something went wrong", font=("Helvetica", 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            exit()
window.close()
