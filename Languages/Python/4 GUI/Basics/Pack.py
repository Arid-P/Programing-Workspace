from tkinter import Tk, Label

root = Tk()

#To crete someting in tk we first define/create it then put it on screen

#creating
myLabel = Label(root, text="Hello World!")

#shoving it onto the screen
myLabel.pack()
#packs make the output window as large as need by the content in it 

#a loop which dedects all the things happening on the screen
root.mainloop()

