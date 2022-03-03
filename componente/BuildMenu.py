import tkinter as tk

import componente.CerintaA as cerA
#import componente.CerintaB as cerB
import componente.CerintaC as cerC
import componente.CerintaD as cerD
# import componente.CerintaE as cerE

valoareaSelectata = None

def buildOptionsMenu():
    """
    :return: instanta Tkinter
    """
    mainApp = tk.Tk()
    mainApp.title("Managementul unui depozit de produse cosmetice")
    mainApp.geometry("500x300")
    listaOptiuni = ["Cerinta A)",
                   "Cerinta B)",
                   "Cerinta C)",
                   "Cerinta D)",
                   "Cerinte E)"
                   ]
    global valoareaSelectata
    valoareaSelectata = tk.StringVar(mainApp) #retine optiunea selectata
    valoareaSelectata.set('Alege o optiune')
    meniuCerinte = tk.OptionMenu(mainApp, valoareaSelectata, *listaOptiuni) #instantiaza meniul pentru fereastra principala
    meniuCerinte.pack()                                                     #retine valoarea selectata,lista de optiuni drop down

    butonTrimitere = tk.Button(mainApp, text="Porneste", command=schimbaFereastra) #actiunea butonului pt fereastra principala
    butonTrimitere.pack()

    return mainApp

def schimbaFereastra(): #functia pentru schimbarea widgetului, infunctie de selectie
    if valoareaSelectata.get() == "Cerinta A)":
        cerA.executieCerintaA()
    if valoareaSelectata.get() == "Cerinta C)":
        cerC.executieCerintaC()
    if valoareaSelectata.get() == "Cerinta D)":
        cerD.executieCerintaD()