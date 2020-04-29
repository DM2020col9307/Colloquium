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
• GCD( *, * ) - НОД 
• LCM( *, * ) - НОК
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
root.iconbitmap(r'.\images\icon.ico') #иконка программы
image1=PhotoImage(file=".\images\icon1.gif") #кнопки
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
ok_btn.place(x=260,y=545, height=40, width=90) #Позиция кнопки Ok
help_btn.place(x = 360, y = 545, height=40, width=90)        #позиция кнопоки help
clear_btn.place(x = 460, y = 545, height=40, width=90)       #позиция кнопки clear

label = Label(text = "ВВЕДИТЕ АЛГЕБРАИЧЕСКОЕ ВЫРАЖЕНИЕ",   #подпись(что делать)
              foreground = "#105753",               #цвет подписи
              padx = "20",                          #отступ по горизонтали
              pady = "20",                          #отступ по вертикали
              font="Arial 16"
              )
label.place(x = 150, y = 60)       #координаты подписи

entry = Entry(textvariable=input_text)                                    #окно ввода
entry.place(height = 20, width = 480, x = 160, y = 130)   #координаты окна ввода

out_label = Label(text = "РЕЗУЛЬТАТ",        #надпись
               foreground = "#105753",
               padx = "10",
               pady = "10",
               font="Arial 16"
               )
out_label.place(x = 310, y = 170) #координаты надписи
output = Text() #окно вывода
output.config(state=DISABLED) #отлючаем возможность ввода в окно вывода
output.place(height = 100, width = 480, x = 160, y = 220)        #положение окна вывода
entry.bind('<Return>', press_enter) #обработка нажатия Enter'a

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
btn1.place(x = 20, y = 10)
btn2.place(x = 130, y = 10)
btn3.place(x = 240, y = 10)
btn4.place(x = 350, y = 10)
btn5.place(x = 460, y = 10)
btn6.place(x = 570, y = 10)
btn7.place(x = 680, y = 10)


root.mainloop()
