import tkinter 

window = tkinter.Tk()
window.title("my first GUI")
window.minsize(width = 500,height = 300 )

my_label = tkinter.Label(text = "my name is subham", font=("Arial",24,"bold"))
my_label.pack(side="left")

my_label["text"] = "new text"
my_label.config(text="new text")

def button_clicked():
    print("i got clicked")
    my_label.config(text="button got clicked")

button = tkinter.Button(text="click me", command = button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
