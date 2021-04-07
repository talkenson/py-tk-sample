from tkinter import *
from tkinter import filedialog
from os import path

window = Tk()
window.title("Taxi-route estimator")
window.geometry('420x220+300+300')

file = ''
selected = 0
linecount = 10


def processHandler(file):
    # open(file)
    # count lines in file
    # linecount = count(file)
    pass


def showSelector():
    global chk, chk_state
    lbl = Label(window, text="Укажите номер")
    lbl.place(x=30, y=80)
    spin = Spinbox(window, from_=0, to=linecount, width=10, wrap=True)
    spin.place(x=150, y=80)
    chk = Button(window, text="Обработать все", command=startProcessing)
    chk.place(x=144, y=106)


def selectFile():
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    processHandler(file)
    showSelector()
    # ... дает путь до файла, функцию переименовтаь, загруить в панду

Label(window, text="Расчетчик времени").place(x=130, y=8)


lbl = Label(window, text="Выберите файл")
lbl.place(x=30, y=40)
btn = Button(window, text="Выбрать", command=selectFile)
btn.place(x=150, y=36)
'''
el = Label(window, text=chk_state.get())
el.place(x=0, y=0)'''

window.mainloop()
