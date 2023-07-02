import tkinter
import random

fnster=tkinter.Tk()

fnster.title ( "Super Duper SCHERE;STEIN UND PAPIER (;  (o: " )

liste = ["schere","stein","papier"]

def ssp (user):

  npc = random.choice (liste)

  if user==npc:
     return "Unentschieden"

  if (user == "schere" and npc == "papier") or (user == "stein" and npc == "schere") or (user == "papier" and npc == "stein"):
    return "Gewonnen"
  else:
    return "Verloren"
  







Button = tkinter.Button(fnster, text="Schere", command=lambda: result.set(ssp('schere')))
Button.pack()

Butto = tkinter.Button(fnster, text="Stein", command=lambda: result.set(ssp('stein')))
Butto.pack()

Butt = tkinter.Button(fnster, text="Papier", command=lambda: result.set(ssp('papier')))
Butt.pack()

result=tkinter.StringVar()

label=tkinter.Label(fnster, textvariable=result)
label.pack()


fnster.mainloop()
