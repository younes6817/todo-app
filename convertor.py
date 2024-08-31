from feet_inches import  convert
import PySimpleGUI as sg

sg.theme('DarkAmber')

input_box = sg.InputText(tooltip="enter a number", key="number")
input_box2 = sg.InputText(tooltip="enter a number", key="number2")
text_box = sg.Text("enter feet", key="feet")
text_box2 = sg.Text("enter inches", key="inches")
convert_button = sg.Button('Convert', key='convert')


window = sg.Window('Convertor',
                   layout=[[text_box, input_box],
                    [text_box, input_box2],
                    [convert]])

answer = window.read()
print(answer)