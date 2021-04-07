from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Menu
from os import path

window = Tk()
window.title("Taxi-route estimator")
window.geometry('420x220+300+300')

file = StringVar()
file.set('')
selected = IntVar()
linecount = 10


def processHandler(file): # только импорт и подсчет
    # open(file)
    # count lines in file
    # linecount = count(file)
    pass

def startProcessingOne():
    print('processing ' + str(selected.get()))
    createResultWindow('processing ' + str(selected.get()))
    pass


def startProcessingAll():
    print('processing all')
    createResultWindow('processing all')
    pass

def showAbout():
    res = Tk()
    res.title("About")
    res.geometry('220x220+630+330')

    txt = scrolledtext.ScrolledText(res, width=28, height=27, wrap=WORD)
    txt.place(x=0,y=0)

    txt.insert(1.0, 'Мой хэлп текст, сделал я, права мои')
    res.mainloop()

def createResultWindow(substring):
    res = Tk()
    res.title("Prediction Info")
    res.geometry('220x420+330+330')

    txt = scrolledtext.ScrolledText(res, width=28, height=27, wrap=WORD)
    txt.place(x=0,y=0)

    txt.insert(1.0, substring)
    res.mainloop()


def showSelector():
    global chk, chk_state
    lbl = Label(window, text="Укажите номер")
    lbl.place(x=30, y=80)
    spin = Spinbox(window, textvariable=selected, from_=0, to=linecount, width=13, wrap=True)
    spin.place(x=152, y=80)
    chk = Button(window, text="Обработать эту", command=startProcessingOne)
    chk.place(x=150, y=106)
    chk = Button(window, text="Обработать все", command=startProcessingAll)
    chk.place(x=150, y=136)


def selectFile():
    fileTemp = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    if not fileTemp: return
    file.set(fileTemp[:5] + '...' + fileTemp[-12:])
    processHandler(fileTemp)
    showSelector()
    # ... дает путь до файла, функцию переименовтаь, загруить в панду



menu = Menu(window)
aboutmenu = Menu(menu)
aboutmenu.add_command(label='About', command=showAbout)
aboutmenu.add_separator()
aboutmenu.add_command(label='Exit', command=exit)
menu.add_cascade(label='Info', menu=aboutmenu)
window.config(menu=menu)



Label(window, text="Расчетчик времени").place(x=130, y=8)


lbl = Label(window, text="Выберите файл")
lbl.place(x=30, y=40)
btn = Button(window, text="Выбрать", command=selectFile)
btn.place(x=150, y=36)
lx = Label(window, textvariable=file)
lx.place(x=240, y=40)
'''
el = Label(window, text=chk_state.get())
el.place(x=0, y=0)'''

window.mainloop()
