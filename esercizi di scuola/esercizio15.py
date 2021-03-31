import tkinter as tk
from typing import Text #importing module
fv = 0
sv =0

window = tk.Tk() #starting the windows
window.title = 'Multiplication' #setting the title
mainframe = tk.Frame( #setting the main frame in which the layout is staying
    window
)
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S')) #fixing the grids in the case i want to use them laters
#probably not :)


label1  = tk.Label( #declaring the first label
    mainframe,
    text='insert one number:'
)

fv_entry = tk.Entry(mainframe) #the entry
fv  = fv_entry.get()



label2 = tk.Label( #declaring the second label
    mainframe,
    text = 'insert the second number:'
)
sv_entry = tk.Entry(mainframe) #getting the second entry
sv = sv_entry.get() #useless, i will remove in a further update


label3 = tk.Label( #declaring the second label
    mainframe,
    text = 'Result'
)

def multiplicationpopup(): #--> where we input v1 and v2 as fv and sv
    global label3
    try:
        v1 = int(sv_entry.get())
        v2 = int(fv_entry.get())
        label3(Text=v1*v2) #I cannot modify this :(, i need to find another way 
        return v1*v2
    except ValueError: 
        v1 = 0
        v2 = 0
        print('unsuccessful') 

btn = tk.Button(
    mainframe,
    text='Press to multiplicate',
    command=lambda: multiplicationpopup() #we use lambda to anonymize and single insert the function without parameters // needed for a previous error
    )

#for simplification purposes I am not using the frame, declared it just as a test.

label1.pack()
fv_entry.pack()
label2.pack()
sv_entry.pack()
btn.pack()
label3.pack()
window.mainloop()




