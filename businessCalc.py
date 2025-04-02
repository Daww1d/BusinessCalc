# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext

# Window Setup
window = tk.Tk()
window.geometry("600x400")
window.title("Business Calculator")
window.iconbitmap("image.ico")
window.minsize(1200, 600)

# Variables
helpWords = [
    "# Help Section - Business Calculator",
    "## Overview",
    "The Business Calculator is a simple application designed to help businesses track their quarterly costs and revenues.",
    "It allows users to input financial data, update records, and view an overview of stored information.",
    "The application is built using Python's Tkinter library for a user-friendly graphical interface.",
    "## Navigation",
    "The application consists of three main sections:",
    "1. Update - Enter and update financial data.",
    "2. Overview - View a summary of stored data.",
    "3. Help - Access this guide for assistance.",
    "To switch between sections, use the navigation buttons in the header.",
    "## Features",
    "### 1. Adding Data",
    "- Navigate to the Update section by clicking the update button.",
    "- Enter the following details:",
    "  - Quarter: Specify the financial quarter (e.g., Q1, Q2, Q3, Q4).",
    "  - Costs: Input the total cost for the quarter.",
    "  - Revenue: Input the total revenue for the quarter.",
    "- Click the Add Data button to save the information.",
    "- A message will confirm whether the update was successful or if there was an error.",
    "### 2. Updating the Table",
    "- Click the Update Table button to refresh the displayed data.",
    "- The table will show all stored quarterly entries with formatted cost and revenue values.",
    "### 3. Viewing the Overview",
    "- Click the Overview button to access a summarized view of all financial data.",
    "### 4. Help Section",
    "- Click the Help button to return to this help guide.",
    "## Error Handling",
    "- If invalid or empty entries are submitted, an error message will appear.",
    "- Ensure all fields contain valid numerical data before adding an entry.",
    "## Troubleshooting",
    "- If the table does not update, click the Update Table button.",
    "- If the application is unresponsive, close and restart it.",
    "- Make sure all input fields contain valid numbers before adding data.",
    "For further assistance, contact support or refer to the application's documentation.",
]

data = []
profit = []
roi = []

totalRoi = 0
netProfit = 0

#style = ttk.Style()
#style.theme_use("xpnative")
window.tk.call("source", "Azure/azure.tcl")
window.tk.call("set_theme", "dark")

# Frames
# --------Main frames-------
header = ttk.Frame(window, height=50, borderwidth=10, relief=tk.SOLID)
update = ttk.Frame(window)
update.pack_propagate(False)
overview = ttk.Frame(window)
overview.pack_propagate(False)
help = ttk.Frame(window)
help.pack_propagate(False)
# ----------subframes--------
# update page
updateLeft = ttk.Frame(update)
updateRight = ttk.Frame(update)
updateBar = ttk.Frame(updateLeft)


# Frame content
# Header frames
logoLabel = ttk.Label(header, text="Business Calculator", font="Calibri 15 bold")
updateButton = ttk.Button(header, text="Update", command=lambda: changeTab(update))
overviewButton = ttk.Button(header, text="Overview", command=lambda: changeTab(overview))
helpButton = ttk.Button(header, text="Help", command=lambda: changeTab(help))
# update frame
quaterLabel = ttk.Label(updateLeft, text="Quater :", font="Calibri 15 bold")
costLabel = ttk.Label(updateLeft, text="Cost :", font="Calibri 15 bold")
salesLabel = ttk.Label(updateLeft, text="Sales :", font="Calibri 15 bold")

quaterSelect = ttk.Entry(updateLeft, font=("calibre", 20, "normal"))
costInput = ttk.Entry(updateLeft, font=("calibre", 20, "normal"))
saleInput = ttk.Entry(updateLeft, font=("calibre", 20, "normal"))
addDataButton = ttk.Button(updateBar, text="Add Data", command=lambda: updateData())

errorDisplay = ttk.Label(updateBar, text="Please Enter Data Above")
# Table
mainTable = ttk.Treeview(updateRight, columns=("Quater", "Costs", "Revenue"), show="headings")
mainTable.heading("Quater", text="Quater")
mainTable.heading("Costs", text="Cost")
mainTable.heading("Revenue", text="Revenue")
roiDisplay = ttk.Label(updateRight, text="ROI")
profitDisplay = ttk.Label(updateRight, text="0")
profitLabel = ttk.Label(updateRight, text="Profit :")
roiLabel = ttk.Label(updateRight, text="ROI")

