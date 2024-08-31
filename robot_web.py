import streamlit as st
import os


def save_language(language):
    with open("languages.txt", 'w') as languages_file:
        languages_file.write(language)

if not os.path.exists("languages.txt"):
    with open("languages.txt", 'w') as languages_file:
        pass

with open("languages.txt", 'r') as languages_file:
    language = languages_file.readline()

# نمایش عنوان و خوش‌آمدگویی
st.title('My Robot')
st.subheader('Welcome to Robot')
st.write('I am a robot that you can talk to')

# بررسی زبان انتخاب شده یا درخواست از کاربر برای انتخاب
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = language if language else ""

# تابع برای تغییر زبان
def set_language():
    st.session_state.selected_language = st.session_state.input_language
    if "persian" in st.session_state.input_language.lower():
        st.session_state.selected_language = "Persian"
        save_language("Persian")
    elif "english" in st.session_state.input_language.lower():
        st.session_state.selected_language = "English"
        save_language("English")
    else:
        st.write('Coming soon')

# اگر زبان انتخاب نشده، درخواست زبان از کاربر
if st.session_state.selected_language == "":
    st.text_input(label="Enter language:", placeholder="Language", key="input_language", on_change=set_language)
else:
    if st.session_state.selected_language == "english":
        st.write('Hello')
        help = ""
        st.text_input(label="can I help you?", placeholder="enter", key="help", on_change=help)
        col1, col2 = st.columns(2)
        with col2:
            if "your name" in help:
                print(help)
                st.write(help)
        with col1:
            st.write("my name is YRobot")

    elif st.session_state.selected_language == "Persian":
        st.write("سلام")


