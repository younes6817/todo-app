import PySimpleGUI as sg
# from mojors.Calculadora_functions import Radical
import math as riazi
import time




sg.theme('NeonBlue1')

input_box = sg.InputText(tooltip="enter a number", key="number")
plus_button = sg.Button('+', key='+')
negativos_button = sg.Button('-', key='-')
multiplicativos_button = sg.Button('×', key='*')
divisiones_button = sg.Button('÷', key='/')
igual_button = sg.Button('=', key='=')
radical_button = sg.Button('√', key='R')
power_button = sg.Button('Xⁿ', key='^')
percentage_button = sg.Button('%', key='%')
pi_button = sg.Button('π', key='π')
pifull_button = sg.Button('πFULL', key='πf')
exit_button = sg.Button('quit', key='quit')



Window = sg.Window("my Calculadora",
                   layout=[[input_box],
                        [plus_button, negativos_button, multiplicativos_button, divisiones_button,
                         power_button, radical_button, percentage_button],
                           [pi_button, pifull_button],
                           [igual_button],
                           [exit_button],],
                   font=(100))
try:
    while True:
        answer = Window.read()
        input_box.update(value="")
        # answer2 = Window.read()
        answer_car = answer[0]
        answer_number = answer[1]
        answer_number = float(answer_number["number"])
        # answer_number2 = answer2[1]
        # answer_number2 = int(answer_number2["number"])

        match answer_car:
            case "+":
                answer_car2 = "+"
                input_box.update(value="")
                while answer_car2 == "+":
                    answer2 = Window.read()
                    input_box.update(value="")
                    answer_car2 = answer2[0]
                    answer_number2 = answer2[1]
                    answer_number2 = float(answer_number2["number"])
                    answer_number = answer_number + answer_number2
                print(answer_number)
                input_box.Update(value=answer_number)
            case "-":
                answer_car2 = "-"
                input_box.update(value="")
                while answer_car2 == "-":
                    answer2 = Window.read()
                    input_box.update(value="")
                    answer_car2 = answer2[0]
                    answer_number2 = answer2[1]
                    answer_number2 = float(answer_number2["number"])
                    answer_number = answer_number - answer_number2
                print(answer_number)
                input_box.Update(value=answer_number)
            case "*":
                answer_car2 = "*"
                input_box.update(value="")
                while answer_car2 == "*":
                    answer2 = Window.read()
                    input_box.update(value="")
                    answer_car2 = answer2[0]
                    answer_number2 = answer2[1]
                    answer_number2 = float(answer_number2["number"])
                    answer_number = answer_number * answer_number2
                print(answer_number)
                input_box.Update(value=answer_number)
            case "/":
                answer_car2 = "/"
                input_box.update(value="")
                while answer_car2 == "/":
                    answer2 = Window.read()
                    input_box.update(value="")
                    answer_car2 = answer2[0]
                    answer_number2 = answer2[1]
                    answer_number2 = float(answer_number2["number"])
                    answer_number = answer_number / answer_number2
                print(answer_number)
                input_box.Update(value=answer_number)
            case "^":
                answer_car2 = "^"
                input_box.update(value="")
                while answer_car2 == "^":
                    answer2 = Window.read()
                    input_box.update(value="")
                    answer_car2 = answer2[0]
                    answer_number2 = answer2[1]
                    answer_number2 = float(answer_number2["number"])
                    answer_number = answer_number ** answer_number2
                print(answer_number)
                input_box.Update(value=answer_number)
            case "R":
                answer_number = riazi.sqrt(answer_number)
                answer_number = float(answer_number)
                input_box.Update(value=answer_number)
            case "%":
                input_box.update(value="")
                input_box.update(value="SOON")
            case "π":  # TODO: error pi
                pi = 3.14
                input_box.update(value=pi)
            case "πf":
                pifull = 3.141592653589793238462643383279502884197
                input_box.update(value=pifull)
            case "quit":
                # TODO:اگر چیزی ننویسی ارور میده
                exit("exit")
except ValueError:
    # TODO:ننوشتن ارور
    input_box.update(value="")
    input_box.update(value="Error")
    time.sleep(1)
    Window.close()