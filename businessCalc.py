# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import math
import matplotlib


# Window Setup
window = tk.Tk()
window.geometry("600x400")
window.title("Business Calculator")
window.iconbitmap("image.ico")
window.minsize(600,400)

#Variables
data = []




# Frames
#--------Main frames-------
header = ttk.Frame(window, height=50, borderwidth=10, relief=tk.GROOVE)
update = ttk.Frame(window, borderwidth=10, relief=tk.GROOVE)
update.pack_propagate(False)
overview = ttk.Frame(window, borderwidth=10, relief=tk.GROOVE)
overview.pack_propagate(False)
help = ttk.Frame(window, borderwidth=10, relief=tk.GROOVE)
help.pack_propagate(False)
#----------subframes--------
#update page
updateLeft = ttk.Frame(update, borderwidth=10, relief=tk.GROOVE)
updateRight = ttk.Frame(update, borderwidth=10, relief=tk.GROOVE)



#Frame content
#Header frames
logoLabel = ttk.Label(header, text="Business Calculator", font="Calibri 15 bold")
updateButton = ttk.Button(header, text="Update", command=lambda: changeTab(update))
overviewButton = ttk.Button(header, text="Overview", command=lambda: changeTab(overview))
helpButton = ttk.Button(header, text="Help", command=lambda: changeTab(help))
#update frame
quaterSelect = ttk.Entry(updateLeft)
costInput = ttk.Entry(updateLeft)
saleInput = ttk.Entry(updateLeft)
updateTableButton = ttk.Button(updateLeft, text="Update Table", command=lambda: updateData())
#Table
mainTable = ttk.Treeview(updateRight, columns= ("Quater", "Costs", "Revenue"), show= "headings")
mainTable.heading("Quater", text="Quater")
mainTable.heading("Costs", text="Cost")
mainTable.heading("Revenue", text="Revenue")
#help frame

#overview frame

#Deafult Pack
#Pack header
header.pack(fill="x")
logoLabel.pack(side="left")
helpButton.pack(side="right")
overviewButton.pack(side="right")
updateButton.pack(side="right")

#pack update
updateLeft.pack(side="left", fill="both", expand=True)
updateRight.pack(side="right", fill="both", expand=True)
#left side
quaterSelect.pack()
costInput.pack()
saleInput.pack()
updateTableButton.pack()
#right side 
mainTable.pack(fill="both",expand=True, padx=30, pady=30)


#Fucntions
def changeTab(tab=update):
    update.pack_forget()
    overview.pack_forget()
    help.pack_forget()
    tab.pack(fill="both", expand=True)

def calRoi():
    pass

def updateData():
    data.append([quaterSelect.get(), costInput.get(), saleInput.get()])
    updateTable()

def updateTable():
    for item in mainTable.get_children():
        mainTable.delete(item)
    for item in data:
        mainTable.insert(parent="", index=tk.END, values= item)

# run
changeTab()

window.mainloop()
