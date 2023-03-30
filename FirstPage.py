from tkinter import END, IntVar, messagebox, ttk
from tabulate import tabulate
import customtkinter
import ConnectFile

customtkinter.set_appearance_mode("dark") #or light,system
customtkinter.set_default_color_theme("dark-blue") #or green

root = customtkinter.CTk()
root.geometry("1000x350")
root.title("CLIENT MGT")

ModeVar = IntVar()

def AppearMODE():
    if ModeVar.get():
         customtkinter.set_appearance_mode("light") #or light,system
    else:
         customtkinter.set_appearance_mode("dark") #or light,system




def insertValue():
    res = ConnectFile.conn.cursor()
    sql = "insert into client (name, age, address, tel) values('"+entry1.get()+"','"+entry2.get()+"','"+entry3.get()+"','"+entry4.get()+"')"
    res.execute(sql)
    ConnectFile.conn.commit()
    messagebox.showinfo("Inserting record","Record well inserted")


def fetch():
      res = ConnectFile.conn.cursor()
      sql = "select * from client"
      res.execute(sql)
      rows = res.fetchall()
      #print(tabulate(result, headers=["ID","NAME","AGE","ADDRESS","TELEPHONE"]))
      return rows


def display_data():
      treeview.delete(*treeview.get_children()) #to avoid displaying data multiple times
      for row in fetch():
            treeview.insert("",END, values=row)



def selectById():
      res = ConnectFile.conn.cursor()
      sql = "select * from client where id = '"+entrySearch.get()+"'"
      res.execute(sql)
      result = res.fetchone()
      entry1.insert(0, result[1])
      entry2.insert(0, result[2])
      entry3.set(result[3])
      #entry3.insert(0, result[3])
      entry4.insert(0, result[4])


def update():
      res = ConnectFile.conn.cursor()
      sql = "update client set name = '"+entry1.get()+"', age = '"+entry2.get()+"', address = '"+entry3.get()+"', tel = '"+entry4.get()+"' where id = '"+entrySearch.get()+"'"
      res.execute(sql)
      ConnectFile.conn.commit()
      messagebox.showinfo("Update record","Record well updated")

def delete():
      res = ConnectFile.conn.cursor()
      sql = "delete from client where id = '"+entrySearch.get()+"'"
      res.execute(sql)
      ConnectFile.conn.commit()
      messagebox.showinfo("Deleting record","Record is well deleted!!")




frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

searchFrame = customtkinter.CTkFrame(master=frame, width=400, height=60)
searchFrame.place(x = 0, y = 60)

tableFrame = customtkinter.CTkFrame(master=frame, width=500, height=350)
tableFrame.place(x = 400, y = 60)

switchMode = customtkinter.CTkCheckBox(master=frame, variable=ModeVar, text="mode", command=AppearMODE)
switchMode.place(x=1, y=1)

label = customtkinter.CTkLabel(master=frame, text="Client System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entrySearch = customtkinter.CTkEntry(master=searchFrame, placeholder_text="Enter a value to search", width=160)
entrySearch.place(x=30, y=14)

button = customtkinter.CTkButton(master=searchFrame, text="Search by ID", command=selectById)
button.place(x=200, y=14)
#button.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Names of client", font=("Roboto", 14))
entry1.place(x=30, y=126)
#entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Age of client", font=("Roboto", 14))
entry2.place(x=200, y=126)
#entry2.pack(pady=12, padx=10)

#entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Address of client")
#entry3.place(x=30, y=176)

entry3 = customtkinter.CTkComboBox(master=frame, values=['KIGALI CITY', 'NORTHEN', 'SOURTHERN', 'WESTERN', 'EASTERN'])
entry3.place(x=30, y=176)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Telephone of client")
entry4.place(x=200,y=176)

button = customtkinter.CTkButton(master=frame, text="Submit", command=insertValue)
button.place(x=30, y=240)
#button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Display", command=display_data)
button.place(x=200, y=240)
#button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Update", command=update)
button.place(x=30, y=280)
#button.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Delete", command=delete)
button.place(x=200, y=280)
#button.pack(pady=12, padx=10)


#checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
#checkbox.pack(pady=12, padx=10)

style = ttk.Style()
style.configure("mystle.Treeview", rowheight=80)
style.configure("mystyle.Treeview.Heading")
style.layout("mystyle.Treeview", [('mystlye.Treeview.treearea',{'sticky':'nswe'})])


treeview = ttk.Treeview(tableFrame, columns=(1,2,3,4,5), show="headings", style="mystyle.Treeview")
treeview.heading("1", text="ID")
treeview.column("1", width=130)
treeview.heading("2", text="NAME")
treeview.column("2", width=130)
treeview.heading("3", text="AGE")
treeview.column("3", width=130)
treeview.heading("4", text="ADDRESS")
treeview.column("4", width=130)
treeview.heading("5", text="TELEPHONE")
treeview.column("5", width=130)

treeview.pack()

display_data()

root.mainloop()