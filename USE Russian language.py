"""USE Russian language.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""ЕГЭ русский язык.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""


import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Radiobutton
import sys

class About4(tk.Toplevel):  # Четверное Окно
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x600+550+100')
        self.title('''       ЕГЭ русский язык (Окно №2 из 3-х)''')
        self.iconbitmap(default="C:\FOTO  Python\mvoice.ico")

        self.foto2 = ImageTk.PhotoImage(file="C:\FOTO  Python\mvovr.png")
        self.button = tk.Button(self, image=self.foto2)
        self.button.pack(padx=0, pady=0)

        self.label = tk.Label(self, text='''1. Правильный ответ: по контексту        
         подразумевается    
         "ЗАТРУДНИТЕЛЬНЫЙ" - содержащий     
          трудности; причиняющий затруднение.    ''', font='Times 14', foreground="#355286")
        self.label.pack(padx=10, pady=30)

        self.label = tk.Label(self, text='''2. Правильно: с "ПОЛУТОРАСТА          
                    рублями".                ''',
                              font='Times 14', foreground="#355286", anchor='nw',
                              justify='center')
        self.label.pack(padx=10, pady=10)

        self.label = tk.Label(self, text='''3. Правильный ответ: "недоумевая".        
        Пишется слитно, потому что          
         не употребляется без НЕ.         ''',
                              font='Times 14', foreground="#355286", anchor='nw',
                              justify='center')
        self.label.pack(padx=10, pady=10)

        # закрытие программы
        self.button__1 = tk.Button(self, text='''Закрыть программу''',
                                   font='Times 19', fg='#b60536',
                                   command=self.exzit)
        self.button__1.pack(padx=10, pady=30)

    def clous_all_okna(self):
        sys.exit()

    def exzit(self):
        choice = messagebox.askyesno("ЗАКРЫТИЕ ПРОГРАММЫ",
                         "Вы действительно хотите\n      закрыть программу?")
        print(choice)
        if choice == True:
            print('Выходим')
            self.clous_all_okna()
        if choice == False:
            print('Остаемся')

class About3(tk.Toplevel):  # Третье Окно
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x600+1000+100')
        self.title('''       ЕГЭ русский язык (Окно №3 из 3-х)''')
        self.iconbitmap(default="C:\FOTO  Python\mvoice.ico")

        self.foto3 = ImageTk.PhotoImage(file="C:\FOTO  Python\mtolstoj01.jpg")
        self.button = tk.Button(self, image=self.foto3)
        self.button.pack(padx=0, pady=0)

        self.label = tk.Label(self, text='''3. Определите предложение, в котором 
        НЕ со словом пишется СЛИТНО.''',
                              font='Times 14', foreground="#355286")
        self.label.pack(padx=10, pady=10)

        self.var3 = tk.IntVar()

        # Правильный ответ (Андрей): недоумевая Пишется слитно, потому
        # что не употребляется без НЕ
        rad8 = Radiobutton(self, text='Еще (не)распустившиеся цветки побили морозом  ',
                           variable=self.var3, value=1)
        rad8.pack(padx=10, pady=10)

        rad9 = Radiobutton(self, text='(Не)говоря ни слова, лесничий взвалил на себя       '
                                      '\nтяжелую корзину.',
                           variable=self.var3, value=2)
        rad9.pack(padx=10, pady=10)

        rad10 = Radiobutton(self, text='Андрей, (не)доумевая, вертел пакет в руках.               ',
                            variable=self.var3, value=3)
        rad10.pack(padx=10, pady=10)

        rad11 = Radiobutton(self, text='Только через семьдесят лет будут обнаружены'
                                       '\n (не)опубликованные редактором бумаги деда.        ',
                            variable=self.var3, value=4)
        rad11.pack(padx=10, pady=10)

        self.button__1 = tk.Button(self, text='''РЕЗУЛЬТАТ ТЕСТА''',
                                   font='Times 19', fg='#b60536',
                                   command=self.prov)
        self.button__1.pack(padx=0, pady=0)

        # правильные ответы
        self.button__1 = tk.Button(self, text='''ПРАВИЛЬНЫЕ ОТВЕТЫ''',
                                   font='Times 16',
                                   foreground="#355286", command=self.open_window4)
        self.button__1.pack(padx=10, pady=10)

    def prov(self):
        global a3

        if self.var3.get() == 3:
            a3 = 1
            self.rezultat()

        elif self.var3.get() < 1:
            a3 = 0
            messagebox.showinfo('''ВНИМАНИЕ''',
                                '''Сначала выберите ответ.''')

        elif self.var3.get() >= 1:
            a3 = 0
            self.rezultat()

        else:
            a3 = 0

    def rezultat(self):
        prob1 = str('                 ')
        print(self.var3.get())
        global z

        if int(a1 + a2 + a3) == 3:
            z = 1
            messagebox.showinfo('''Результат теста''', prob1 + ''' ОТЛИЧНО. 
             У ВАС 100%''')

        elif int(a1 + a2 + a3) == 2:
            z = 1
            messagebox.showinfo('''Результат теста''', prob1 + ''' ХОРОШО. 
                         У вас 66%\n''')

        elif int(a1 + a2 + a3) == 1:
            z = 1
            messagebox.showinfo('''Результат теста''', prob1 + ''' УДОВЛЕТВОРИТЕЛЬНО. 
                         У ВАС 33%\n''')

        elif int(a1 + a2 + a3) == 0:
            z = 1
            messagebox.showinfo('''Результат теста''', prob1 + ''' ПЛОХО. 
                        У ВАС 0%\n''')

        else:
            z = 0

    def open_window4(self):

        if z == 1:
            about4 = About4(self)
            about4.grab_set()

        else:
            messagebox.showinfo('''Сначала пройдите тест''')


class About(tk.Toplevel):  # Второе Окно
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('400x600+550+100')
        self.title('''       ЕГЭ русский язык (Окно №2 из 3-х)''')
        self.iconbitmap(default="C:\FOTO  Python\mvoice.ico")

        self.foto2 = ImageTk.PhotoImage(file="C:\FOTO  Python\golol02.jpg")
        self.button = tk.Button(self, image=self.foto2)
        self.button.pack(padx=0, pady=0)

        self.label = tk.Label(self, text='''2. В одном из выделенных ниже слов
         допущена ошибка в образовании
          формы  слова. Выберите 
          словосочетание с этим словом.''',
                              font='Times 14', foreground="#355286", anchor='nw',
                              justify='center')
        self.label.pack(padx=10, pady=10)

        self.var2 = tk.IntVar()

        # Правильно (с ПОЛУТОРАСТА рублями)
        rad4 = Radiobutton(self, text='   надежные СТОРОЖА            ',
                           variable=self.var2, value=4)
        rad4.pack(padx=10, pady=10)

        rad5 = Radiobutton(self, text='    ОБРЕТШИЙ покой                 ',
                           variable=self.var2, value=5)
        rad5.pack(padx=10, pady=10)

        rad6 = Radiobutton(self, text='с ПОЛУТОРАСТАМИ рублями',
                           variable=self.var2, value=6)
        rad6.pack(padx=10, pady=10)

        rad7 = Radiobutton(self, text='    несколько КЕГЛЕЙ                 ',
                           variable=self.var2, value=7)
        rad7.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Продолжить тест...", font='Times 19',
                                fg='#b60536', command=self.open_window3)
        self.button.pack(padx=10, pady=40)

    def open_window3(self):
        print(self.var2.get())

        global a2
        if self.var2.get() == 6:
            a2 = 1
            about3 = About3(self)
            about3.grab_set()


        elif self.var2.get() < 1:
            a2 = 0
            messagebox.showinfo('''ВНИМАНИЕ''',
                                '''Сначала выберите ответ.''')

        elif self.var2.get() >= 1:
            a2 = 0
            about3 = About3(self)
            about3.grab_set()

        else:
            a2 = 0


class App(tk.Tk):  # Главное Окно
    def __init__(self):
        super().__init__()

        self.geometry('400x600+100+100')
        self.title('''       ЕГЭ русский язык (Окно №1 из 3-х)''')
        self.iconbitmap(default="C:\FOTO  Python\mvoice.ico")

        self.foto1 = ImageTk.PhotoImage(file="C:\FOTO  Python\puskin01.jpg")
        self.button = tk.Button(self, image=self.foto1)
        self.button.pack(padx=0, pady=0)

        self.label = tk.Label(self, text='''                1. В одном из приведённых ниже                
        предложений НЕВЕРНО 
        употреблено выделенное слово.\n     Выберите это предложение.''',
                              font='Times 14', foreground="#355286")
        self.label.pack(padx=10, pady=10)

        self.var1 = tk.IntVar()

        # правильный ответ (2)
        # По контексту подразумевается ЗАТРУДНИТЕЛЬНЫЙ - содержащий трудности;
        # причиняющий затруднение.
        rad1 = Radiobutton(self, text='Для выполнения ремонтных работ необходимо        '
                                      '\nв целях безопасности ОГОРОДИТЬ опасную зону. ',
                           variable=self.var1, value=1)
        rad1.pack(padx=10, pady=10)

        rad2 = Radiobutton(self, text='Введение новых требований поставит'
                                      ' разработчиков\n нового проекта в ЗАТРУДНЕННОЕ положение',
                           variable=self.var1, value=2)
        rad2.pack(padx=10, pady=10)

        rad3 = Radiobutton(self, text='КОРЕННЫЕ жители полуострова живут '
                                      'обособленно\n многие века, их быт практически не изменился',
                           variable=self.var1, value=3)
        rad3.pack(padx=10, pady=10)

        # продолжить тест
        self.button = tk.Button(self, text="Продолжить тест...",
                                font='Times 19', fg='#b60536', command=self.open_window)
        self.button.pack(padx=10, pady=40)

    def selekt(self):
        print(self.var1.get())

    def open_window(self):
        print(self.var1.get())

        global a1
        if self.var1.get() == 2:
            a1 = 1
            about = About(self)
            about.grab_set()


        elif self.var1.get() < 1:
            a1 = 0
            messagebox.showinfo('''ВНИМАНИЕ''',
                                '''Сначала выберите ответ.''')

        elif self.var1.get() >= 1:
            a1 = 0
            about = About(self)
            about.grab_set()

        else:
            a1 = 0


if __name__ == "__main__":
    app = App()
    app.mainloop()
