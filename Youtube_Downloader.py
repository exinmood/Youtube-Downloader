### used tk for creating app ###
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import pytube

### size and title ###
window = Tk()
window.title("Youtube Downloader")
window.minsize(450,175)
window.maxsize(450,175)

### Functions ###
def one():
    directory = askdirectory(initialdir="" , title="Save")
    d_var.set(directory)
    print (directory)

def tow():
    messagebox.showinfo(title="Can Not!" , message="this app is not download video\n(in next update)")
    
   

d_var = StringVar()

lb1 = Label(window , text='    Link    :' , fg='black' , font=100 , bg='white')
lb2 = Label(window , text='Directory:' , font=100 , bg='white')
en1 = Entry(window , width=20 , font=60 )
en2 = Entry(window , width=20 , font=60 , textvariable=d_var)
bn1 = Button(window , text='Open' , fg='white' , bg='black' , command=one)
bn2 = Button(window , text='Download', bg='green' , font=100 , height=2, width=13 , command=tow)

lb1.grid(padx=10, pady=4 , sticky='w')
lb2.grid(padx=10, pady=10)
en1.grid(row=0 , column=1 , padx=10 , pady=15)
en2.grid(row=1 , column=1 ,  padx=10)
bn1.grid(row=2 , column=0 , pady=26 , sticky="s")
bn2.grid(pady=0 , row=2, column=1 )

window.mainloop()

