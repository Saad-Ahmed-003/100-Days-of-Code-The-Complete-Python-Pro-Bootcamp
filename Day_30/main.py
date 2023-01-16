import tkinter

window = tkinter.Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)

# label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold "))
my_label.pack()




window.mainloop()
