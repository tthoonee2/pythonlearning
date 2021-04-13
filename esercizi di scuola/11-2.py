import tkinter as tk
finestra = tk.Tk()

vallue_watt = 0
def set_value_of_kw(value):
    global vallue_watt
    vallue_watt = value

label_up = tk.Label(
    text='choose your consumption in kilowatts:'
)

bn_3 = tk.Button(
    text='3 Kw',
    command= lambda *args: set_value_of_kw(3) )

bn_45= tk.Button(
    text='4.5 Kw',
    command= lambda *args: set_value_of_kw(4.5)
)

bn_6 = tk.Button(
    text='6 Kw',
    command= lambda *args: set_value_of_kw(6)
)
label_up.pack()
bn_3.pack()
bn_45.pack()
bn_6.pack()
