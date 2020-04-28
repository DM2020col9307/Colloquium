from tkinter import*
from tkinter import messagebox
from main import *

def clear():
    """Функция очистки полей ввода и вывода"""
    entry.delete(0, END)
    output.config(state=NORMAL)
    output.delete(1.0,END)
    output.config(state=DISABLED)
def btn_help():
    """Функция вывода информативного окна для помощи пользователю в пользовании программы"""
    information = '''Добро пожаловать в алгебраическую систему для вычислений.
С помощью данной программы Вы можете выполнять любые арифметические действия в множествах N, Z, Q и Полиномов.
После ввода команды необходимо ввести желаемое число из N,Z,Q или Полиномов в скобки. 
Если Вы используете числа из разных множеств - они приведутся к старшему типу, если это возможно
Основные команды:
• GCD( ) - НОД
• LCM( ) - НОК
• der( ) - Производная
• reduce( ) - Сокращение дроби
• deg( ) - Старшая степень полинома
• lead( ) - Старший коэффициент полинома
Также вы можете сравнивать и использовать любые операторы сравнения. 1 - результат вернул True, 0 - False
Ещё доступны стандартные команды:
• Сложение (+)
• Вычитание (-)
• Деление (/, //, %)
• Возведение в степень (^, **)
'''
    messagebox.showinfo("Help", information)
def btn_ok():
    """Функция, отвечающая за действия при нажатии на кнопку OK"""
    try:
        output.config(state=NORMAL)
        output.delete(1.0, END)
        s=output.insert(1.0,eval(parse(input_text.get())))
        output.config(state=DISABLED)
    except Exception as e:
        messagebox.showinfo("ОШИБКА!", e) #Вывод текста ошибки во всплывающее окно
def press_enter(event):
    """Функция, отвечающая за действия при нажатии на кнопку OK"""
    output.delete(1.0, END)
    try:
        output.config(state=NORMAL)
        s = output.insert(1.0, eval(parse(input_text.get())))
        output.config(state=DISABLED)
    except Exception as e:
        messagebox.showinfo("ОШИБКА!", e)  # Вывод текста ошибки во всплывающее окно

root = Tk()
root.title("Алгебраическая система")                     #название окна
root.geometry("800x600+300+100")                        #размеры окна и смещение его в центр
root.resizable(False, False) #Отменить возможнось расширения окна
root.iconbitmap(r'.\images\icon.ico')
image1=PhotoImage(file=".\images\icon1.gif")
image2=PhotoImage(file=".\images\icon2.gif")
image3=PhotoImage(file=".\images\icon3.gif")
image4=PhotoImage(file=".\images\icon4.gif")
image5=PhotoImage(file=".\images\icon5.gif")
image6=PhotoImage(file=".\images\icon6.gif")
image7=PhotoImage(file=".\images\icon7.gif")
image_ok=PhotoImage(file=".\images\ok.gif")
image_help=PhotoImage(file=".\images\help.gif")
image_clear=PhotoImage(file=".\images\clear.gif")
input_text=StringVar()
help_btn = Button(image=image_help,
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = btn_help             #комманда, выполняемая кнопкой
             )

clear_btn = Button(image=image_clear,
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = clear          #комманда, выполняемая кнопкой
            )

ok_btn = Button(image=image_ok,
             padx = "20",               #отступ по горизонтали
             pady = "5",               #отступ по вертикали
             font = "16",                #высота шрифта
             command = btn_ok       #комманда, выполняемая кнопкой
            )
ok_btn.place(x=500,y=545, height=40, width=90)
help_btn.place(x = 700, y = 545, height=40, width=90 )        #позиция кнопоки
clear_btn.place(x = 600, y = 545, height=40, width=90)       #задается координатами левого верхнего угла

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
output.config(state=DISABLED)
output.place(height = 100, width = 480, x = 120, y = 115)        #координаты поля
entry.bind('<Return>', press_enter)

btn1 = Button(
             height = 20, width = 95, compound=TOP, image=image1,
              command = lambda x='GCD()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x

btn2 = Button(height = 20, width = 95, compound=TOP, image=image2,
              command = lambda x='LCM()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x

btn3 = Button(height = 20, width = 95, compound=TOP, image=image3,
              command = lambda x='der()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x


btn4 = Button(height = 20, width = 95, compound=TOP, image=image4,
              command = lambda x='reduce()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x


btn5 = Button(height = 20, width = 95, compound=TOP, image=image5,
              command = lambda x='deg()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x


btn6 = Button(height = 20, width = 95, compound=TOP, image=image6,
              command = lambda x='lead()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x

btn7 = Button(height = 20, width = 95, compound=TOP, image=image7,
              command = lambda x='factor()': (entry.insert(entry.index(INSERT), x), entry.icursor(entry.index(INSERT)-1))
              ) #При нажатии на кнопку будет введен текст, хранящийся в x


#Координаты кнопок в левом меню
btn1.place(x = 5, y = 5)
btn2.place(x = 5, y = 35)
btn3.place(x = 5, y = 65)
btn4.place(x = 5, y = 95)
btn5.place(x = 5, y = 125)
btn6.place(x = 5, y = 155)
btn7.place(x = 5, y = 185)


root.mainloop()
