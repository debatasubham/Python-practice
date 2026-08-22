from tkinter import *

#creating window
window = Tk()
window.title("widget Example")
window.minsize(width =500 , height = 500)
window.config(bg="yellow")
#label
label = Label(text = "this is old text")
label.config(text="this is new text")
label.pack()

#Buttons
def action():
    print("do something")

#calls action() when pressed
button = Button(text="click Me",command=action)
button.pack()

#entries
entry = Entry(width=30)
#add some text to begin with
entry.insert(END , string = "some text to begin with.")
#gets text in entry
print(entry.get())
entry.pack()

#text
text = Text(height=5,width=30)
#puts cursor in textbox
text.focus()
#add some text to begin with
text.insert(END,"example of multiline text entry.")
#gets current value in textbox at line 1, character 0
print(text.get("1.0",END))
text.pack()








window.mainloop()