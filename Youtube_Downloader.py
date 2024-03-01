from tkinter import *
# # # #
window = Tk()
window.title("Youtube Downloader")
window.minsize(450,170)
window.maxsize(450,170)
bn = Button(window  , text = "Link" , bg="white")
bn.grid(row=4 , padx=30 , pady=35)
lb = Label(window , text="Enter Your Link:")
en = Entry(window , width=25)
en.grid(padx=200 )

bn2 = Button(window  , text = "Download" , bg="white")
bn2.grid(row=30 , padx=30)

window.mainloop()

