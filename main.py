# Planning Doc - https://www.figma.com/file/gFAKggjgcKjdOdezbFK7yo/GUI-Layout?node-id=0%3A1
# Helpful Links - https://docs.google.com/document/d/1toyieKYiQkFsAFKO-ngZMJfX_TGfkJNv-bmoDEP0Elw/edit
# Rubric - https://docs.google.com/document/d/1Ms6KoPEgk0HrYWwik8MlkYdgCNWlRwvZgAsRTJZ7myE/edit

#Resources - https://www.askpython.com/python-modules/tkinter/age-calculator
from datetime import date
today = date.today()
 
def exit():
    window.destroy()
def get_ageYears():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("600x600")
window.config(bg="orange")
window.resizable(width=False,height=False)
window.title('Age Calculator!')
 
l1 = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="white",bg="orange")
l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year. (dd/mm/yyyy)",fg="white",bg="orange")
 
l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="white",bg="orange")
l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="white",bg="orange")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="white",bg="orange")
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)
e3=tk.Entry(window,width=5)
e4=tk.Entry(window,width=5)
e5=tk.Entry(window,width=5)
 
b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=get_ageYears)
 
l3 = tk.Label(window,text="Your age in years is: ",font=('Arial',12,"bold"),fg="white",bg="orange")
t1=tk.Text(window,width=5,height=0,state="disabled")

l4 = tk.Label(window,text="Your age in months is: ",font=('Arial',12,"bold"),fg="white",bg="orange")
t1=tk.Text(window,width=5,height=0,state="disabled")

l5 = tk.Label(window,text="Your age in days is: ",font=('Arial',12,"bold"),fg="white",bg="orange")
t1=tk.Text(window,width=5,height=0,state="disabled")

b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)
 
l1.place(x=70,y=5)
l2.place(x=10,y=40)
l3.place(x=50,y=200)
l4.place(x=50,y=250)
l5.place(x=50,y=300)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
e4.place(x=270,y=250)
e5.place(x=250,y=300)
b1.place(x=100,y=450)
b2.place(x=300,y=450)
t1.place(x=240,y=203)
 
window.mainloop()