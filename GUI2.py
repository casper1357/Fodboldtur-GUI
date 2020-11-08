import pickle
from tkinter import *
from tkinter import messagebox, ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk, Image
root = Tk()
filename = 'betalinger.pk'
fodboldtur = {}

class Tkinter:
    def __init__(self):
        self.moneygoal = 4500 #
        pass

    def rootwindow(self):
        root.geometry("400x400")
        root.title("FODBOLDTUR")
        root.iconbitmap('cat.ico')
        shrek = ImageTk.PhotoImage(Image.open("shrek.jpg"))
        shreklabel = Label(root, image=shrek)
        shreklabel.image = shrek
        shreklabel.pack()
        self.afslutBtn = Button(root, text="Afslut program", command=self.afslut, fg="royal blue").pack(side=TOP)
        self.progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
        self.progressbar.pack(side=BOTTOM)
        self.rootmenubar()

    def rootmenubar(self):
        self.root_menu_bar = Menu(root)
        root.config(menu=self.root_menu_bar)
        self.root_graphs_menu = Menu(self.root_menu_bar)
        self.root_dict_menu = Menu(self.root_menu_bar)
        self.root_indbetal_menu = Menu(self.root_menu_bar)
        self.root_menu_bar.add_cascade(label="Dict", menu=self.root_dict_menu)
        self.root_dict_menu.add_command(label="Print dict", command=self.printdictwindow)
        self.root_dict_menu.add_separator()
        self.root_dict_menu.add_command(label="Reset values", command=self.resetvaluesindictwindow)
        self.root_dict_menu.add_separator()
        self.root_dict_menu.add_command(label="Tilføj navn", command=self.additemtodictwindow)
        self.root_dict_menu.add_separator()
        self.root_dict_menu.add_command(label="Fjern navn", command=self.popdictwindow)
        self.root_menu_bar.add_cascade(label="Indbetaling", menu=self.root_indbetal_menu)
        self.root_indbetal_menu.add_command(label="Indbetal", command=self.indbetalwindow)
        self.root_indbetal_menu.add_separator()
        self.root_indbetal_menu.add_command(label="Mindstbetalende", command=self.mindstbetalendewindow)
        self.root_menu_bar.add_cascade(label="Grafer", menu=self.root_graphs_menu)
        self.root_graphs_menu.add_command(label="Cirkeldiagram", command=self.graphwindow)

    def printdictwindow(self):
        self.printdictwindow = Toplevel()
        self.printdictwindow.geometry("400x300")
        self.printdictwindow.title('Print dict window')
        self.printdictwindow.iconbitmap('cat.ico')
        self.printdict()

    def printdict(self):
        rownumber = 0
        columnnumber = 0
        for key, value in fodboldtur.items():
            columnnumber += 1
            name = Entry(self.printdictwindow, fg="royal blue")
            name.grid(row=rownumber, column=columnnumber)
            name.insert(END, (str(key) + ": " + str(value) + "kr"))
            if columnnumber >= 3:
                columnnumber = 0
                rownumber += 1
        self.samlet = sum(fodboldtur.values())
        Label(self.printdictwindow, text="Samlet: " + str(self.samlet) + " kr", fg="royal blue").grid(row=rownumber+2, column=1, columnspan = 3)
        backBtn = Button(self.printdictwindow, text="Gå tilbage til menu", command=self.printdictwindow.destroy, fg="royal blue").grid(row=(rownumber + 1), column=1, columnspan = 3)

    def resetvaluesindictwindow(self):
        self.resetwindow = Toplevel()
        self.resetwindow.geometry("400x150")
        self.resetwindow.title('Reset Window')
        self.resetwindow.iconbitmap('cat.ico')
        self.resetvaluesindict()

    def resetvaluesindict(self):
        rownumber = 0
        columnnumber = 0
        for values in fodboldtur.copy():
            fodboldtur[values] = 0
        for key, value in fodboldtur.items():
            columnnumber += 1
            name = Entry(self.resetwindow, fg="royal blue")
            name.grid(row=rownumber, column=columnnumber)
            name.insert(END, (str(key) + ": " + str(value) + "kr"))
            if columnnumber >= 3:
                columnnumber = 0
                rownumber += 1
        label = Label(self.resetwindow, text="Alle values er nu reset!", fg="royal blue").grid(row=rownumber + 1 , column = 1, columnspan=3)
        backBtn = Button(self.resetwindow, text="Gå tilbage til menu", command=self.resetwindow.destroy,
                         fg="royal blue").grid(row=rownumber + 2 , column=1, columnspan=3)

    def additemtodictwindow(self):
        self.additemtodictwindow = Toplevel()
        self.additemtodictwindow.geometry("400x400")
        self.additemtodictwindow.title('Add item to dict')
        self.additemtodictwindow.iconbitmap('cat.ico')
        Label(self.additemtodictwindow, text="Tilføj et navn til dicten her:", fg="royal blue").pack()
        self.addName = Entry(self.additemtodictwindow)
        self.addName.pack()
        self.submitBtn = Button(self.additemtodictwindow, text="Submit", command=self.additemtodict, fg="royal blue").pack()
        backBtn = Button(self.additemtodictwindow, text="Gå tilbage til menu", command=self.additemtodictwindow.destroy, fg="royal blue").pack()

    def additemtodict(self):
        name = self.addName.get()
        if len(name) != 0:
            fodboldtur[name] = 0
            addednamelabel = Label(self.additemtodictwindow, text=(name + " er blevet tilføjet til fodboldturdicten"), fg="royal blue").pack()
            self.dumpdict()
        else:
            messagebox.showinfo("Error", "WARNING! Du har ikke skrevet et navn ind")

    def popdictwindow(self):
        self.popdictwindow = Toplevel()
        self.popdictwindow.geometry("400x200")
        self.popdictwindow.title('Pop dict')
        self.popdictwindow.iconbitmap('cat.ico')
        Label(self.popdictwindow, text="Fjern et navn fra dicten her:", fg="royal blue").pack()
        self.clickedpopdict = StringVar()
        self.clickedpopdict.set("Navne")
        self.droppopdict = OptionMenu(self.popdictwindow, self.clickedpopdict, *fodboldtur.keys())
        self.droppopdict.config(fg="royal blue")
        self.droppopdict.pack()
        self.btnpopdict = Button(self.popdictwindow, text="Submit", command=self.popdict, fg="royal blue").pack()
        backBtn = Button(self.popdictwindow, text="Gå tilbage til menu", command=self.popdictwindow.destroy,
                              fg="royal blue").pack()

    def popdict(self):
        name = self.clickedpopdict.get()
        fodboldtur.pop(name, None)
        removednamelabel = Label(self.popdictwindow, text=(name + " er blevet fjernet fra fodboldturdicten"), fg="royal blue").pack()
        self.dumpdict()

    def indbetalwindow(self):
        self.indbetalwindow = Toplevel()
        self.indbetalwindow.geometry("300x150")
        self.indbetalwindow.title('Indbetaling')
        self.indbetalwindow.iconbitmap('cat.ico')
        self.e = Entry(self.indbetalwindow)
        self.e.pack()
        self.bIndbetal = Button(self.indbetalwindow, text="Submit", command=self.indbetal, fg="royal blue").pack()
        self.clicked = StringVar()
        self.clicked.set("Navne")
        self.drop = OptionMenu(self.indbetalwindow, self.clicked, *fodboldtur.keys())
        self.drop.config(fg="royal blue")
        self.drop.pack()
        backBtn = Button(self.indbetalwindow, text="Gå tilbage til menu", command=self.indbetalwindow.destroy, fg="royal blue").pack()
        if sum(fodboldtur.values()) > self.moneygoal:
            Label(self.indbetalwindow, text="I har mere end nok penge til fodboldturen!", fg="royal blue").pack()

    def indbetal(self): #Her er der en hel masse try/excepts og if else/statements for at sikre at programmet ikke får errors
        self.person = self.clicked.get()
        self.betalt = self.e.get()
        if self.person != "Navne":
            if len(self.betalt) == 0:
                messagebox.showinfo("Beløb Error", "WARNING! Du har ikke skrevet noget beløb ind")
            else:
                try:
                    comma = ","
                    if comma in self.betalt:
                        messagebox.showinfo("Comma Error", "WARNING! Brug punktum i stedet for komma tak!")
                    else:
                        if float(self.betalt) < 0:
                            self.cats()
                        else:
                            fodboldtur[str(self.person)] += float(self.betalt)
                            label = Label(self.indbetalwindow, text=(self.person + " har tilføjet " + self.e.get() + " kroner!")).pack()
                            print(fodboldtur[str(self.person)])
                            self.progressbar['value'] = sum(fodboldtur.values()) / (self.moneygoal / 100) #Progressbaren er 100 i alt så derfor skal pengemål divideres med 100
                            self.cats()
                except:
                    messagebox.showinfo("Datatype Error", "WARNING! Dette er ikke en float!")
        else:
            messagebox.showinfo("Person Error", "WARNING! Du har ikke valgt personen som betaler")

    def mindstbetalendewindow(self): # virker pt ikke
        self.mindstbetalendewindow = Toplevel()
        self.mindstbetalendewindow.geometry("400x400")
        self.mindstbetalendewindow.title('Mindstbetalende')
        self.mindstbetalendewindow.iconbitmap('cat.ico')
        self.mindstbetalende = sorted(fodboldtur.items(), key=lambda kv: (kv[1], kv[0]))
        print(self.mindstbetalende)
        self.mindstbetalt = self.mindstbetalende[0][1]
        self.tremindstbetalende = [kv for kv in self.mindstbetalende[:3]]
        Label(self.mindstbetalendewindow, text="Den/dem som har betalt mindst er:").pack()
        for kv in self.mindstbetalende: #William Bauer hjalp mig med at få alle navnene til at vise sig hvis flere end 3 havde betalt det samme beløb og det var dem som havde betalt mindst
            if kv[1] != self.mindstbetalt:
                Label(self.mindstbetalendewindow, text="De tre personer som har betalt mindst er: \n " + str(self.tremindstbetalende)).pack()
            if kv[1] == self.mindstbetalt:
                Label(self.mindstbetalendewindow, fg="RED", text=kv[0]).pack()
            else:
                break
        backBtn = Button(self.mindstbetalendewindow, text="Gå tilbage til menu", command=self.mindstbetalendewindow.destroy,
                              fg="royal blue").pack(side=BOTTOM)

    def graphwindow(self):
        self.graphwindow = Toplevel()
        self.graphwindow.geometry("600x500")
        self.graphwindow.title('Grafer')
        self.graphwindow.iconbitmap('cat.ico')
        backBtn = Button(self.graphwindow, text="Gå tilbage til menu", command=self.graphwindow.destroy,
                              fg="royal blue").pack(side=BOTTOM)
        self.piechart()


    def piechart(self): #Pie charten navnene bliver lidt meget lagt ovenpå hinanden så de er svære at læse og det vidste jeg ikke helt lige hvordan man skulle fixe.
        Label(self.graphwindow, text="Hvor meget personerne har betalt i forhold til hinanden i procent").pack()
        self.samlet = sum(fodboldtur.values())
        if float(self.samlet) != 0:
            fig = Figure(figsize=(6, 5), dpi=100)
            subplot = fig.add_subplot(111)
            subplot.pie(fodboldtur.values(), labels=fodboldtur.keys(), autopct='%1.1f%%', shadow=True,startangle=90)
            subplot.axis('equal')
            pie = FigureCanvasTkAgg(fig, self.graphwindow)
            pie.get_tk_widget().pack()
            plt.show()
        else:
            messagebox.showinfo("ERROR", "WARNING! Ingen af personer har betalt noget")

    def dumpdict(self):
        outfile = open(filename, 'wb')
        pickle.dump(fodboldtur, outfile)

    def afslut(self):
        outfile = open(filename, 'wb')
        pickle.dump(fodboldtur, outfile)
        outfile.close()
        print("Programmet er afsluttet!")
        quit()

    def cats(self):
        self.catWindow = Toplevel()
        self.catWindow.geometry("400x400")
        self.catWindow.iconbitmap("cat.ico")
        if float(self.e.get()) < 0:
            self.catWindow.geometry("1980x1080")
            cat_img1 = ImageTk.PhotoImage(Image.open("disgusted.jpg"))
            self.catWindow.title("dont steal man")
        elif float(self.e.get()) >= 0 and float(self.e.get()) <= 200:
            self.catWindow.geometry("400x400")
            cat_img1 = ImageTk.PhotoImage(Image.open("sad.png"))
            self.catWindow.title("bruh")
        elif float(self.e.get()) >= 200 and float(self.e.get()) <= 300:
            self.catWindow.geometry("400x400")
            cat_img1 = ImageTk.PhotoImage(Image.open("yoink.jpg"))
            self.catWindow.title(":o")
        elif float(self.e.get()) > 300 and float(self.e.get()) <= 600:
            self.catWindow.geometry("400x400")
            cat_img1 = ImageTk.PhotoImage(Image.open("happy.jpg"))
            self.catWindow.title("noice")
        else:
            self.catWindow.geometry("400x400")
            cat_img1 = ImageTk.PhotoImage(Image.open("reallyhappy.jpg"))
            self.catWindow.title("*happyface*")
        catlabel = Label(self.catWindow, image=cat_img1)
        catlabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.catWindow.mainloop()

infile = open(filename, 'rb')
fodboldtur = pickle.load(infile)
infile.close()
tkinterclass = Tkinter()
tkinterclass.rootwindow()
root.mainloop()