# help frame
helpInfo = scrolledtext.ScrolledText(help)
helpInfo.insert(tk.INSERT," Help Section - Business Calculator\n Overview\nThe Business Calculator is a simple application designed to help businesses track their quarterly costs and revenues.\nIt allows users to input financial data, update records, and view an overview of stored information.\nThe application is built using Python's Tkinter library for a user-friendly graphical interface.\n\n Navigation\nThe application consists of three main sections:\n1. Update - Enter and update financial data.\n2. Overview - View a summary of stored data.\n3. Help - Access this guide for assistance.\nTo switch between sections, use the navigation buttons in the header.\n\n Features\n 1. Adding Data\n- Navigate to the Update section by clicking the Update button.\n- Enter the following details:\n  - Quarter: Specify the financial quarter (e.g., Q1, Q2, Q3, Q4).\n  - Costs: Input the total cost for the quarter.\n  - Revenue: Input the total revenue for the quarter.\n- Click the Add Data button to save the information.\n- A message will confirm whether the update was successful or if there was an error.\n\n 2. Updating the Table\n- Click the Update Table button to refresh the displayed data.\n- The table will show all stored quarterly entries with formatted cost and revenue values.\n\n 3. Viewing the Overview\n- Click the Overview button to access a summarized view of all financial data.\n\n 4. Help Section\n- Click the Help button to return to this help guide.\n\n Error Handling\n- If invalid or empty entries are submitted, an error message will appear.\n- Ensure all fields contain valid numerical data before adding an entry.\n\n Troubleshooting\n- If the table does not update, click the Update Table button.\n- If the application is unresponsive, close and restart it.\n- Make sure all input fields contain valid numbers before adding data.\n\nFor further assistance, contact support or refer to the application's documentation.",)
helpInfo.configure(state="disabled")

# overview frame

# Deafult Pack
# Pack header
header.pack(fill="x")
logoLabel.pack(side="left", padx=2)
helpButton.pack(side="right",padx=2)
overviewButton.pack(side="right",padx=2)
updateButton.pack(side="right",padx=2)

# pack update
updateLeft.pack(side="left", fill="both", expand=True, padx=40,pady=10)
updateRight.pack(side="right", fill="both", expand=True,padx=40,pady=10)
updateBar.pack(side="bottom", fill="both", expand=True,padx=40,pady=10)
# left side
quaterLabel.pack(fill="both", expand=True)
quaterSelect.pack(fill="both", expand=True, padx=40, pady=30)
costLabel.pack(fill="both", expand=True)
costInput.pack(fill="both", expand=True, padx=40, pady=30)
salesLabel.pack(fill="both", expand=True)
saleInput.pack(fill="both", expand=True, padx=40, pady=30)
addDataButton.pack(side="left", expand=True)
errorDisplay.pack(side="right", expand=True)
# right side
mainTable.pack(fill="both", expand=True, padx=30, pady=30)
roiDisplay.pack(side="left", expand=True)
profitDisplay.pack(side="right", expand=True)
roiLabel.pack(side="left", expand=True)
profitLabel.pack(side="right", expand=True)

# pack help
helpInfo.pack(side="right", fill="both", expand=True)




# Fucntions
def changeTab(tab=update):
    update.pack_forget()
    overview.pack_forget()
    help.pack_forget()
    tab.pack(fill="both", expand=True)


def calRoi():
    for entry in data:
        currentRoi = 0
        currentRoi = (int(entry[2])- int(entry[1])) / int(entry[1]) * 100
        #roi.append(currentRoi)
        roiLabel.config(text=totalRoi)

def totalRoi():
    global totalRoi
    for item in roi:
        totalRoi += item

    return totalRoi

def totalProfit():
    global netProfit
    netProfit = 0
    print(profit)
    for item in profit:
        netProfit += int(item)

    profitDisplay.config(text=netProfit)

def calcProfit():
    global profit
    for entry in data:
        currentProfit = 0
        currentProfit = int(entry[2]) - int(entry[1])
        profit.append(currentProfit)
    totalProfit()
    profit = []

def validEntry(entry):
    for item in entry:
        if item.isnumeric() == True:
            pass
        else:
            return False # if even one value isnt number stops loop 
    return True

def updateData():  # Adds data in inputs to store
    if validEntry([quaterSelect.get(), costInput.get(), saleInput.get()]):
        errorDisplay.config(text="Update Successful !")
        data.append([quaterSelect.get(), costInput.get(), saleInput.get()])
        updateTable()
    else:
        errorDisplay.config(text="Invalid Input")

    #calRoi()
    calcProfit()

def updateTable():
    # removes previous data in table
    for item in mainTable.get_children():
        mainTable.delete(item)
    for item in data:
        # Adds values to table from data
        mainTable.insert(
            parent="", index=tk.END, values=(item[0], f"£ {item[1]}", f"£ {item[2]}"))


# run
changeTab()

window.mainloop()
