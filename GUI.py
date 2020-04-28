from tkinter import*
from tkinter import messagebox
repeat=200
cursor=0

def clear():                            #функция очистки поля ввода
    entry.delete(0, END)

def btn_1_entry():
    global cursor
    entry.insert(cursor,"GCD()")
    cursor+=5
def btn_2_entry():
    global cursor
    entry.insert(cursor,"LCM()")
    cursor+=5
def btn_3_entry():
    global cursor
    entry.insert(cursor,"der()")
    cursor+=5
def btn_4_entry():
    global cursor
    entry.insert(cursor,"derivative()")
    cursor+=12
def btn_5_entry():
    global cursor
    entry.insert(cursor,"reduce()")
    cursor+=8
def btn_6_entry():
    global cursor
    entry.insert(cursor,"reduceQ()")
    cursor+=9
def btn_7_entry():
    global cursor
    entry.insert(cursor,"rdc()")
    cursor+=5
def btn_8_entry():
    global cursor
    entry.insert(cursor,"reducifraction()")
    cursor+=16
def btn_9_entry():
    global cursor
    entry.insert(cursor,"defrac()")
    cursor+=8
def btn_10_entry():
    global cursor
    entry.insert(cursor,"deg()")
    cursor+=5
def btn_11_entry():
    global cursor
    entry.insert(cursor,"degree()")
    cursor+=8
def btn_12_entry():
    global cursor
    entry.insert(cursor,"lead()")
    cursor+=6
def btn_13_entry():
    global cursor
    entry.insert(cursor,"leadcoef()")
    cursor+=10
def btn_14_entry():
    global cursor
    entry.insert(cursor,"factor()")
    cursor+=8
def btn_15_entry():
    global cursor
    entry.insert(cursor,"factorize()")
    cursor+=11

def btn_help():                         #функция вызова поля помощи(нет текста)
    information = '''Добро пожаловать в алгебраическую систему для вычислений.
С помощью данной программы Вы можете выполнять любые арифметические действия в множествах N, Z, Q и Полиномов.
Основные команды:
• GCD( ) - НОД
• LCM( ) - НОК
• der( ) - Производная
• derivative( ) - Производная
• reduce( ) - Сокращение
• reduceQ( ) - сокращение
• rdc( ) - сокращение
• reducefraction( ) - сокращение
• defrac( ) - 
• deg( ) - старшая степень
• degree( ) - старшая степень
• lead( ) - старший коэффициент
• leadcoef( ) - старший коэффициент
• factor( ) - факториал 
• factorize( ) - факториал
'''
    messagebox.showinfo("Help", information)


def btn_add():
    global repeat
    if (repeat>=200):
        add_btn.config(state="disabled")
    label = Label(text="Введите числа или полином",  # подпись(что делать)
                  foreground="#105753",  # цвет подписи
                  padx="10",  # отступ по горизонтали
                  pady="10",  # отступ по вертикали
                  )
    label.place(x=110, y=5+repeat)  # вывод подписи

    entry = Entry()  # ввод чего-то из консоли
    entry.place(height=20, width=480, x=290, y=15+repeat)  # вывод поля чего-то

    out_label = Label(text="Место для вывода",  # вывод программы
                      foreground="#105753",
                      padx="10",
                      pady="20"
                      )
    out_label.place(x=165, y=80+repeat)
    output = Entry()
    output.insert(0, "Результат работы программы. ХЗ как его подключить")  # полином или число
    output.place(height=100, width=480, x=290, y=60+repeat, anchor="nw")  # координаты поля
    add_btn.place(x=190,y=200+repeat)
    repeat+=200
root = Tk()
root.title("Наш интерфейс")                     #название окна
root.geometry("800x600")                        #размеры окна
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
add_btn = Button(text = "Add field",
             background = "#105753",     #цвет кнопки
             foreground = "#D6EBEA",     #цвет текста
             activebackground = "#14837D",  #цвет кнопки при нажатии
             height=1,
             width=6,
             padx = "5",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = btn_add         #комманда, выполняемая кнопкой
            )
add_btn.place(x = 190, y = 200)
help_btn.place(x = 710, y = 545)        #позиция кнопоки
clear_btn.place(x = 610, y = 545)       #задается координатами левого верхнего угла

label = Label(text = "Введите числа или полином",   #подпись(что делать)
              foreground = "#105753",               #цвет подписи
              padx = "10",                          #отступ по горизонтали
              pady = "10",                          #отступ по вертикали
              )
label.place(x = 110, y = 5)       #вывод подписи

entry = Entry()                                     #ввод чего-то из консоли
entry.place(height = 20, width = 480, x = 290, y = 15)   #вывод поля чего-то

out_label = Label(text = "Место для вывода",        #вывод программы
               foreground = "#105753",
               padx = "10",
               pady = "20"
               )
out_label.place(x = 165, y = 80)
output = Entry()
output.insert(0, "Результат работы программы. ХЗ как его подключить")        #полином или число
output.place(height = 100, width = 480, x = 290, y = 60, anchor = "nw")        #координаты поля

btn1 = Button(text = "GCD", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_1_entry
              )

btn2 = Button(text = "LCM", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
               height = 1, width = 13,
              command = btn_2_entry
              )

btn3 = Button(text = "der", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_3_entry
              )

btn4 = Button(text = "derivative", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_4_entry
              )

btn5 = Button(text = "reduce", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_5_entry
              )

btn6 = Button(text = "reduceQ", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_6_entry
              )

btn7 = Button(text = "rdc", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_7_entry
              )

btn8 = Button(text = "reducefraction", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_8_entry
              )

btn9 = Button(text = "defrac", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_9_entry
              )

btn10 = Button(text = "deg", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_10_entry
              )

btn11 = Button(text = "degree", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_11_entry
              )

btn12 = Button(text = "lead", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_12_entry
              )

btn13 = Button(text = "leadcoef", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_13_entry
              )

btn14 = Button(text = "factor", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_14_entry
              )

btn15 = Button(text = "factorize", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = btn_15_entry
              )

btn1.place(x = 5, y = 5)
btn2.place(x = 5, y = 35)
btn3.place(x = 5, y = 65)
btn4.place(x = 5, y = 95)
btn5.place(x = 5, y = 125)
btn6.place(x = 5, y = 155)
btn7.place(x = 5, y = 185)
btn8.place(x = 5, y = 215)
btn9.place(x = 5, y = 245)
btn10.place(x = 5, y = 275)
btn11.place(x = 5, y = 305)
btn12.place(x = 5, y = 335)
btn13.place(x = 5, y = 365)
btn14.place(x = 5, y = 395)
btn15.place(x = 5, y = 425)

root.mainloop()
