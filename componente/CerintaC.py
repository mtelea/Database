import tkinter
import tkinter as tk
from tkinter import ttk
from componente.SQLUtils import solveCerintaC

class CerintaC:
    def __init__(self):
        self.mainApp = tk.Toplevel()
        self.mainApp.title("Cerinta C")
        self.mainApp.geometry("800x400")
        self.mainApp.resizable(0, 0)

    def getApp(self):
        return self.mainApp

def executieCerintaC():
    cerintaC = CerintaC()
    app = cerintaC.getApp()
    tabelDiv = tk.Frame(app, width=780, height=380)
    tabelDiv.place(x=10, y=10)
    tv = ttk.Treeview(tabelDiv, show="headings", height="10")
    scrollX = ttk.Scrollbar(tabelDiv, orient=tk.HORIZONTAL, command=tv.xview)
    scrollY = ttk.Scrollbar(tabelDiv, orient=tk.VERTICAL, command=tv.yview)
    tv.configure(xscrollcommand=scrollX.set)
    tv.configure(yscrollcommand=scrollY.set)
    tabelDiv.pack_propagate(0)
    scrollX.pack(side="bottom", fill="x")
    scrollY.pack(side="right", fill="y")
    tv.pack(side="top", fill="both", expand=True)

    header, results = solveCerintaC()
    tv.delete(*tv.get_children())
    tv['columns'] = list(range(len(results[0])))
    columnsName = [i[0] for i in header]
    for i in range(len(results[0])):
        tv.heading(i, text=columnsName[i])
    for row in results:
        tv.insert('', tk.END, values=row)

    app.mainloop()
