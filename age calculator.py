import datetime
import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
window.geometry("620x780")
#window.attributes("-fullscreen",True)

heading = tk.Label(window,text="age calculation",font=('times','15','bold italic'))
heading.configure(bg="brown",fg='yellow')
heading.grid( column=4,row=0)

window.title("AATTMM")


window.title(" Age Calculator App ")
name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Date")
date.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
def getInput():
    name=nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea = tk.Text(master=window,height=9,width=35)
    textArea.grid(column=1,row=6)
    textArea.configure(bg='powder blue',fg='black')
    answer = " Heyy {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END,answer)

button=tk.Button(window,text="Calculate Age",font=("Algerian"),command=getInput,bg="pink",fg="purple",activebackground="gray")
button.grid(column=1,row=5)

btn2=tk.Button(window,text="     Exit     ",font=('chiller','18','bold underline'),command=window.destroy)
btn2.configure(bg='green',fg='white',activebackground='pink')
btn2.place(x=50,y=300)


class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
image=Image.open('age.jpg')
image.thumbnail((200,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)
window.mainloop
