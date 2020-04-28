from tkinter import*
from tkinter import messagebox

def clear():                            #функция очистки поля ввода
    entry.delete(0, END)

def btn_help():                         #функция вызова поля помощи(нет текста)
    information = "Тут должна быть помощь\n Но мне лень ее писать\n Напишите за меня, плиз\n[McM] О'кей, и за меня...\n"
    messagebox.showinfo("Help", information)

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

btn5 = Button(text = "degree", background = "#105753", foreground = "#D6EBEA", activebackground = "#14837D",
              height = 1, width = 13,
              command = lambda x='degree()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
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
