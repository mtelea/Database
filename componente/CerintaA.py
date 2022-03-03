import tkinter
import tkinter as tk
from tkinter import ttk
from componente.SQLUtils import getAllTables, getAllColumnsFromTable, selectAllFromOrderBy

class CerintaA:
    def __init__(self):
        self.mainApp = tk.Toplevel() #face noua fereastra sa apara peste cea precedenta
        self.mainApp.title("Cerinta A")
        self.mainApp.geometry("800x400")
        self.mainApp.resizable(0, 0)
        self.__drawGrid__()

    def __drawGrid__(self):
        labelCerinta = ttk.Label(self.mainApp, text="Listare continut cu posibilitatea\n de sortare (toate tabelele)")
        labelCerinta.place(x=10, y=10)

        labelInfoColoane = ttk.Label(self.mainApp, text="Coloanele dupa care poti sorta")
        labelInfoColoane.place(x=210, y=10)

    def getApp(self):
        return self.mainApp


def executieCerintaA():
    cerintaA = CerintaA() #instantiaza obiect de tip CerintaA
    app = cerintaA.getApp() #widget nou
    listTables = drawTableList(app) #cream in widgetul curent listboxul cu tabele
    columnList = tk.Listbox(app, selectmode='single', exportselection=False) #listbox coloane
    columnList.place(x=240, y=100)
    listTables.bind('<<ListboxSelect>>', lambda event: drawColumnList(app, listTables, columnList)) #legatura dintre tabel coloana, selectam tabel, apar coloanele acestuia in listbox
    tabelDiv = tk.Frame(app, width = 380, height=370) #frame tabel
    tabelDiv.place(x=410, y=10)
    tv = ttk.Treeview(tabelDiv, show="headings", height = "10") #instantiem widget treeview care retine o lista de obiecte, fiecare avand mai multe coloane
    scrollX = ttk.Scrollbar(tabelDiv, orient=tk.HORIZONTAL, command=tv.xview)
    scrollY = ttk.Scrollbar(tabelDiv, orient=tk.VERTICAL, command=tv.yview)
    tv.configure(xscrollcommand=scrollX.set)
    tv.configure(yscrollcommand=scrollY.set)
    tabelDiv.pack_propagate(0)
    scrollX.pack(side="bottom", fill="x")
    scrollY.pack(side="right", fill="y")
    tv.pack(side="top", fill="both", expand=True)
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    butonAsc = tk.Button(app,text='Crescator', command=lambda: drawTableTreeView(tv, listTables.get(listTables.curselection()),
                                                                             columnList.get(columnList.curselection()),
                                                                             True)).place(x=230,y=300)
    butonDesc = tk.Button(app, text='Descrescator', command=lambda: drawTableTreeView(tv, listTables.get(listTables.curselection()),
                                                                             columnList.get(columnList.curselection()),
                                                                             False)).place(x=300, y=300)
    app.mainloop()

def drawTableTreeView(tv, table, orderBy, asc):
    header, results = selectAllFromOrderBy(table,orderBy,asc) #header-coloanele tabelului , results-array de "linii din tabel"
    #print(len(results[0]))
    tv.delete(*tv.get_children())
    tv['columns'] = list(range(len(results[0])))
    columnsName = [i[0] for i in header]
    for i in range(len(results[0])):
        tv.heading(i, text=columnsName[i]) #heading pt tabel, luate din parcurgerea header-ului
    for row in results:
        tv.insert('', tk.END, values=row) #inseram fiecare rand in tabel

def drawTableList(mainApp):
    listTables = tk.Listbox(mainApp, selectmode='single', exportselection=False) #instantiem un obiect de tip listbox
    listTables.place(x=40, y=100) #il plasam
    allTables = getAllTables() #obtinem array ul de tabele cu ajutorul functiei din mysqlutils
    i = 0
    for table in allTables:
        i += 1
        listTables.insert(i, table) #parcurgem array ul de tabele si inseram in listbox la pozitia i
    return listTables #returnam listboxul cu tabele

def drawColumnList(mainApp,listTables,columnList):
    try:
        tabelSelectat = listTables.get(listTables.curselection())
    except tkinter.TclError as e:
        return
    allColumns = getAllColumnsFromTable(tabelSelectat[0])
    columnList.delete(0, tk.END)
    i = 0
    for column in allColumns:
        i += 1
        columnList.insert(i, column[3])

