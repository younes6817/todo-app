import streamlit as st
from mojors.functions import get_todos, set_todos

todos = get_todos()

def add_todo():
    todos = get_todos()
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    set_todos(todos)
def remove_todo(todo):
    todos.remove(todo)
    set_todos(todos)
    st.rerun()

st.title('My todo App')
st.subheader('This is my todo app')
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        remove_todo(todo)

st.text_input(label="", placeholder="Enter new todo:",
              key="new_todo", on_change=add_todo)
print("hello")