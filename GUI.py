from tkinter import*
from tkinter import messagebox
from main import *

def clear():                            #функция очистки поля ввода
    entry.delete(0, END)
    output.delete(1.0,END)

def btn_help():
    information = '''Добро пожаловать в алгебраическую систему для вычислений.
С помощью данной программы Вы можете выполнять любые арифметические действия в множествах N, Z, Q и Полиномов.
После ввода команды необходимо ввести желаемое число из N,Z,Q или Полиномов в скобки. 
Если Вы используете числа изразных множеств - они приведутся к старшему типу, если это возможно
Основные команды:
• GCD( ) - НОД
• LCM( ) - НОК
• der( ) - Производная
• reduce( ) - Сокращение дроби
• deg( ) - Старшая степень полинома
• lead( ) - Старший коэффициент полинома
• factor( ) - Факторизация полинома
Также вы можете сравнивать и использовать любые операторы сравнения. 1 - результат вернул True, 0 - False
'''
    messagebox.showinfo("Help", information)
def btn_ok():
    output.delete(1.0,END)
    try:
        s=output.insert(1.0,eval(parse(input_text.get())))
    except Exception as e:
        output.insert(1.0,e)

root = Tk()
root.title("Наш интерфейс")                     #название окна
root.geometry("800x600")                        #размеры окна
input_text=StringVar()
help_btn = Button(text = "Help",             #текст на кнопке
             background = "#105753",     #цвет кнопки
             foreground = "#D6EBEA",     #цвет текста
             activebackground = "#14837D",  #цвет кнопки при нажатии
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = btn_help             #комманда, выполняемая кнопкой
             )

clear_btn = Button(text = "Clear",
             background = "#105753",     #цвет кнопки
             foreground = "#D6EBEA",     #цвет текста
             activebackground = "#14837D",  #цвет кнопки при нажатии
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = clear          #комманда, выполняемая кнопкой
            )

ok_btn = Button(text = "OK",
             background = "#105753",     #цвет кнопки
             foreground = "#D6EBEA",     #цвет текста
             activebackground = "#14837D",  #цвет кнопки при нажатии
             height=1,
             width=6,
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = btn_ok       #комманда, выполняемая кнопкой
            )
ok_btn.place(x=500,y=545)
help_btn.place(x = 710, y = 545)        #позиция кнопоки
clear_btn.place(x = 610, y = 545)       #задается координатами левого верхнего угла

label = Label(text = "Введите алгебраическое выражение",   #подпись(что делать)
              foreground = "#105753",               #цвет подписи
              padx = "10",                          #отступ по горизонтали
              pady = "10",                          #отступ по вертикали
              font="Arial 16"
              )
label.place(x = 110, y = 5)       #вывод подписи

entry = Entry(textvariable=input_text)                                     #ввод чего-то из консоли
entry.place(height = 20, width = 480, x = 120, y = 50)   #вывод поля чего-то

out_label = Label(text = "Результат",        #вывод программы
               foreground = "#105753",
               padx = "10",
               pady = "15",
               font="Arial 16"
               )
out_label.place(x = 110, y = 70)
output = Text()
output.place(height = 100, width = 480, x = 120, y = 115)        #координаты поля

btn1 = Button(text = "GCD", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='GCD()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )

btn2 = Button(text = "LCM", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
               height = 1, width = 13,
              command = lambda x='LCM()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )

btn3 = Button(text = "der", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='der()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )


btn4 = Button(text = "reduce", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='reduce()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )


btn5 = Button(text = "deg", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='deg()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )


btn6 = Button(text = "lead", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='lead()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )

btn7 = Button(text = "factor", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='factor()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              )


btn1.place(x = 5, y = 5)
btn2.place(x = 5, y = 35)
btn3.place(x = 5, y = 65)
btn4.place(x = 5, y = 95)
btn5.place(x = 5, y = 125)
btn6.place(x = 5, y = 155)
btn7.place(x = 5, y = 185)


root.mainloop()
