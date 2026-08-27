from tkinter import Tk, Label

root = Tk()

#To crete someting in tk we first define/create it then put it on screen

#creating
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is ...")

#shoving it onto the screen
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=2, column=1)
#yLabel1.grid()
#packs make the output window as large as need by the content in it


#we can do both creting and shoving together like
myLabel3 = Label(root, text="Ram Lali Verma").grid(row=1, column=3)

for i in range(12) :
    for j in range(13) :
        myLabel4 = Label(root, text=".").grid(row=i, column=j)
        
#a loop which dedects all the things happening on the screen
root.mainloop()
